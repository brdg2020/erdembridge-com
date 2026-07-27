import os
import re
import json

SITE_ROOT = r"C:\Users\Erdem\.gemini\antigravity\scratch\erdembridge-com"

# 13 Key Personal Brand & High-Intent Page Definitions for erdembridge.com
PAGES_META = {
    "anasayfa": {
        "slug": "",
        "dir": "",
        "title": "Erdem Öztürk | Türkiye Briç Milli Takım Antrenörü & Kaptanı (Resmi Web Sitesi)",
        "description": "Türkiye Briç Milli Takım Antrenörü ve Kaptanı Erdem Öztürk'ün resmi kişisel web sitesi. TBF 3. Kademe antrenör ile İstanbul Beşiktaş Levent ve BBO online özel briç dersleri.",
        "type": "profile"
    },
    "hakkimda": {
        "slug": "hakkimda",
        "dir": "hakkimda",
        "title": "Erdem Öztürk Kimdir? Antrenörlük Kariyeri & Biyografi | erdembridge.com",
        "description": "Türkiye Briç Milli Takım Antrenörü ve Kaptanı, TBF 3. Kademe Kıdemli Antrenör Erdem Öztürk'ün biyografisi, ODTÜ geçmişi, antrenörlük felsefesi ve başarıları.",
        "type": "profile"
    },
    "ozgecmis-ve-kariyer": {
        "slug": "ozgecmis-ve-kariyer",
        "dir": "ozgecmis-ve-kariyer",
        "title": "Erdem Öztürk Özgeçmiş & Spor Kariyeri | erdembridge.com",
        "description": "Erdem Öztürk'ün 2002'den bu yana aktif briç sporculuğu, 2009'dan itibaren profesyonel antrenörlük kariyeri, lisansları ve akademik özgeçmişi.",
        "type": "article"
    },
    "milli-takim-kariyeri": {
        "slug": "milli-takim-kariyeri",
        "dir": "milli-takim-kariyeri",
        "title": "Türkiye Briç Milli Takımı Kariyeri & Kaptanlık | Erdem Öztürk",
        "description": "Erdem Öztürk'ün Türkiye Briç Milli Takım Kaptanlığı, antrenörlük görevleri, uluslararası şampiyonalar ve milli takım vizyonu.",
        "type": "article"
    },
    "turnuvalar-ve-basarilar": {
        "slug": "turnuvalar-ve-basarilar",
        "dir": "turnuvalar-ve-basarilar",
        "title": "Turnuva Başarıları, Dereceler & Master Puanları | Erdem Öztürk",
        "description": "Erdem Öztürk'ün ulusal ve uluslararası briç turnuvalarındaki şampiyonlukları, kupaları ve TBF master puan dereceleri.",
        "type": "article"
    },
    "basinda-biz": {
        "slug": "basinda-biz",
        "dir": "basinda-biz",
        "title": "Basında Erdem Öztürk | Medya Haberleri & Röportajlar",
        "description": "Erdem Öztürk hakkında basında çıkan haberler, gazete ve TV röportajları, briç sporu üzerine makaleler ve medya yansımaları.",
        "type": "article"
    },
    "referanslar": {
        "slug": "referanslar",
        "dir": "referanslar",
        "title": "Öğrenci Yorumları & Kulüp Referansları | Erdem Öztürk Briç Dersleri",
        "description": "Erdem Öztürk'ten özel briç dersi ve koçluk alan öğrencilerin görüşleri, başarı hikayeleri ve kulüp referansları.",
        "type": "article"
    },
    "ozel-bric-dersleri": {
        "slug": "ozel-bric-dersleri",
        "dir": "ozel-bric-dersleri",
        "title": "Özel Briç Dersleri & Birebir Koçluk | Erdem Öztürk",
        "description": "Milli Takım Antrenörü Erdem Öztürk ile birebir özel briç dersleri ve özel grup koçluğu. İstanbul Beşiktaş Levent ve Zoom/BBO seçenekleri.",
        "type": "course"
    },
    "istanbul-bric-dersi": {
        "slug": "istanbul-bric-dersi",
        "dir": "istanbul-bric-dersi",
        "title": "İstanbul Beşiktaş Levent Briç Dersleri | Erdem Öztürk",
        "description": "İstanbul Beşiktaş Levent Tenis Kulübü'nde Milli Takım Antrenörü Erdem Öztürk ile yüz yüze özel briç dersleri ve kulüp pratikleri.",
        "type": "course"
    },
    "online-bric-koclugu": {
        "slug": "online-bric-koclugu",
        "dir": "online-bric-koclugu",
        "title": "Online BBO Briç Koçluğu & Canlı Masa Analizi | Erdem Öztürk",
        "description": "Bridge Base Online (BBO) üzerinden Milli Takım Antrenörü Erdem Öztürk rehberliğinde canlı masa koçluğu, el analizi ve online özel ders.",
        "type": "course"
    },
    "ileri-seviye-bric-ve-makaleler": {
        "slug": "ileri-seviye-bric-ve-makaleler",
        "dir": "ileri-seviye-bric-ve-makaleler",
        "title": "İleri Seviye Briç Analizleri & Makaleler | Erdem Öztürk",
        "description": "Turnuva oyuncuları için ileri seviye briç teknikleri, oyun planı analizleri, savunma stratejileri ve Erdem Öztürk imzalı briç makaleleri.",
        "type": "article"
    },
    "birebir-bric-kursu": {
        "slug": "birebir-bric-kursu",
        "dir": "birebir-bric-kursu",
        "title": "Birebir Briç Kursu & VIP Antrenörlük Programı | Erdem Öztürk",
        "description": "Milli Takım Antrenörü Erdem Öztürk ile kişiselleştirilmiş birebir briç kursu ve VIP turnuva koçluğu. İstanbul Levent ve BBO online canlı dersler.",
        "type": "course"
    },
    "sss": {
        "slug": "sss",
        "dir": "sss",
        "title": "Özel Dersi & Koçluk S.S.S. | Erdem Öztürk",
        "description": "Özel briç dersi ücretleri, ders süreleri, Beşiktaş Levent lokasyonu ve BBO online koçluk kayıt soruları.",
        "type": "faq"
    },
    "iletisim": {
        "slug": "iletisim",
        "dir": "iletisim",
        "title": "İletişim & Özel Ders Başvurusu | Erdem Öztürk",
        "description": "Milli Takım Antrenörü Erdem Öztürk ile iletişime geçin. İstanbul Levent yüz yüze ders veya BBO online koçluk başvurusu için WhatsApp ve iletişim formu.",
        "type": "contact"
    }
}

def clean_html_template(content):
    # Ensure all canonical and schema references point strictly to erdembridge.com
    content = content.replace("https://www.bricdersi.net/", "https://www.erdembridge.com/")
    content = content.replace("https://www.bricdersi.net", "https://www.erdembridge.com")
    content = content.replace("https://bricdersi.net", "https://www.erdembridge.com")
    content = content.replace("bricdersi.net", "erdembridge.com")

    # Clean up duplicated script tags
    content = re.sub(r'(\s*<script>window\.initialRouteTab\s*=\s*"[^"]*";</script>)+', '\n    <script>window.initialRouteTab = "__ROUTE__";</script>', content)

    return content

def build_schema_json(slug, page_meta):
    url = f"https://www.erdembridge.com/{slug}" if slug else "https://www.erdembridge.com/"
    
    graph = [
        {
            "@type": "Person",
            "@id": "https://www.erdembridge.com/#person",
            "name": "Erdem Öztürk",
            "jobTitle": "Türkiye Briç Milli Takım Antrenörü & Kaptanı (TBF 3. Kademe Antrenör)",
            "description": "2002'den bu yana aktif briç sporcusu, 2009'dan itibaren profesyonel briç eğitmeni. Türkiye Briç Milli Takım Antrenörü ve Kaptanı. ODTÜ mezunu.",
            "url": "https://www.erdembridge.com",
            "image": "https://www.erdembridge.com/favicon-32x32.png",
            "telephone": "+905368533284",
            "email": "bricogren@gmail.com",
            "sameAs": [
                "https://www.erdembridge.com",
                "https://www.instagram.com/bric.dersi",
                "https://www.youtube.com/channel/UCPvnp7T9eOpixvbIA4olNYQ",
                "https://www.udemy.com/course/bric-dersi/?referralCode=39CF07889CA4DDF887DF",
                "https://apps.apple.com/tr/app/bridge-begin/id1241733213"
            ],
            "knowsAbout": [
                "Briç",
                "Briç Eğitimi",
                "Milli Takım Briç Antrenörlüğü",
                "Turnuva Briçi",
                "İleri Seviye Konvansiyonlar"
            ],
            "alumniOf": {
                "@type": "CollegeOrUniversity",
                "name": "ODTÜ"
            },
            "award": "TBF 3. Kademe Lisanslı Briç Antrenörü & Türkiye Milli Takım Kaptanı"
        },
        {
            "@type": "LocalBusiness",
            "@id": "https://www.erdembridge.com/#business",
            "name": "Erdem Öztürk Özel Briç Dersleri & Koçluk",
            "url": "https://www.erdembridge.com",
            "image": "https://www.erdembridge.com/favicon-32x32.png",
            "telephone": "+905368533284",
            "email": "bricogren@gmail.com",
            "priceRange": "$$",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Levent Tenis Kulübü, Levent",
                "addressLocality": "Beşiktaş",
                "addressRegion": "İstanbul",
                "postalCode": "34330",
                "addressCountry": "TR"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 41.0825,
                "longitude": 29.0158
            },
            "sameAs": [
                "https://www.instagram.com/bric.dersi",
                "https://www.youtube.com/channel/UCPvnp7T9eOpixvbIA4olNYQ"
            ]
        },
        {
            "@type": "WebSite",
            "@id": "https://www.erdembridge.com/#website",
            "url": "https://www.erdembridge.com/",
            "name": "Erdem Öztürk - Resmi Web Sitesi",
            "description": "Türkiye Briç Milli Takım Antrenörü Erdem Öztürk Resmi Web Sitesi ve Özel Dersi Portalı",
            "publisher": {"@id": "https://www.erdembridge.com/#person"}
        }
    ]

    if slug:
        graph.append({
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumb",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Ana Sayfa",
                    "item": "https://www.erdembridge.com/"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": page_meta["title"].split("|")[0].strip(),
                    "item": url
                }
            ]
        })

    if page_meta["type"] == "article":
        graph.append({
            "@type": "Article",
            "@id": f"{url}#article",
            "isPartOf": {"@id": "https://www.erdembridge.com/#website"},
            "author": {"@id": "https://www.erdembridge.com/#person"},
            "headline": page_meta["title"],
            "description": page_meta["description"],
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "publisher": {"@id": "https://www.erdembridge.com/#person"},
            "inLanguage": "tr",
            "datePublished": "2024-01-01",
            "dateModified": "2026-07-26"
        })
    elif page_meta["type"] == "course":
        graph.append({
            "@type": "Course",
            "@id": f"{url}#course",
            "name": page_meta["title"],
            "description": page_meta["description"],
            "url": url,
            "provider": {"@id": "https://www.erdembridge.com/#business"},
            "instructor": {"@id": "https://www.erdembridge.com/#person"},
            "inLanguage": "tr"
        })

    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)

def main():
    print("Building master erdembridge.com personal authority platform...")

    base_index_path = os.path.join(SITE_ROOT, "index.html")
    with open(base_index_path, "r", encoding="utf-8") as f:
        base_html = f.read()

    base_html = clean_html_template(base_html)

    # Write cleaned root index.html
    root_html = base_html.replace('__ROUTE__', 'anasayfa')
    with open(base_index_path, "w", encoding="utf-8") as f:
        f.write(root_html)

    print("Root index.html cleaned and updated for erdembridge.com.")

    # Generate physical subfolder pages
    for key, meta in PAGES_META.items():
        if key == "anasayfa":
            continue

        slug = meta["slug"]
        dir_name = meta["dir"]
        page_dir = os.path.join(SITE_ROOT, dir_name)
        os.makedirs(page_dir, exist_ok=True)

        target_file = os.path.join(page_dir, "index.html")

        page_html = base_html.replace('__ROUTE__', slug)

        # Replace title tag
        page_html = re.sub(r'<title>.*?</title>', f'<title>{meta["title"]}</title>', page_html, flags=re.DOTALL)
        
        # Replace meta description
        page_html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{meta["description"]}">', page_html, flags=re.DOTALL)

        # Replace canonical link
        canonical_url = f"https://www.erdembridge.com/{slug}"
        page_html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{canonical_url}">', page_html, flags=re.DOTALL)

        # Replace OpenGraph & Twitter meta tags
        page_html = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{canonical_url}">', page_html, flags=re.DOTALL)
        page_html = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{meta["title"]}">', page_html, flags=re.DOTALL)
        page_html = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{meta["description"]}">', page_html, flags=re.DOTALL)

        page_html = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{meta["title"]}">', page_html, flags=re.DOTALL)
        page_html = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{meta["description"]}">', page_html, flags=re.DOTALL)

        # Inject JSON-LD Schema
        schema_json = build_schema_json(slug, meta)
        schema_script = f'<script type="application/ld+json">\n{schema_json}\n</script>'
        page_html = re.sub(r'<script type="application/ld\+json">.*?</script>', schema_script, page_html, flags=re.DOTALL)

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(page_html)

        print(f"Generated physical SEO page: /{slug}")

    # Generate sitemap.xml
    sitemap_entries = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for key, meta in PAGES_META.items():
        slug = meta["slug"]
        url = f"https://www.erdembridge.com/{slug}" if slug else "https://www.erdembridge.com/"
        priority = "1.0" if not slug else ("0.9" if "ders" in slug or "hakkimda" in slug else "0.8")
        sitemap_entries.append(f"  <url>\n    <loc>{url}</loc>\n    <lastmod>2026-07-26</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{priority}</priority>\n  </url>")

    sitemap_entries.append('</urlset>')
    sitemap_path = os.path.join(SITE_ROOT, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_entries))

    print("sitemap.xml updated with all 13 canonical erdembridge.com URLs.")

    # Generate robots.txt
    robots_content = "User-agent: *\nAllow: /\n\nSitemap: https://www.erdembridge.com/sitemap.xml\n"
    robots_path = os.path.join(SITE_ROOT, "robots.txt")
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(robots_content)

    print("robots.txt updated.")

    # Update firebase.json with correct site name
    firebase_config = {
        "hosting": {
            "site": "erdembridge-com",
            "public": ".",
            "ignore": [
                "firebase.json",
                "**/.*",
                "**/node_modules/**"
            ],
            "headers": [
                {
                    "source": "/pdf/**",
                    "headers": [
                        {"key": "Cache-Control", "value": "no-cache, no-store, must-revalidate"}
                    ]
                }
            ],
            "redirects": [
                {"source": "/briç-malzemeleri", "destination": "/hakkimda", "type": 301},
                {"source": "/bri%C3%A7-malzemeleri", "destination": "/hakkimda", "type": 301},
                {"source": "/bric-kursu", "destination": "/birebir-bric-kursu", "type": 301},
                {"source": "/anasayfa", "destination": "/", "type": 301}
            ],
            "cleanUrls": True,
            "trailingSlash": False
        }
    }

    firebase_path = os.path.join(SITE_ROOT, "firebase.json")
    with open(firebase_path, "w", encoding="utf-8") as f:
        json.dump(firebase_config, f, indent=2, ensure_ascii=False)

    print("firebase.json updated with target 'erdembridge-com' and 301 redirects.")

if __name__ == "__main__":
    main()
