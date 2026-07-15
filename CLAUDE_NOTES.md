# AI Transition Notes (CLAUDE_NOTES.md)

Hello Claude! This developer note was compiled to help you understand the codebase quickly, avoid breaking active validation systems, and perform modifications safely.

---

## 1. Database Schema (`questions.json`)

The JSON Question Editor modifies a database structured as an array of questions. Every question item in the array MUST strictly follow this JSON schema:

```json
{
  "id": "2026-03-01-atak",
  "date": "2026-03-01",
  "premium": false,
  "titleTr": "Günün Sorusu",
  "titleEn": "Daily Question",
  "playerSeat": "S",
  "playerName": "South",
  "hand": {
    "S": "AKQJ",
    "H": "Q8542",
    "D": "54",
    "C": "32"
  },
  "bidding": [
    {"seat": "S", "call": "Pass"},
    {"seat": "W", "call": "1S"},
    {"seat": "N", "call": "Double"},
    {"seat": "E", "call": "Pass"}
  ],
  "options": [
    "1♠",
    "Pass",
    "♥Q",
    "2♥"
  ],
  "correctAnswer": "A",
  "explanationTr": "Detaylı açıklama buraya yazılır...",
  "explanationEn": "Detailed explanation written here..."
}
```

### Constraints & Form Logic
* **`id`:** Corresponds to the index search string. Must match date and type (e.g., `2026-03-01-atak` or `2026-03-01-konusma`).
* **`hand`:** Only standard bridge ranks (`A, K, Q, J, 10, 9-2`) are allowed. The total sum of ranks across Spade (`S`), Heart (`H`), Diamond (`D`), and Club (`C`) MUST equal exactly 13 cards.
* **`bidding`:** Sequential array of seats (`N, E, S, W`) and calls (e.g., `1C`, `Pass`, `Double`, `Rdbl`, `?`).

---

## 2. Global State Variables in Editor (`json/index.html`)

* **`currentBidding`:** An array of objects representing calls: `[ { seat: "S", call: "Pass" }, ... ]`.
* **`activeBidLevel`:** Stores active selection of level buttons (1-7) in the BBO box. Set to `null` if no level is currently chosen.
* **`CORRECT_PASSCODE`:** String literal value `erdembridge2026`. Used to bypass the lock screen.
* **`handInputs`:** NodeList pointing to Spade, Heart, Diamond, and Club HTML inputs.

---

## 3. UI & Layout Warning Tags

* **Safeguard Wrapper (`#rightColumn`):**
  * **Warning:** Do NOT remove the parent wrapper element `#rightColumn` and attach form constraints directly to `#formCard`.
  * **Reason:** Without this separate wrapper layer, grid tracking algorithms in WebKit/Safari mobile browsers collapse column width when interactive elements are toggled.
* **T-Key Auto-Mapping:**
  * **Warning:** The keystroke listener for hand card inputs automatically replaces the character `T` with `10`. Ensure any modifications to `sanitizeHandInput()` preserve this mapping, as users expect `T` to input `10`.
* **Suit Insertion Buttons:**
  * Suit toolbar icons (`♠, ♥, ♦, ♣`) are styled with `transform: scale(2)` to accommodate mobile touch targets. Keep them large for responsiveness.
