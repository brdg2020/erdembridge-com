# Changelog

All notable changes and optimization work for this project are documented in this file to prepare the codebase for future developers and AI agents (such as Claude).

## [1.1.0] - 2026-07-15

### Cleaned & Refactored
* **Duplicate JS Removals:** 
  * Removed the redundant first `<script>` block in [index.html](file:///C:/Users/Erdem/.gemini/antigravity/scratch/erdembridge-com/index.html) containing the duplicate `checkQuizAnswer` function.
  * Removed the duplicate first declarations of `switchTab` and `switchSubTab` in [index.html](file:///C:/Users/Erdem/.gemini/antigravity/scratch/erdembridge-com/index.html) (overridden by the full hash-routing and metadata-enabled definitions later in the file).
* **Code Documentation & Structure:**
  * Added clean, numbered section headers and documentation comments in [index.html](file:///C:/Users/Erdem/.gemini/antigravity/scratch/erdembridge-com/index.html) covering accordions, routing, meta updates, tab navigation, quiz logic, and theme toggling.
  * Documented core features of [json/index.html](file:///C:/Users/Erdem/.gemini/antigravity/scratch/erdembridge-com/json/index.html) (dealers rotation map, 4-column bidding render matrix, HCP calculations, hand sanitization, and the Safari container width safety wrapper).
  * Documented parsing loops, suit translations, vulnerability indices, and download anchors in [pbntolin/index.html](file:///C:/Users/Erdem/.gemini/antigravity/scratch/erdembridge-com/pbntolin/index.html).

### Postponed/Noted
* **Domain Migration (To Be Done Later):** The migration of domain names from `erdembridge.com` to `bricdersi.net` in canonicals, schemas, titles, and paths has been postponed per user request to preserve current production alignments. It will be conducted during the next phase of deployment.
* **Google Play App Package Link:** The package identifier `com.erdembridge.quiz` remains unchanged in the download link to avoid breaking connection with the live store application.

---

## [1.0.0] - 2026-07-07

### Added
* **Hand Cards Input Validation & Rules:**
  * Configured automatic uppercase rank conversions (`A, K, Q, J, 9-2`) and keyboard filter guards.
  * Implemented an autocomplete listener to replace `T` (or `t`) characters with `10` dynamically.
  * Enforced a strict maximum limit constraint capping the total sum of cards across all four suits (Spades, Hearts, Diamonds, Clubs) at exactly 13 cards.
  * Programmed live High Card Points (HCP) calculator counting values of honors (`A=4, K=3, Q=2, J=1`) and total cards count dynamically.
* **BBO Interactive Bidding Box & Flow Grid:**
  * Created interactive level (1-7), denomination (♣, ♦, ♥, ♠, NT), and special calls (Pass, Dbl, Rdbl, ?) button controls.
  * Implemented clockwise dealer rotation sequencer automatically ordering bidding seats based on dealer select field.
  * Rendered sequential bids in a 4-column layout table representing West, North, East, South.
* **UI Layout Enhancements:**
  * Capped edit form card width to `max-width: 720px` to enhance typing ergonomics.
  * Embedded the edit form card within a standard container wrapper `#rightColumn` to resolve grid rendering collapse issues on mobile webkit/Safari browsers.
  * Doubled the scale of suit symbol toolbar insert controls for ease of touch selection.
* **Security lock screen:**
  * Integrated a passcode lock gate (`CORRECT_PASSCODE = 'erdembridge2026'`) to restrict unauthorized access to the editor.
