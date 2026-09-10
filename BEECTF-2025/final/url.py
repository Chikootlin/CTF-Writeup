import re
import sys

if len(sys.argv) < 2:
    print("Usage: python3 find_urls.py <memory_dump_file>")
    sys.exit(1)

infile = sys.argv[1]
outfile = "website.txt"

with open(infile, "rb") as f:
    b = f.read()

try:
    text = b.decode("utf-8", "ignore")
except Exception:
    text = b.decode("latin1", "ignore")

url_pattern = re.compile(r'https?://[A-Za-z0-9\-\._/~?&=%:\,\+]{10,300}', re.IGNORECASE)
urls = set(url_pattern.findall(text))

base64_pattern = re.compile(r'[A-Za-z0-9+/]{40,}={0,2}')
base64_tokens = set(base64_pattern.findall(text))

with open(outfile, "w", encoding="utf-8") as out:
    out.write("Extracted \n")
    if urls:
        for u in sorted(urls):
            out.write(u + "\n")
    else:
        out.write("(no URLs found)\n")

    out.write("\nBase64 Line Token \n")
    if base64_tokens:
        for t in sorted(base64_tokens):
            out.write("BASE64: " + t + "\n")
    else:
        out.write("(no long base64 tokens found)\n")

print(f"Done. {outfile}")
print(f"URLs found: {len(urls)}, BASE64 tokens found: {len(base64_tokens)}")