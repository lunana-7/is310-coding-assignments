# AI Chat & Collaboration Log: Cultural Command Line Maze

**Assignment:** Lost & Found in the Cultural Command Line (IS 310)  
**Student:** Min Kim  
**GitHub Username:** @lunana-7  
**Group:** A2 (Music & Cultural Data)  
**Tool Used:** Google Antigravity (Gemini 3.7 Flash)  
**Dates of Interaction:** September 6–10, 2026  

---

## Overview of AI Collaboration
This log documents the iterative prompts, AI responses, and technical decision-making during the development and refinement of the Cultural Command Line Maze. Google Antigravity was used as a pair programming assistant to audit assignment requirements, structure hip-hop cultural data, craft command-line puzzle logic, solve cross-platform issues, and maintain clean Git repository hygiene.

---

## 1. Initial Prompt: Audit & Theme Replacement

### User Prompt
> "Could you check if anything is missing here? Also, I wrote how to play this in readme.md"

### AI Response & Summary of Action
1. **Rubric Audit & Gap Identification:**
   - Diagnosed an accidental leading space in the folder name (`" command-line-maze"`), standardizing it to `command-line-maze`.
   - Identified leftover Project Gutenberg text files (`moby-dick.txt`, `alice-in-wonderland.txt`, Dracula, Frankenstein) that did not match Group A2's **Music & Cultural Data** focus.
   - Identified missing required deliverables: `hide-dotfiles.ps1` for Windows, unzipped `README.md`, empty `ai-chat-log.md`, and `maze.zip`.
2. **Thematic Replacement:**
   - Retained and integrated Min's existing Kanye West lyric file (`violent-crime.txt`).
   - Planned the replacement of old literary files with hip-hop and music cultural texts: 2Pac's *Changes* (`track_changes.txt`) and Kendrick Lamar's *Alright* (`mystery_track.txt`).

---

## 2. Follow-Up Prompt: Puzzle Design & CLI Mechanics

### User Prompt
> "I want players to navigate only using the terminal. In my README, I specified that players should solve clues using word counts (`wc`) and searching for terms (`grep`), and that 0-word empty files should act as dead ends. How should we arrange the files and clues across the rooms?"

### AI Response & Summary of Action
1. **Designed a 4-Tier Interactive Puzzle Structure:**
   - **Entrance (Kanye West - *Violent Crimes*):** Players analyze `violent-crime.txt` with `grep -i -c "daughters" violent-crime.txt` (returns 4) vs. `grep -i -c "karma" violent-crime.txt` (returns 1). Since "daughters" is greater, the clue directs them to `door_1`.
   - **Studio A / `door_1` (2Pac - *Changes*):** Players run `wc -w track_changes.txt` (629 words). Since it exceeds 500 words, the clue guides them to `track_vault_3`.
   - **Production Studio / `track_vault_3` (Kendrick Lamar - *Alright*):** Clue introduces hidden Unix files, requiring `ls -a` to reveal the `.secret_vault` directory.
   - **Backstage Vault / `.secret_vault`:** Houses five doors (`final_door_1` through `final_door_5`).
2. **Dead-End Architecture:**
   - Placed 0-word / 0-byte trap files (`dead_end.txt`, `empty_studio.txt`, `door_empty_1`, `silent_room.txt`) in wrong rooms (`door_2`, `track_vault_1`, `track_vault_2`), requiring players to recognize empty files and backtrack using `cd ..`.
   - Placed the winning victory banner in `final_door_3/message.txt`.

---

## 3. Follow-Up Prompt: Cross-Platform & Windows Compatibility

### User Prompt
> "The assignment mentions Windows users might have trouble with hidden dot-folders like `.secret_vault` because PowerShell doesn't hide them the same way macOS/Linux does. How do we create the helper script for Windows?"

### AI Response & Summary of Action
1. **Script Implementation (`hide-dotfiles.ps1`):**
   - Created the PowerShell script to automatically locate all dotfiles/folders recursively and apply Windows hidden attributes:
     ```powershell
     Get-ChildItem -Recurse -Force | Where-Object { $_.Name.StartsWith('.') } | ForEach-Object { attrib +h $_.FullName }
     ```
2. **Documentation in README:**
   - Documented exact instructions for PowerShell users on how to run `.\hide-dotfiles.ps1` and how to bypass execution policy restrictions if needed (`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`).

---

## 4. Follow-Up Prompt: Packaging & Verification

### User Prompt
> "Can we verify that all puzzle paths work properly from the command line, and package the maze correctly according to the assignment requirements?"

### AI Response & Summary of Action
1. **Terminal Command Verification:**
   - Verified `grep -i -c "daughters" violent-crime.txt` = 4 and `grep -i -c "karma" violent-crime.txt` = 1 (routes to `door_1`).
   - Verified `wc -w track_changes.txt` = 629 (routes to `track_vault_3`).
   - Verified `ls -a` exposes `.secret_vault`.
   - Verified `cat final_door_3/message.txt` displays the solved ASCII art banner.
2. **Archive Packaging:**
   - Packaged the `entrance/` directory into `maze.zip` using `zip -r maze.zip entrance/`.
   - Verified that `README.md`, `ai-chat-log.md`, and `hide-dotfiles.ps1` remain outside `maze.zip` for peer access.

---

## 5. Maintenance Prompt: Git Hygiene & .DS_Store Cleanup

### User Prompt
> ```bash
> git rm --cached .DS_Store
> git rm --cached images/.DS_Store
> echo .DS_Store >> .gitignore
> git add .gitignore
> git commit -m "Remove DS_Store files"
> git push origin main
> ```
> *"Did this prompt work?"*

### AI Response & Summary of Action
1. **Output Analysis:**
   - Confirmed that Git successfully stopped tracking `.DS_Store` (`rm '.DS_Store'`).
   - Explained that `fatal: pathspec 'images/.DS_Store' did not match any files` was expected and harmless because `images/.DS_Store` had never been tracked.
   - Confirmed that `.DS_Store` was appended to `.gitignore` so macOS system files will never be tracked anywhere in the repository.
   - Confirmed the commit and push (`main -> main`) succeeded on GitHub.

---

## 6. Critical Reflection & AI Evaluation
- **Strengths of AI Assistance:**
  - Fast identification of missing edge cases (rubric requirements such as Windows PowerShell compatibility).
  - Rapid generation of thematic CLI puzzles tied directly to text-analysis commands (`wc`, `grep`).
  - Clear troubleshooting of Git configuration and repository cleanup.
- **Human Oversight & Decision-Making:**
  - Guided the selection of music artists and specific songs relevant to Group A2's cultural data theme.
  - Ensured clues and maze difficulty felt engaging and educational for classmates rather than overly difficult or trivial.
  - Verified and tested each command manually in the terminal to confirm player experience matches the documentation.

