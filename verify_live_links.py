import requests
from bs4 import BeautifulSoup
import urllib.parse

base_url = "https://app.sphynxplay.com"
links_to_test = [
    "/",
    "/browse",
    "/faq",
    "/privacy",
    "/terms",
    "/soul-token-terms",
    "/content-policy",
    "/support",
    "/admin/login",
    "/delete-account"
]

results = []
for path in links_to_test:
    url = urllib.parse.urljoin(base_url, path)
    try:
        # Use a real user agent to avoid bot detection if any
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        res = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        results.append((res.status_code, url))
    except Exception as e:
        results.append((f"ERR: {str(e)}", url))

for status, url in results:
    print(f"{status} - {url}")
