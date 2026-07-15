# Bridge Training & Quiz Platform (bricdersi.net / erdembridge.com)

Welcome! This repository hosts a single-page interactive bridge training application, a daily question JSON database editor, and a PBN-to-LIN converter utility. 

This project is fully ready for deployment via Firebase Hosting and is optimized to run with zero build steps (Vanilla HTML, CSS, and JS).

---

## Quick Start

### Running Locally
To test the project locally, run a static file server in the root directory:
```bash
# Python 3
python -m http.server 8000

# Node.js (http-server)
npx http-server -p 8000
```
Open your browser and navigate to `http://localhost:8000`.

### Deploying to Firebase
The platform is deployed using Firebase Hosting.
```bash
# Install Firebase CLI if not already installed
npm install -g firebase-tools

# Login and deploy
firebase login
firebase deploy --only hosting
```

---

## Project Structure at a Glance
* **`index.html`**: The main public interactive training portal (SPA with hash routing).
* **`json/index.html`**: Hashed passcode-locked visual question editor for `questions.json`.
* **`pbntolin/index.html`**: File converter to translate PBN files into BBO's LIN format.
* **`CHANGELOG.md`**: Chronological log of recent structural improvements and fixes.

---

## Developer Transition Documents
To quickly understand the project before writing code, please review the following developer notes:
1. **[Architecture & Design Flows (`ARCHITECTURE.md`)](ARCHITECTURE.md)**: SPA routing, layout constraints, passcode system, and live validator loops.
2. **[Detailed File Inventory (`PROJECT_STRUCTURE.md`)](PROJECT_STRUCTURE.md)**: Directory map and file descriptions.
3. **[Technical Debt & Refactoring Checklist (`TECH_DEBT.md`)](TECH_DEBT.md)**: Postponed migrations, performance debt, and split targets.
4. **[AI Transition Notes (`CLAUDE_NOTES.md`)](CLAUDE_NOTES.md)**: Special guide specifically compiled for Claude or next-generation AI agents to execute edits safely.
