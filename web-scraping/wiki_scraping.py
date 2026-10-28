"""Compare documentation of works in GhibliWiki's two director galleries.

Run from the repository root: .venv/bin/python web-scraping/wiki_scraping.py
Only index and work landing pages are fetched; linked subpages are counted,
not downloaded. No page text or images are redistributed.
"""

import csv
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table

BASE_URL = "https://nausicaa.net"
INDEX_URL = f"{BASE_URL}/wiki/Main_Page"
ROBOTS_URL = f"{BASE_URL}/robots.txt"
POLICIES = [
    f"{BASE_URL}/wiki/GhibliWiki:About",
    f"{BASE_URL}/wiki/GhibliWiki:General_disclaimer",
    f"{BASE_URL}/wiki/GhibliWiki:Privacy_policy",
]
USER_AGENT = (
    "is310-course-scraper/1.0 (Min Kim; "
    "https://github.com/lunana-7/is310-coding-assignments; educational homework)"
)
REQUEST_DELAY = 2
OUTPUT_DIR = Path(__file__).resolve().parent
GROUPS = {"Miyazaki": "Hayao Miyazaki", "Takahata": "Isao Takahata"}
console = Console()


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class WikiClient:
    """Identify the project, check robots, and space every request apart."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        self.robots = RobotFileParser()
        self.request_log = []
        self.delay = REQUEST_DELAY

    def download(self, url, check_robots=True):
        # No automatic redirects: a redirect could lead to a disallowed path.
        if urlsplit(url).netloc != urlsplit(BASE_URL).netloc:
            raise ValueError("Requests must stay on the chosen wiki.")
        if check_robots and not self.robots.can_fetch(USER_AGENT, url):
            raise RuntimeError(f"robots.txt disallows {url}")
        entry = {"requested_at_utc": utc_now(), "url": url, "http_status": "", "error": ""}
        try:
            response = self.session.get(url, timeout=30, allow_redirects=False)
            entry["http_status"] = response.status_code
            if response.status_code != 200:
                entry["error"] = f"HTTP {response.status_code}; not parsed"
                return None
            if any(marker in response.text.lower() for marker in
                   ("just a moment...", "enable javascript and cookies")):
                raise RuntimeError("Bot challenge encountered; stop rather than bypass it.")
            return response
        except requests.RequestException as error:
            entry["error"] = str(error)
            return None
        finally:
            self.request_log.append(entry)
            time.sleep(self.delay)

    def check_rules(self):
        response = self.download(ROBOTS_URL, check_robots=False)
        if response is None:
            raise RuntimeError("Cannot verify robots.txt; no articles will be requested.")
        (OUTPUT_DIR / "robots_snapshot.txt").write_text(response.text, encoding="utf-8")
        self.robots.parse(response.text.splitlines())
        self.delay = max(REQUEST_DELAY, self.robots.crawl_delay(USER_AGENT) or 0)

    def soup(self, url):
        response = self.download(url)
        if response is None:
            return None
        if "html" not in response.headers.get("Content-Type", "").lower():
            raise RuntimeError(f"Expected HTML at {url}")
        return BeautifulSoup(response.text, "html.parser")


def discover_works(soup):
    """Level 1: discover work links in the two named index galleries."""
    works = []
    for anchor_id, director in GROUPS.items():
        anchor = soup.find(id=anchor_id)
        if anchor is None:
            raise ValueError(f"Missing index section: {anchor_id}")
        gallery = anchor.find_next("ul", class_="gallery")
        if gallery is None:
            raise ValueError(f"Missing gallery: {anchor_id}")
        seen = set()
        for link in gallery.select(".gallerytext a[href]"):
            href = link["href"]
            parts = urlsplit(href)
            # Exclude edit/red links, query strings, files, and off-site links.
            if (parts.netloc or not parts.path.startswith("/wiki/")
                    or parts.query or parts.fragment or parts.path.startswith("/wiki/File:")):
                continue
            url = urljoin(INDEX_URL, href)
            if url in seen:
                continue
            seen.add(url)
            works.append({"title": link.get_text(" ", strip=True),
                          "director_group": director, "source_url": INDEX_URL,
                          "source_section": anchor_id, "page_url": url})
    if not works or len(works) > 30:
        raise ValueError("Unexpected sample size; inspect index before continuing.")
    return works


def measure_work(work, soup):
    """Level 2: measure the work landing page, preserving missing data."""
    record = {**work, "retrieved_at_utc": utc_now(), "work_type": "",
              "word_count": "", "character_count": "", "internal_link_count": "",
              "unique_internal_link_count": "", "linked_subpage_count": "",
              "measurement_status": "download_failed"}
    if soup is None:
        return record
    content = soup.select_one("#mw-content-text .mw-parser-output")
    if content is None:
        record["measurement_status"] = "missing_article_content"
        return record
    # Keep tables/captions, but remove script/style and the table of contents.
    for element in content.select("script, style, .toc, .mw-editsection"):
        element.decompose()
    text = content.get_text(" ", strip=True)
    header = content.find("table")
    type_label = header.find("b") if header else None
    record["work_type"] = type_label.get_text(" ", strip=True).rstrip(":") if type_label else "Unknown"
    links = []
    for link in content.select("a[href]"):
        parts = urlsplit(link["href"])
        if (not parts.netloc and parts.path.startswith("/wiki/")
                and not parts.query and not parts.fragment):
            links.append(parts.path)
    # Count destinations to this work's related subpages, without visiting them.
    page_path = unquote(urlsplit(work["page_url"]).path)
    related = {path for path in links if unquote(path).startswith(page_path + "_(")}
    record.update({"word_count": len(text.split()), "character_count": len(text),
                   "internal_link_count": len(links), "unique_internal_link_count": len(set(links)),
                   "linked_subpage_count": len(related), "measurement_status": "ok"})
    return record


def save_csv(records, path):
    if not records:
        raise ValueError("No rows to save")
    with path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def main():
    client = WikiClient()
    started = utc_now()
    try:
        client.check_rules()
        # These policies were manually reviewed before the initial collection.
        # Fetch them again to record availability; changed rules need human review.
        for policy in POLICIES:
            if client.soup(policy) is None:
                raise RuntimeError(f"Cannot recheck community policy: {policy}")
        index = client.soup(INDEX_URL)
        if index is None:
            raise RuntimeError("Cannot download index")
        works = discover_works(index)
        records = []
        for number, work in enumerate(works, 1):
            console.print(f"{number}/{len(works)}: {work['title']}", markup=False)
            records.append(measure_work(work, client.soup(work["page_url"])))
        save_csv(records, OUTPUT_DIR / "ghibli_wiki_data.csv")
        table = Table(title="GhibliWiki landing-page documentation")
        for label in ("Work", "Director group", "Type", "Words", "Unique links", "Status"):
            table.add_column(label)
        for row in records:
            table.add_row(row["title"], row["director_group"], row["work_type"],
                          str(row["word_count"]), str(row["unique_internal_link_count"]), row["measurement_status"])
        console.print(table)
        metadata = {"started_at_utc": started, "finished_at_utc": utc_now(),
                    "user_agent": USER_AGENT, "delay_seconds": client.delay,
                    "index_url": INDEX_URL, "robots_url": ROBOTS_URL, "policy_urls": POLICIES,
                    "records": len(records), "successful_measurements": sum(r["measurement_status"] == "ok" for r in records)}
        (OUTPUT_DIR / "run_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        console.print(f"Saved: {OUTPUT_DIR / 'ghibli_wiki_data.csv'}", markup=False, soft_wrap=True)
    finally:
        if client.request_log:
            save_csv(client.request_log, OUTPUT_DIR / "request_log.csv")
        client.session.close()


if __name__ == "__main__":
    main()
