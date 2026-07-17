# SEO Handover Report: bricdersi.net & erdembridge.com

This report summarizes the technical SEO modifications, the implementation of the Static Site Generation (SSG) pipeline, and the long-term strategic recommendations designed to prepare these codebases for future development sessions.

---

## 1. Technical Audit Summary & Solved Issues

Before modifications, a full enterprise-level SEO audit revealed critical performance and indexing roadblocks:
*   **Domain Canonical Conflict:** Canonical link elements, Open Graph headers, JSON-LD schemas, and sitemap destinations in the codebase were pointing to `erdembridge.com`, while files were actively deployed to `bricdersi.net`. This caused Google's search algorithms to de-index or deprioritize page rankings due to duplication.
*   **SPA Client-Side Hash Routing (`#`):** Guide links transitioned pages using hashes. Crawlers (Googlebot, Bingbot) cannot crawl dynamic client-side tab switching routes efficiently, leaving deep educational content unindexed.

### Changes Implemented:
1.  **Domain Migration:** Aligned all canonical targets, Open Graph social links, sitemap nodes, and schema graph URLs in the core code blocks to point to the production host `https://www.bricdersi.net/`.
2.  **Hydrated Routing:** Shifted navigation from hash URLs (`#bric-nedir`) to clean path URLs (`/bric-nedir`). Binded `popstate` events to preserve browser back/forward history transitions.

---

## 2. Static Site Generation (SSG) Engine Architecture

To resolve crawler indexability while retaining the single-page application (SPA) design, we developed a build-time compile pipeline:

```
                  ┌───────────────────────┐
                  │   seo_metadata.json   │
                  └───────────+───────────┘
                              │ (Reads metadata config)
                              ▼
┌──────────────┐   ┌───────────────────────┐   ┌───────────────────────┐
│  index.html  ├──>│    build_pages.py     ├──>│ /hakkimda/index.html   │
│  (Template)  │   │  (Python SSG Engine)  │   │ /rehber/index.html    │
└──────────────┘   └───────────+───────────┘   │ (Injected Subpages)   │
                               │               └───────────────────────┘
                               ▼
                  ┌───────────────────────┐
                  │ sitemap.xml & robots  │
                  └───────────────────────┘
```

*   **Template Source (`index.html`):** The absolute single source of truth for design, styles, and logic.
*   **Metadata Matrix (`seo_metadata.json`):** Centralizes route definitions, custom titles, search description tags, dynamically constructed breadcrumbs, and FAQ structured data markup.
*   **SSG Builder (`build_pages.py`):** Runs locally or on CI/CD pipelines to output search-engine-readable static files into subdirectories (e.g. `/dersler/index.html`).
*   **Client Bridge Loader:** Injects `window.initialRouteTab` into subpages to instruct the SPA router which tab to activate automatically during direct entry page loads.
*   **Validation Pipeline:** Automatically compiles `build_validation_report.txt` testing host matches and loader presence on all generated routes (12/12 routes currently pass).

---

## 3. Revised Long-Term SEO Strategy Summary

The multi-site roadmap (`LONG_TERM_SEO_STRATEGY.md`) divides brand positioning to avoid search cannibalization:

*   **`bricdersi.net`:** Turkey's premier educational portal focusing on informational keyword intent ("briç nasıl oynanır", "briç puan hesaplama").
*   **`erdembridge.com`:** Personal authority brand focusing on transactional & editorial intent ("Özel briç dersi", "milli takım antrenörü").

### Key Structural Rules Added:
*   **Google-Compliant Schemas:** Restricts `Course` schema strictly to purchasable classes, `HowTo` to procedural tutorials (e.g. BBO setup), and uses compliant `LocalBusiness` reviews.
*   **Internal Link Rules:** Mandatory cluster-to-pillar link pairings, a minimum of 3 outgoing internal links for new articles, and natural cross-domain links.
*   **EEAT Experience Indicators:** Highlighting university records (attended ODTÜ) and certified TBF credentials on biography nodes.
*   **Content Pruning:** Emphasizes improving and merging thin pages before considering removal.

---

## 4. Git Deployment Logs

*   **Repository:** `https://github.com/brdg2020/erdembridge-com`
*   **Latest Commit Hash:** `e7b375b971e9b7a67544e5f9f53d8d2dd9dca5a9`
*   **Latest Commit Message:** `docs: refine SEO strategy with intent mapping table, internal linking rules and verified credentials`
