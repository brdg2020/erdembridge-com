# GSC Coverage Report: Prioritized Action Plan

This document outlines the prioritized action plan designed to resolve the crawl and indexing anomalies discovered in the Google Search Console (GSC) export files for **bricdersi.net** and **erdembridge.com**.

---

## 1. Issue Classification & Analysis

We classify the detected GSC Coverage report issues based on their immediate impact on search ranking and visibility.

### Issue A: Duplicate, Google chose different canonical than user
*   **Classification:** **Fix immediately**
*   **Why it happens:** Both sites served identical HTML/JavaScript content under two different domains (`erdembridge.com` and `bricdersi.net`). Google's duplicate detection algorithm chose one domain as canonical and excluded the other's equivalent pages, suppressing search visibility.
*   **Solved by SSG implementation?** **Yes.** The SSG pipeline writes distinct canonical elements mapping strictly to their respective home host domains in `index.html`.
*   **Manual action required?** **Yes (Verification Trigger).** Request validation in Google Search Console under the specific indexing issue panel for both domains.
*   **Expected recovery timeline:** 2 to 4 weeks (depending on Googlebot recrawl speed).

---

### Issue B: Crawled - currently not indexed
*   **Classification:** **Fix immediately**
*   **Why it happens:** Googlebot fetched the page URLs but did not index them. This was primarily caused by:
    1.  The client-side hash routing (`#`) rendering an empty/thin template shell if JavaScript execution timed out during crawling.
    2.  Content duplication between the sister domains.
*   **Solved by SSG implementation?** **Yes.** Pre-rendering HTML pages statically removes template timeout risks. Distinct canonical headers resolve the duplication.
*   **Manual action required?** **No.** Google will naturally update these indices on its next crawl sweep.
*   **Expected recovery timeline:** 2 to 3 weeks.

---

### Issue C: Discovered - currently not indexed
*   **Classification:** **Monitor**
*   **Why it happens:** Google has discovered the URLs (mostly through sitemap paths or backlinks) but has not yet crawled them due to crawl budget constraints or duplication priority flags.
*   **Solved by SSG implementation?** **Yes.** The newly generated sitemaps contain only clean, unique HTML paths with updated priorities, signaling higher quality and prompting Googlebot to prioritize crawling.
*   **Manual action required?** **No.**
*   **Expected recovery timeline:** 1 to 2 weeks after submitting the updated `sitemap.xml`.

---

### Issue D: Not found (404)
*   **Classification:** **Monitor**
*   **Why it happens:** Legacy paths (like `/briç-malzemeleri`) or dynamic test pages no longer exist in the active codebase directory.
*   **Solved by SSG implementation?** **Indirectly.** The new sitemaps exclude these dead paths, which prevents Google from wasting crawl resources on them.
*   **Manual action required?** **Yes (Redirects mapping).** If these paths have legacy backlinks or search traffic, we must set up 301 redirects in `firebase.json` mapping them to the closest active path (e.g. `/rehber`).
*   **Expected recovery timeline:** 4 to 8 weeks for Google to drop dead 404 paths from index records.

---

### Issue E: Page with redirect
*   **Classification:** **Ignore (Expected Behavior)**
*   **Why it happens:** Legacy hash paths are redirected to clean routes, or `http://` requests are redirected to `https://`.
*   **Solved by SSG implementation?** **Yes.** This is expected behavior and confirms redirect logic is functioning.
*   **Manual action required?** **No.**
*   **Expected recovery timeline:** Immediate (no action needed).

---

### Issue F: Alternate page with proper canonical tag
*   **Classification:** **Ignore (Expected Behavior)**
*   **Why it happens:** Mobile URLs, tracking parameters, or trailing slashes point to the primary canonical URL. Google indexes only the canonical version.
*   **Solved by SSG implementation?** **Yes.** Confirms canonical declarations are functioning correctly.
*   **Manual action required?** **No.**
*   **Expected recovery timeline:** N/A.

---

## 2. Prioritized Action Table (Ordered by SEO Impact)

| Priority | Issue | Classification | Impact | Manual Action Required |
|:---:|:---|:---|:---:|:---|
| **1** | Duplicate, Google chose different canonical than user | **Fix immediately** | **Critical** (Domain split block) | **Yes** - Trigger "Validate Fix" in GSC |
| **2** | Crawled - currently not indexed | **Fix immediately** | **High** (Missing index content) | **No** - Resolved via static pre-rendering |
| **3** | Discovered - currently not indexed | **Monitor** | **Medium** (Index queue backlog) | **No** - Re-submit new `sitemap.xml` |
| **4** | Not found (404) | **Monitor** | **Low-Medium** (Crawl budget leak) | **Yes** - Setup redirects in `firebase.json` for traffic URLs |
| **5** | Page with redirect / Alternate canonical | **Ignore** | **None** (Clean states) | **No** - Expected behavior |
