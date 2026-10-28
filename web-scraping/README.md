# GhibliWiki: two directors, different documentation?

**Min Kim · IS310 · Community Wikis and Web Scraping**

## Wiki and research question

This project uses [GhibliWiki](https://nausicaa.net/wiki/Main_Page), the independent, community-run wiki at Nausicaa.net. Its [About page](https://nausicaa.net/wiki/GhibliWiki:About) describes a collaboration between Team Ghiblink and visitors, rather than an official Studio Ghibli site. This continues the Ghibli topic from my earlier data-entry homework.

**Question:** How do the works listed in GhibliWiki's Hayao Miyazaki and Isao Takahata galleries differ in landing-page length, internal links, and links to related subpages?

These measurements can help a researcher locate uneven documentation and decide which parts of this English-language fan archive deserve closer reading. The data represents the wiki's organization of cultural material, rather than audience responses to the films.

## Responsible collection and policies

Reviewed on October 28, 2026:

- [robots.txt](https://nausicaa.net/robots.txt): the general `User-agent: *` group disallows `/w/` but does not disallow the `/wiki/` article URLs used here. Several named crawlers are forbidden from the entire site; comments object to whole-site copying and excessive request rates. Later specialized path directives occur under the final named crawler group. This project uses its own honest identifier, reads robots before article requests, never requests `/w/` assets or edit pages, and does not disguise itself as a browser or search engine. Robots rules are operational signals, not permission to republish everything.
- [About GhibliWiki](https://nausicaa.net/wiki/GhibliWiki:About): describes its community and scope.
- [General disclaimer](https://nausicaa.net/wiki/GhibliWiki:General_disclaimer): identifies a volunteer, fan-maintained resource, acknowledges third-party copyrights, and cautions that accuracy is not guaranteed.
- [Privacy policy](https://nausicaa.net/wiki/GhibliWiki:Privacy_policy): states the site's privacy commitments. This project does not collect user profiles, account details, contributor histories, or discussion posts.
- The wiki footer identifies contributed content as [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/), unless otherwise noted. Every dataset row attributes its source page and index section. This noncommercial educational project shares titles, provenance, and derived measurements; it does not redistribute article bodies, artwork, or translations. Where reuse of wiki contributions requires a license, CC BY-NC-SA 3.0 applies; no ownership of third-party material is claimed.

No additional scraping prohibition was found on the reviewed community pages. The script uses a two-second `time.sleep()` after every request (including failed ones), honors a longer crawl delay if provided, checks status codes, does not parse non-200 responses, and stops on a detected bot challenge. Redirects are not automatically followed. If the site blocks access or its rules change, stop and reconsider the source rather than bypassing restrictions.

The exact identifying header is:

```text
is310-course-scraper/1.0 (Min Kim; https://github.com/lunana-7/is310-coding-assignments; educational homework)
```

The GitHub project URL provides an actual contact route without inventing an Illinois email address.

## Two levels of pages and scope

1. **Index:** parse `Main_Page` and locate the `Miyazaki` and `Takahata` section anchors. Extract work links from `.gallerytext` inside each following gallery, rather than hard-coding a list of movie URLs. Deduplicate within each gallery and reject external, edit, file, query, and fragment links.
2. **Individual work pages:** follow those links and measure `#mw-content-text .mw-parser-output`. Record the work-type label from the first table, text length, internal links, and links to related subpages.

The sample is deliberately bounded to these two galleries, with a safety cap of 30 records. It includes the works actually listed there, including shorts and advertisements, rather than assuming every entry is a feature film or that the galleries are a complete filmography. The dataset's `director_group` records an editorial grouping, not an independently verified production credit. Linked story, FAQ, credits, and availability pages are counted as destinations but are not fetched. Policy and robots requests are preliminary checks, not a substitute for the two content levels.

## Setup and run

From the repository root, use the course's existing `.venv`. If needed, create it first with `python3 -m venv .venv`.

```sh
source .venv/bin/activate
python -m pip install -r web-scraping/requirements.txt
python web-scraping/first_web_scraper.py
python web-scraping/wiki_scraping.py
```

On Windows PowerShell, activate with `.\.venv\Scripts\Activate.ps1`; use `python -m venv .venv` to create the environment if necessary. The scraper requires Python 3.10 or newer and internet access. It runs sequentially and normally takes about a minute or two. Outputs are saved beside the script regardless of the terminal's working directory. A new run replaces the previous dataset and run logs, so copy them elsewhere first if preserving a snapshot.

`first_web_scraper.py` is a small offline BeautifulSoup exercise adapted from the lesson; `wiki_scraping.py` performs the live assignment collection with requests and BeautifulSoup. Rich provides the terminal preview.

## Files and data dictionary

| File | Purpose |
| --- | --- |
| `wiki_scraping.py` | Actual two-level scraper |
| `first_web_scraper.py` | Offline lesson warm-up |
| `ghibli_wiki_data.csv` | Actual collected data, UTF-8 CSV |
| `requirements.txt` | Installed dependency versions |
| `robots_snapshot.txt` | Robots rules returned during the run |
| `request_log.csv` | Each run request's timestamp, URL, status, and error |
| `run_metadata.json` | Run times, identity, source/policy URLs, delay, and record totals |
| `test_wiki_scraping.py` | Offline regression checks |
| `ai-chat-log.md` | AI use and troubleshooting record |

| CSV field | Meaning |
| --- | --- |
| `title` | Work's link text on the index |
| `director_group` | Director gallery in which the work was discovered |
| `source_url`, `source_section` | Discovery provenance |
| `page_url` | Attributed work page |
| `retrieved_at_utc` | UTC timestamp recorded when processing the request result |
| `work_type` | Bold label in the first article table, or `Unknown` |
| `word_count` | Number of whitespace-separated tokens in selected text |
| `character_count` | Length of selected Unicode text, including spaces and punctuation |
| `internal_link_count` | All qualifying relative `/wiki/` link occurrences |
| `unique_internal_link_count` | Distinct qualifying encoded destination paths |
| `linked_subpage_count` | Distinct paths whose decoded name begins with this work's path plus `_(` |
| `measurement_status` | `ok`, `download_failed`, or `missing_article_content` |

Text is extracted with `get_text(" ", strip=True)` after removing scripts, styles, table-of-contents elements, and edit controls. Tables, navigation within the article, captions, and translated titles remain. Link counts exclude query strings and fragments, but include file/category/help links if they occur in the article. Absolute links are excluded even when they point to the same wiki. Link uniqueness compares encoded paths literally, so equivalent spellings may count separately. Subpage counts describe visible links to existing destinations, not a verified inventory of every related page. Missing measurements are blank rather than misleading zeros.

## What these measurements mean

Page length and link counts measure the structure of selected landing pages, not film quality, popularity, cultural importance, or the size of a fandom. A short page may send readers to a large story or FAQ subpage that this scraper does not visit. Standard navigation tables can inflate length and links, and whitespace-based word counts handle English and Japanese differently. The two director galleries have different numbers and kinds of works; raw group totals would therefore be a misleading comparison. Even a feature-film-only comparison remains shaped by page age, volunteer labor, templates, and the wiki's coverage. Someone would be wrong to conclude that a director or film with more words is more culturally valuable or more loved. These results identify documentation patterns that need close reading and other evidence to interpret.

## Verification

Run the network-free checks from the repository root:

```sh
python -m unittest discover -s web-scraping -p 'test_*.py' -v
```

The checks cover two-gallery discovery, filtering and deduplication, article/link/subpage measurements, missing-data handling, a non-200 response, request delays, and robots blocking. Actual collection and dataset checks are summarized below.

## Collected results — October 28, 2026

The live run collected **21 distinct work pages: 16 in the Miyazaki gallery and 5 in the Takahata gallery**. All 26 requests in the final run (robots, three policy pages, the index, and 21 works) returned HTTP 200; every work had the expected article container. Four offline tests passed, and the output was checked for unique page URLs, positive text counts, and consistent total/unique/subpage link counts. Run timestamps and source URLs are in the accompanying logs. Preliminary source/policy inspection requests preceded this final run and are not included in its request log.

Because the galleries mix work types, the table compares only rows whose extracted label is exactly `Feature Film`. Medians are calculated per page, rather than summing differently sized groups.

| Director gallery | Feature-film pages | Median words | Median characters | Median all internal links | Median unique internal links | Median linked subpages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Hayao Miyazaki | 10 | 201 | 1185.5 | 15 | 13 | 9 |
| Isao Takahata | 5 | 226 | 1371 | 12 | 11 | 7 |

In this snapshot, Takahata's feature-film landing pages had a higher median word count, while Miyazaki's had more internal destinations and related subpage links. This is a difference in landing-page documentation, not evidence that one director has more fans. The wiki's habit of distributing material across related pages makes a simple “longer means more attention” argument especially weak. `Imaginary Flying Machines` received `Unknown` for its type because the expected label was absent from the first table; it remains in the CSV but is excluded from the feature-film comparison.

To reproduce the feature-film summary without making new requests:

```sh
python - <<'PY'
import csv
from statistics import median
with open('web-scraping/ghibli_wiki_data.csv', encoding='utf-8', newline='') as file:
    rows = list(csv.DictReader(file))
for director in ('Hayao Miyazaki', 'Isao Takahata'):
    films = [r for r in rows if r['director_group'] == director
             and r['work_type'] == 'Feature Film' and r['measurement_status'] == 'ok']
    print(director, len(films), {
        key: median(int(r[key]) for r in films)
        for key in ('word_count', 'character_count', 'internal_link_count',
                    'unique_internal_link_count', 'linked_subpage_count')
    })
PY
```

## AI assistance

Codex helped choose and inspect the source, implement and test the scraper, run the actual collection, calculate summaries, and write the documentation. See `ai-chat-log.md`. The data comes from real HTTP requests, not AI-generated measurements. The interpretive question and reflection are AI-assisted drafts that I remain responsible for understanding.
