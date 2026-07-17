import os
import json
import re
import shutil

local_path = r"C:\Users\Erdem\\.gemini\\antigravity\\scratch\\erdembridge-com"
config_path = os.path.join(local_path, "seo_metadata.json")
template_path = os.path.join(local_path, "index.html")

# Define helper to locate and parse json-ld block in html content
def extract_json_ld(html):
    # Regex to find ld+json block content
    match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1).strip()), match.group(0)
        except Exception as e:
            print(f"Warning parsing JSON-LD from template: {e}")
    return None, None

def build():
    # 1. Load config and template
    if not os.path.exists(config_path):
        print("Error: seo_metadata.json config file not found.")
        return False
    
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        
    if not os.path.exists(template_path):
        print("Error: index.html template file not found.")
        return False
        
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    base_url = config.get("site_base_url", "https://www.bricdersi.net")
    default_og_image = config.get("default_og_image", f"{base_url}/logo.png")
    pages = config.get("pages", [])
    
    original_schema, original_script_tag = extract_json_ld(template)
    
    generated_pages = []
    
    # 2. Iterate pages and generate static files
    for page in pages:
        route = page.get("route", "")
        title = page.get("title", "")
        description = page.get("description", "")
        breadcrumbs = page.get("breadcrumbs", [])
        has_faq = page.get("has_faq", False)
        
        # Determine target file path
        if route == "":
            # Root page is index.html
            target_dir = local_path
            target_file = os.path.join(target_dir, "index.html")
            page_url = base_url + "/"
        else:
            target_dir = os.path.join(local_path, route)
            target_file = os.path.join(target_dir, "index.html")
            page_url = f"{base_url}/{route}"
            
        # Create output directory
        if target_dir != local_path:
            os.makedirs(target_dir, exist_ok=True)
            
        page_html = template
        
        # Apply standard meta tag replacements
        # Canonical Link
        page_html = re.sub(
            r'<link rel="canonical" href="[^"]*">',
            f'<link rel="canonical" href="{page_url}">',
            page_html
        )
        # Meta Title & Description
        page_html = re.sub(
            r'<title>[^<]*</title>',
            f'<title>{title}</title>',
            page_html
        )
        page_html = re.sub(
            r'<meta name="description" content="[^"]*">',
            f'<meta name="description" content="{description}">',
            page_html
        )
        # Open Graph
        page_html = re.sub(
            r'<meta property="og:title" content="[^"]*">',
            f'<meta property="og:title" content="{title}">',
            page_html
        )
        page_html = re.sub(
            r'<meta property="og:description" content="[^"]*">',
            f'<meta property="og:description" content="{description}">',
            page_html
        )
        page_html = re.sub(
            r'<meta property="og:url" content="[^"]*">',
            f'<meta property="og:url" content="{page_url}">',
            page_html
        )
        # Twitter Cards
        page_html = re.sub(
            r'<meta name="twitter:title" content="[^"]*">',
            f'<meta name="twitter:title" content="{title}">',
            page_html
        )
        page_html = re.sub(
            r'<meta name="twitter:description" content="[^"]*">',
            f'<meta name="twitter:description" content="{description}">',
            page_html
        )
        
        # Modify the dynamic page load trigger in body onload or initial routing script
        # So that when a user loads a static subpage directly, client-side routing automatically switches to the correct tab.
        # We can inject a default tab handler variable on the window object:
        tab_id = route if route != "" else "anasayfa"
        page_html = page_html.replace(
            '<head>',
            f'<head>\n    <script>window.initialRouteTab = "{tab_id}";</script>'
        )

        # 3. Dynamic JSON-LD Schema Construction
        if original_schema and original_script_tag:
            # Deep copy original schema
            page_schema = json.loads(json.dumps(original_schema))
            
            # Filter and update graph elements
            new_graph = []
            for item in page_schema.get("@graph", []):
                item_type = item.get("@type")
                
                # Update basic URL fields to point to this page or base
                if "url" in item and item["url"] == base_url:
                    if item_type in ["Person", "Organization", "LocalBusiness"]:
                        item["url"] = base_url
                        
                # 1. Update BreadcrumbList for this specific route
                if item_type == "BreadcrumbList":
                    item["@id"] = f"{page_url}#breadcrumb"
                    item_list = []
                    for idx, bc in enumerate(breadcrumbs, 1):
                        item_list.append({
                            "@type": "ListItem",
                            "position": idx,
                            "name": bc["name"],
                            "item": f"{base_url}/{bc['item']}" if bc["item"] != "" else f"{base_url}/"
                        })
                    item["itemListElement"] = item_list
                    new_graph.append(item)
                    
                # 2. Update FAQPage if applicable
                elif item_type == "FAQPage":
                    if has_faq:
                        item["@id"] = f"{page_url}#faq"
                        new_graph.append(item)
                    # Skip FAQPage if the route does not declare has_faq
                else:
                    new_graph.append(item)
                    
            page_schema["@graph"] = new_graph
            
            # Serialize updated schema
            serialized_schema = json.dumps(page_schema, ensure_ascii=False, indent=2)
            new_script_tag = f'<script type="application/ld+json">\n{serialized_schema}\n</script>'
            page_html = page_html.replace(original_script_tag, new_script_tag)

        # Write generated HTML
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(page_html)
            
        generated_pages.append({
            "route": route,
            "url": page_url,
            "path": target_file,
            "size": os.path.getsize(target_file)
        })

    # 4. Generate sitemap.xml
    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for page in generated_pages:
        loc = page["url"]
        # Add change frequency and priorities
        if page["route"] == "":
            freq = "weekly"
            priority = "1.0"
        elif page["route"] in ["hakkimda", "dersler", "rehber", "sss", "iletisim"]:
            freq = "monthly"
            priority = "0.8"
        else:
            freq = "monthly"
            priority = "0.7"
        sitemap_lines.append(f'  <url><loc>{loc}</loc><changefreq>{freq}</changefreq><priority>{priority}</priority></url>')
    sitemap_lines.append('</urlset>')
    
    sitemap_content = "\n".join(sitemap_lines) + "\n"
    sitemap_out_path = os.path.join(local_path, "sitemap.xml")
    with open(sitemap_out_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("Sitemap generated successfully.")

    # 5. Generate robots.txt
    robots_content = f"User-agent: *\nAllow: /\n\nSitemap: {base_url}/sitemap.xml\n"
    robots_out_path = os.path.join(local_path, "robots.txt")
    with open(robots_out_path, "w", encoding="utf-8") as f:
        f.write(robots_content)
    print("robots.txt generated successfully.")

    # 6. Generate Validation Report
    report_lines = [
        "=== SSG Pipeline Build Validation Report ===",
        f"Base URL: {base_url}",
        f"Total Pages Generated: {len(generated_pages)}",
        ""
    ]
    for idx, pg in enumerate(generated_pages, 1):
        report_lines.append(f"{idx}. Route: '/{pg['route']}'")
        report_lines.append(f"   URL: {pg['url']}")
        report_lines.append(f"   Output File: {pg['path']}")
        report_lines.append(f"   File Size: {pg['size']} bytes")
        
        # Verify tag insertions by reading output file
        with open(pg['path'], "r", encoding="utf-8") as f:
            test_content = f.read()
        
        has_canonical = f'href="{pg["url"]}"' in test_content or f"href='{pg['url']}'" in test_content
        has_initial_tab = f'window.initialRouteTab = "{pg["route"] if pg["route"] != "" else "anasayfa"}"' in test_content
        
        report_lines.append(f"   Verification - Canonical Matches Host: {'PASS' if has_canonical else 'FAIL'}")
        report_lines.append(f"   Verification - Client-side Loader Injected: {'PASS' if has_initial_tab else 'FAIL'}")
        report_lines.append("")
        
    report_content = "\n".join(report_lines)
    report_out_path = os.path.join(local_path, "build_validation_report.txt")
    with open(report_out_path, "w", encoding="utf-8") as f:
        f.write(report_content)
    print("Validation report compiled.")
    
    return True

if __name__ == "__main__":
    success = build()
    if success:
        print("SSG Pipeline finished successfully!")
    else:
        print("SSG Pipeline build failed.")
