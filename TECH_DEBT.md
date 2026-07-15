# Technical Debt & Refactoring Checklist

This document details the existing technical debt, architectural constraints, and refactoring targets for future phases of development.

---

## 1. Pending & Postponed Migrations

* **Domain Name Transition:** 
  * Currently, all canonical URLs, Open Graph schemas, dynamically updated link targets, and title suffixes are hardcoded to `erdembridge.com`.
  * **Target:** Update all references of `https://www.erdembridge.com` and `erdembridge.com` to `https://www.bricdersi.net` and `bricdersi.net`.
* **Google Play Link Package:** 
  * The download link currently targets `com.erdembridge.quiz`.
  * **Target:** Update if the application is republished under a new namespace.

---

## 2. Code Size & Asset Inlining (index.html)

The main landing page `index.html` has grown to over **570 KB** due to extensive asset inlining.

* **Base64 Inlined Images:** 
  * The file contains 7 large base64-encoded image strings (favicons, logos, illustrations) totaling about 345 KB.
  * **Refactoring Target:** Extract all inline base64 strings into standalone files inside an `/assets/images/` directory to clean up raw HTML editing.
* **Inline CSS and JS:**
  * It features 38 KB of inline CSS and 24 KB of inline Javascript.
  * **Refactoring Target:** Split inline styles into `/assets/css/styles.css` and inline script blocks into `/assets/js/app.js`.

---

## 3. Tooling & Bundling

* **Build Pipeline:**
  * There is currently no compiler, package manager (`package.json`), or bundler (e.g. Vite, Webpack). It relies on global scope variables and raw DOM selectors.
  * **Target:** Migrate to a modern Vite setup, split components, bundle assets, and use ES Modules.

---

## 4. Security Mechanics (Editor Access)

* **Client-Side Passcode Verification:**
  * The Question Database Editor lock check (`CORRECT_PASSCODE = 'erdembridge2026'`) is hardcoded directly inside client-side JS (`json/index.html`).
  * While this is simple and sufficient for basic control, anyone with browser DevTools can inspect the source code to find the passcode.
  * **Target:** Implement token authentication or server-side passcode checks.
