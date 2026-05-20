import re
import requests

def get_links(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return re.findall(r'https?://[a-zA-Z0-9./_-]+', content)

files = ['/tmp/sphynx-motion/index.html', '/tmp/sphynx-motion/server/routes/legal.js']
all_links = set()
for f in files:
    all_links.update(get_links(f))

for link in sorted(all_links):
    if any(x in link for x in ['fonts.', 'jsdelivr', 'justice.gov', 'apple.com', 'google.com']):
        continue
    try:
        # Check if they are at least resolvable or returning 200/404
        res = requests.head(link, timeout=5, allow_redirects=True)
        print(f"{res.status_code} - {link}")
    except Exception as e:
        print(f"ERR - {link}: {e}")
