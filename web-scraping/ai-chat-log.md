# AI use — Community Wikis and Web Scraping

Date: October 28, 2026 (America/Chicago)
Tool: OpenAI Codex

This file summarizes the relevant exchange and work; it is not a verbatim transcript of all generated code and tool output. The submitted scripts preserve the implemented code.

## User request (verbatim)

> also do this hw and submit the work

The user attached the course's Web Scraping with Python lesson and Community Wikis and Web Scraping assignment. Earlier in the conversation, the user had chosen Studio Ghibli movie culture for a previous assignment.

## Assistant contributions

Codex read the assignment and repository, searched for an independent Ghibli wiki, and checked Nausicaa.net with an identifying User-Agent. The web search reader could not fetch its robots file and main wiki page, but ordinary requests with the declared project header received actual HTTP 200 HTML without a browser challenge. No bot protection was bypassed. Codex inspected robots, the About page, general disclaimer, privacy policy, and a sample article before collection.

Codex proposed comparing documentation in GhibliWiki's Miyazaki and Takahata galleries to continue the existing topic. It created `wiki_scraping.py` with requests, BeautifulSoup, a robots check, two-second pauses, status checks, a bounded two-level workflow, CSV export, and source/run logs. It created an offline `first_web_scraper.py` warm-up and four regression tests. It installed requests and BeautifulSoup in the existing course environment and recorded versions with the already-used Rich package.

The live run fetched the main index and followed discovered work links. It generated 21 real records and 26 successful request-log entries in the final run. Preliminary inspection requests were separate. Codex validated CSV counts and provenance and calculated medians for the rows explicitly labeled Feature Film. It wrote the README's source justification, operational definitions, findings, limits, and setup instructions.

## Choices and limitations

The galleries contain different kinds of works, not just feature films. Codex kept every discovered work in the dataset and separated the feature-film comparison rather than silently treating advertisements or shorts as feature films. One missing type label remained Unknown. Failed or missing measurements are designed to remain blank instead of becoming zero.

The measurements include some article tables and captions. They omit the bodies of related FAQ/story/credits pages. Link counts can include file/help links and exclude absolute same-site links. These choices are documented because they affect interpretation. Codex did not invent a student email address, reproduce full articles or images, or claim the results prove popularity. No independent student edits or rejected AI suggestions occurred in this exchange.

## Submission

The user explicitly requested submission. Codex checked the specified course Discussion #7 and the authenticated GitHub account, and confirmed there was no existing submission by `lunana-7` at the time of that check. The intended submission is a brief post identifying Min Kim and linking to the completed web-scraping folder. No class section is invented.
