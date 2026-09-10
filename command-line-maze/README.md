# Min's Cultural Soundstage: A Command Line Maze

**Author:** Min Kim  
**GitHub:** [@lunana-7](https://github.com/lunana-7)  
**Hypothesis Username:** [`lunana-7`](https://hypothes.is/users/lunana-7)  
**Group:** A2 (Music & Cultural Data)  
**Assignment:** IS 310 - Lost & Found in the Cultural Command Line  

---

## Welcome to Min's Music Maze!

Hi, welcome to Min's Maze! I am working with group **A2** regarding the **music topic**. In this maze, you will explore cultural data and hip-hop lyricism (featuring Kanye West, 2Pac, Kendrick Lamar) by navigating directories and solving command-line puzzles.

Your goal is to find the **Center of the Maze** (the Main Stage / Solution Room).

---

## Rules & How to Play

1. **Terminal Only:** To navigate through the maze you'll need to use the command line. You are welcome to ask for help from the Instructors or your peers or your AI chatbot, but you **CANNOT** use your graphic file explorer (Finder / File Explorer).
2. **Clues & Word Counts:** You will primarily have to solve clues and then either print out the text or count the numbers of words.
3. **Dead Ends:** If you find an empty file or your word count equals zero, that's a dead end and you'll need to turn around!
4. **Hidden Paths:** Keep an eye out for hidden directories that begin with a dot (`.`). You will need special flags to reveal them!

---

## Getting Started: Unzipping the Maze

Before entering the maze, you must unzip `maze.zip` inside this folder.

### Unix / macOS / Linux:
```bash
unzip maze.zip
```
Then step into the entrance:
```bash
cd entrance
cat clues.txt
```

### Windows (PowerShell):
```powershell
Expand-Archive -Path "maze.zip" -DestinationPath "."
```

#### ⚠️ Windows Note (Hiding Dotfiles):
To ensure hidden files and directories behave properly on Windows PowerShell, run the provided script after unzipping:
```powershell
.\hide-dotfiles.ps1
```
*If you encounter permission issues in PowerShell, run:*
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass .\hide-dotfiles.ps1
```

---

## Useful Command-Line Cheat Sheet

Here are the primary commands you will need to solve this maze:

| Command | Description | Example Usage |
| :--- | :--- | :--- |
| `cd <dir>` | Change directory | `cd entrance` or `cd door_1` |
| `cd ..` | Move back up one directory level | `cd ..` |
| `ls` | List files and directories in current folder | `ls` |
| `ls -a` | List **all** files including hidden dotfiles | `ls -a` |
| `cat <file>` | Display full contents of a file | `cat clues.txt` |
| `head -n <N> <file>` | View the first N lines of a file | `head -n 20 track_changes.txt` |
| `wc -w <file>` | Count total words in a file | `wc -w track_changes.txt` |
| `grep -i -c "<term>" <file>` | Count occurrences of a specific word | `grep -i -c "daughters" violent-crime.txt` |

---

## Completion & Submission

Once you reach the final center of the maze and see the victory banner:
1. Take a screenshot of the solved maze banner in your terminal.
2. Reply to my post in our class GitHub Discussion: [GitHub Discussion #2](https://github.com/CultureAsData-UIUC/is310-fall-2026/discussions/2) with your screenshot!

Best of luck! 🎧🎤