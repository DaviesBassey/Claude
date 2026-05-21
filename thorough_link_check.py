import requests
from bs4 import BeautifulSoup
import urllib.parse

base_url = "https://app.sphynxplay.com"
try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(base_url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    unique_links = set()
    for link in links:
        href = link.get('href')
        if href:
            full_url = urllib.parse.urljoin(base_url, href)
            unique_links.add(full_url)

    print(f"Found {len(unique_links)} unique links. Testing...")

    for url in sorted(unique_links):
        if url.startswith('mailto:'):
            print(f"SKIP - {url}")
            continue
        try:
            # Use GET to be sure, some servers block HEAD
            res = requests.get(url, headers=headers, timeout=5, allow_redirects=True)
            print(f"{res.status_code} - {url}")
        except Exception as e:
            print(f"ERR - {url}: {e}")
except Exception as e:
    print(f"Could not reach base URL: {e}")
