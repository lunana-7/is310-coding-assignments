# AI Workflow

## Planned AI Tool
For this semester in **IS310: Culture as Data**, I plan to use **Google Antigravity** as my primary AI development assistant and coding environment.

---

## AI Interaction Log for "Init IS310" Assignment

### Purpose
I used Antigravity to verify my local environment setup (Python, Git, and Antigravity) via the terminal and ensure all repository requirements aligned with the assignment specifications and the IS310 GitHub Style Guide.

---

### Prompts & AI Exchanges

#### 1. Verifying Tool Installations in Terminal
- **Prompt:** Asked how to check the installation status of Python, Git, and Antigravity using macOS terminal commands.
- **AI Response:** Provided version and path lookup commands (`python3 --version`, `git --version`, `which git`, etc.).
- **Decision & Outcome:** Ran the check in the terminal and confirmed Python 3.14.3 and Git 2.50.1 are installed.

#### 2. Resolving Antigravity Terminal Check
- **Prompt:** Reported `zsh: command not found: agy` after running the initial CLI command.
- **AI Response:** Explained that on macOS, Antigravity is installed as a desktop application bundle (`/Applications/Antigravity.app`) rather than a standalone CLI binary in `$PATH`. Provided a command using `defaults read` to inspect the app's `Info.plist`.
- **Decision & Outcome:** Ran `defaults read "/Applications/Antigravity.app/Contents/Info.plist" CFBundleShortVersionString && ls -d /Applications/Antigravity*.app` and successfully verified version 2.0.6.

#### 3. Course Requirements & Style Guide Review
- **Prompt:** Provided the assignment requirements and asked if anything was missing.
- **AI Response:** Checked the requirements against the IS310 GitHub Style Guide, verified `README.md` and screenshot links in `images/`, and recommended adding a `.gitignore` and expanding `ai-workflow.md` to document the AI interaction.
- **Decision & Outcome:** Added `.gitignore`, documented this AI workflow log, and pushed the complete assignment repository to GitHub.
