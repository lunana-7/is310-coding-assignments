# AI Chat & Collaboration Log: Cultural Command Line Maze

**Assignment:** Lost & Found in the Cultural Command Line (IS 310)  
**Student:** Min Kim  
**Group:** A2 (Music & Cultural Data)  
**Tool Used:** Google Antigravity  
**Date:** September 6–7, 2026  

---

## 1. Initial Prompt & Objectives
**User Prompt:**
> (Could you check if anything is missing here and create it? Also, I wrote how to play this in readme.md, so based on that, could you delete or replace existing texts like moby-dick.txt?)

**Goals Identified:**
1. Perform a thorough audit against the homework assignment rubric and requirements.
2. Remove old sample Project Gutenberg literature texts (`moby-dick.txt`, `alice-in-wonderland.txt`, `mystery_book.txt`, etc.).
3. Restructure the maze around the student's Group A2 topic: **Music / Hip-Hop Cultural Data**, integrating the user's existing `violent-crime.txt`.
4. Ensure gameplay matches the rules set out in `README.md` (CLI navigation only, using `wc` to count words and `grep` for clues, with empty 0-word files representing dead ends).
5. Add missing cross-platform requirements (`hide-dotfiles.ps1`), document AI usage (`ai-chat-log.md`), and prepare the unzipped structure and `maze.zip`.

---

## 2. Audit Findings & Gap Analysis
During initial investigation, the following issues were diagnosed:
- **Folder Name Syntax:** The directory in the repository was named `" command-line-maze"` with an accidental leading space. This was fixed via `git mv` so peers can run `cd command-line-maze` without path issues.
- **Out-of-Theme Files:** Leftover files from the instructor's sample Gutenberg maze were still present (`moby-dick.txt`, `alice-in-wonderland.txt`, Dracula, Frankenstein files).
- **Missing Required Script:** The Windows helper script `hide-dotfiles.ps1` required by the assignment specification was not yet created.
- **Empty Files:** `ai-chat-log.md` existed but was 0 bytes.
- **README Formatting:** Lacked formal title and author header, command-line cheat sheet, and step-by-step unzip instructions for peers.
- **Packaging:** The required `maze.zip` archive containing the maze structure (excluding `README.md`) was missing.

---

## 3. Architecture & Design Decisions
1. **Cultural Theme Integration:**
   - **Entrance:** Uses Kanye West's *Violent Crimes* (`violent-crime.txt`). The clue asks the player to compare occurrences of "daughters" (4) vs. "karma" (1) using `grep` to select `door_1`.
   - **Studio A (`door_1`):** Features 2Pac's socially conscious masterpiece *Changes* (`track_changes.txt`). Clue requires running `wc -w` (629 words > 500), directing the player to `track_vault_3`.
   - **Production Studio (`track_vault_3`):** Features Kendrick Lamar's *Alright* (`mystery_track.txt`). Clue teaches Unix hidden file concepts (`ls -a`), leading to the dot-directory `.secret_vault`.
   - **Backstage Vault (`.secret_vault`):** Features 5 final doors with `message.txt` files. Dead ends contain 0 words or trap messages; `final_door_3` contains the congratulatory victory banner.
2. **Adherence to Gameplay Rules:**
   - Empty files (0 bytes / 0 words) like `dead_end.txt`, `door_empty_1`, `empty_studio.txt`, and `silent_room.txt` serve as traps that signal players to turn around (`cd ..`).
3. **Cross-Platform Compatibility:**
   - Provided `hide-dotfiles.ps1` with the required PowerShell snippet to hide dotfiles on Windows:
     ```powershell
     Get-ChildItem -Recurse -Force | Where-Object { $_.Name.StartsWith('.') } | ForEach-Object { attrib +h $_.FullName }
     ```

---

## 4. Verification & Testing Steps
The following commands were executed to verify the maze's end-to-end functionality:
1. `grep -i -c "daughters" violent-crime.txt` returned 4; `grep -i -c "karma" violent-crime.txt` returned 1. (Validates path to `door_1`).
2. `wc -w track_changes.txt` returned 629. (Validates path to `track_vault_3`).
3. `ls -a` correctly displayed `.secret_vault`.
4. Verified `final_door_3/message.txt` displayed the victory banner.
5. Checked directory count (12 directories, exceeding >= 5 requirement) and file count (>15 files, exceeding >= 5 requirement).
6. Packaged `entrance/` into `maze.zip` and verified that `README.md` remained unzipped in `command-line-maze/`.
