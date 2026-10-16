# Movie Culture Notebook — AI-Assisted Pathway 2

This assignment collects movie titles, directors, release years, and short cultural notes through a Python CLI and an HTML form. The topic builds on the movies in my earlier Python foundations assignment. A cultural note is a curator's interpretation or research question, not an objective classification of a movie.

Both interfaces show two examples, collect at least two new records, require all four fields, and ask for review and confirmation. Examples are not automatically included in the output. Both export a JSON list of dictionaries with `title`, `director`, `year` (an integer), and `cultural_note`. Release years must be whole numbers from 1888 through the current year. This range is a practical input constraint; it does not establish a universal beginning of cinema.

## Install and run the Python CLI

Use Python 3.10 or newer. From the repository root, create the course environment if it does not already exist:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r python-libraries/requirements.txt
python python-libraries/cli_data_entry.py
```

On Windows PowerShell, use `python -m venv .venv` and `.\.venv\Scripts\Activate.ps1` instead of the first two commands. Keep one `.venv` for the course repository; it is ignored by Git. The requirements file records the packages installed for this assignment.

Enter each movie's fields, then answer `yes` or `no` at the confirmation prompt. A `no` asks you to re-enter that movie. After two confirmed records, you can add more or finish. No records are written until the collection is finished. Ctrl+C cancels without saving that session.

The script saves beside itself as `movies_001.json`, then `movies_002.json`, and so on, using the next available filename. It prints the full file path. It works even when launched from another directory. The included `movies_001.json` was produced by running the CLI with two confirmed records; running it now will create a later numbered file.

## Run the HTML interface

Open `index.html` in a browser. Keep `style.css` and `script.js` in the same folder. No server or package installation is needed.

1. Complete every field and select **Review entry**.
2. Select **Edit entry** to correct the draft, or **Confirm and add** to add it to the table.
3. Repeat for a second movie. Then select **Download JSON** to save `movies_web.json` through your browser.

You can add more than two movies. Only confirmed records are downloaded. The browser chooses the download location, usually Downloads. Records are held only in the open tab and disappear on refresh or close, so download before leaving.

## Comparing the interfaces

The CLI gives one prompt at a time, which makes the order clear, but correcting a rejected movie means typing all its fields again. Its advantage is saving directly to a known local path. The HTML form shows all fields together, keeps draft values when editing, and displays confirmed records in a table. This makes comparisons easier, although the user must explicitly download the file.

The fields and output schema are identical. The CLI validates through loops and explicit yes/no prompts. HTML uses labels, required fields, a number input, whitespace checks, and separate review/confirm buttons. These different controls changed the instructions and correction flow without changing what cultural material is collected.

Codex generated the two interfaces, styling, setup instructions, sample entries, and documentation, and ran checks. During testing, Codex fixed Rich's wrapping of long output paths. The solution uses simple local JSON files rather than a server, and preserves previous CLI output with numbered filenames. These are AI implementation choices; no independent student revisions or rejected AI suggestions are claimed. The student should review the code and add any later personal changes to the AI log.

For a peer collecting a small movie dataset, the HTML interface is the better fit because they can see the fields, edit their notes, and compare records before downloading. The CLI is useful for someone already working in a terminal. Both leave cultural interpretation to the person entering the note, and neither verifies movie facts or the interpretation itself.

## Verification

- Python CLI run successfully using the project virtual environment and Rich.
- Checked empty fields, invalid years, invalid yes/no answers, rejected entries and re-entry, two confirmed records, integer years in JSON, full output path, cancellation, and preservation of earlier files.
- Generated the included sample by running the actual CLI.
- JavaScript syntax check passed. A simulated-DOM check exercised review/edit, whitespace rejection, confirmation, duplicate confirmation protection, the two-record download threshold, literal text handling, and JSON export contents.
- Browser rendering, native HTML validation, and an actual browser download still need manual verification. The assistant's browser tool blocked local-file navigation. To check manually: try an empty field and an invalid year, review and edit a draft, confirm two movies, download JSON, and open the downloaded file.

## Submission and peer testing

The submission folder should contain this README, `cli_data_entry.py`, `requirements.txt`, `movies_001.json`, `ai-chat-log.md`, `index.html`, `style.css`, and `script.js`.

After pushing, post this assignment folder's GitHub link in the course's appropriate Fall 2026 Discussions thread. Posting and peer testing are not completed by these files.

For peer testing, choose a classmate's CLI or HTML interface, enter at least two records, and reply with the interface tested, actual generated data/output, and constructive feedback. Do not claim that testing happened before doing it. A reply can follow this outline:

- Interface tested: [classmate and CLI or HTML]
- Output: [attach the actual file or paste the actual output]
- Worked well: [specific observation from the test]
- Could be clearer: [specific suggestion from the test]
