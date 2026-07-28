import os
import json
import re

local_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(local_path, "seo_metadata.json")
template_path = os.path.join(local_path, "index.html")

def build():
    if not os.path.exists(config_path) or not os.path.exists(template_path):
        print("Error: Config or template file missing.")
        return False

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    base_url = "https://www.erdembridge.com"
    pages = config.get("pages", [])

    for page in pages:
        route = page.get("route", "")
        if route == "":
            target_file = os.path.join(local_path, "index.html")
            page_url = base_url + "/"
        else:
            target_dir = os.path.join(local_path, route)
            os.makedirs(target_dir, exist_ok=True)
            target_file = os.path.join(target_dir, "index.html")
            page_url = f"{base_url}/{route}"

        page_html = template
        if page.get("title"):
            page_html = re.sub(r'<title>.*?</title>', f'<title>{page["title"]}</title>', page_html)
        if page.get("description"):
            page_html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{page["description"]}">', page_html)
        
        # Replace Canonical and OG URLs to erdembridge.com
        page_html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{page_url}">', page_html)
        page_html = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{page_url}">', page_html)

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(page_html)

    print("SSG Build finished successfully for erdembridge.com!")
    return True

if __name__ == "__main__":
    build()
