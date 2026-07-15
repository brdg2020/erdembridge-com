# Project Structure & Inventory

This document maps out all files and directories in this repository.

---

## Directory Map

```
erdembridge-com/
├── .firebase/                  # Firebase CLI cache files
├── json/
│   └── index.html              # Question Database Editor page
├── pbntolin/
│   └── index.html              # PBN to LIN Converter utility
├── ARCHITECTURE.md             # Architecture & design flow descriptions
├── CHANGELOG.md                # Chronological modifications history
├── CLAUDE_NOTES.md             # Developer & AI agent instructions
├── PROJECT_STRUCTURE.md        # File inventory (this file)
├── TECH_DEBT.md                # Postponed tasks & refactoring targets
├── README.md                   # Quick start & deployment guide
├── firebase.json               # Firebase Hosting configuration file
├── .firebaserc                 # Firebase project target aliases
├── index.html                  # Root landing page & SPA training portal
├── robots.txt                  # Crawl directions for search engine bots
├── sitemap.xml                 # XML sitemap for SEO index optimization
├── site.webmanifest            # Manifest metadata for progressive web apps
├── favicon.ico                 # Legacy browser favicon shortcut
├── favicon-16x16.png           # 16px PNG favicon
├── favicon-32x32.png           # 32px PNG favicon
└── apple-touch-icon.png        # iOS homescreen apple touch icon
```

---

## File Inventory & Details

### Public Web Portal
* **`index.html`**
  * **Size:** ~575 KB
  * **Description:** Contains the entire public learning portal, styling, image assets (inlined as base64 strings to ensure fast loading times and single-file portability), and client-side SPA routing.

### JSON Editor Utility
* **`json/index.html`**
  * **Size:** ~67 KB
  * **Description:** Connects to GitHub API to pull/push `questions.json`. Features an interactive BBO-like bidding input box, 4-column bidding grid, and live hand-card validation safeguards.

### File Converter Utility
* **`pbntolin/index.html`**
  * **Size:** ~6.3 KB
  * **Description:** Standard PBN format parsing loop. Rearranges hand ranks clock-wise starting from designated dealer to export BBO compatible LIN strings.

### Configurations
* **`firebase.json`**
  * Configures static routing rules. Rewrites all routing requests (`**`) to `index.html` to allow client-side deep linking while preserving direct loading of subfolder files.
* **`site.webmanifest`**
  * Metadata identifying app shortcuts and color icons for progressive web app (PWA) installation.
