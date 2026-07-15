# Project Architecture & Design Flows

This document details the architectural layout, core functional loops, and UI mechanics of the platform.

---

## 1. Single Page Application (SPA) & SEO Hash Routing

The core website (`index.html`) is structured as a client-side Single Page Application (SPA) to ensure instant transitions between study units and guides without page reloads.

### Routing Mechanics
* **Trigger:** Navigation triggers click handlers calling `switchTab(tabId)` or deep links captured via `handleRouting()`.
* **State Updates:** Tab state is written to the URL hash (e.g. `/#bric-baslangic-rehberi` or `/#konvansiyonlar`).
* **SEO Meta Tag Synchronization:** When a tab changes, `updateMetaTags(tabId)` dynamically updates the page title, description meta tag, canonical link href, and Open Graph/Twitter card tags. This prevents search engines from indexing the SPA as duplicate pages and guarantees accurate metadata matching the visible section.

---

## 2. Question Database Visual Editor (`/json`)

The editor page (`/json/index.html`) is a client-side tool to modify `questions.json` stored in the `brdg2020/BBQData` GitHub repository.

### Key Logic Systems

#### Passcode Lock Gate
* A front-end check validates inputs against the string literal `erdembridge2026`.
* Successful entries store verification in local storage (`bbq_passcode_verified = true`) to bypass the lock screen on subsequent visits.

#### Hand Cards Validator Loop
* **Sanitization:** Typing letters automatically converts input to uppercase, maps the `T` key to `10` immediately on keystroke, and strips non-rank ranks.
* **13-Card Check:** Restricts input across all four suit fields so the absolute sum never exceeds exactly 13 cards.
* **High Card Points (HCP):** Live loops calculate the HCP metrics on every keystroke by mapping `A=4`, `K=3`, `Q=2`, and `J=1` values.

#### Bidding Sequences & Clockwise Rotation
* **Dealer Rotation Sequencer:** The dealer select option determines the starting seat (West, North, East, South). Inserting a bid increments the seat index clockwise sequentially.
* **4-Column Bidding Grid:** The sequential list of bids is transformed into a row-column matrix dynamically. A new row is started if the current bid's seat column index is lower or equal to the previous bid's column index.

#### Safari & Webkit layout safety wrapper
* Mobile webkit engines often collapse layout grids if children have absolute width rules (`max-width: 720px`) inside fractional grid tracks (`1fr`).
* The container `div` `#rightColumn` wraps the form card to act as a layout buffer, keeping the grid track clean and preventing column overlaps.

---

## 3. PBN to LIN Converter (`/pbntolin`)

A self-contained client-side utility (`/pbntolin/index.html`) that parses files in PBN format and outputs BBO's LIN format.

* **Parsing:** RegEx matches brackets (e.g., `[Dealer "N"]`) to build deal objects.
* **Hand Order Conversion:** Rearranges hand ranks clock-wise starting from the designated dealer character.
* **File Download:** Converts raw text to a Blob object and triggers an anchor-click download sequence natively in the browser.
