import re

with open("f:/placement/1round ready2/index.html", "r", encoding="utf-8") as f:
    html = f.read()

ids_in_html = set(re.findall(r'id=["\']([a-zA-Z0-9_-]+)["\']', html))
ids_in_js = set(re.findall(r"\$\(['\"]#([a-zA-Z0-9_-]+)['\"]\)", html))

print(f"Total IDs defined statically in HTML: {len(ids_in_html)}")
print(f"Total IDs queried in JS via $('#id'): {len(ids_in_js)}")

missing = [jid for jid in ids_in_js if jid not in ids_in_html]
print(f"IDs queried that are dynamically populated in JS template literals: {missing}")
