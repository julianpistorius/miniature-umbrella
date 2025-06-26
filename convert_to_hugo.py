import os, re, pathlib

root = pathlib.Path('.')
site_content = root / 'site' / 'content'

html_files = [p for p in root.rglob('*.html') if 'site' not in p.parts and '.git' not in p.parts]

header_re = re.compile(r'(?s)^(.*?<header id="header">.*?</header>)(.*)$')
main_re = re.compile(r'(?s)(<main.*?</main>)')
title_re = re.compile(r'<title>(.*?)</title>', re.S)

for p in html_files:
    text = p.read_text()
    # extract title
    m = title_re.search(text)
    title = m.group(1).strip() if m else p.stem
    # extract main
    m = header_re.search(text)
    if not m:
        continue
    rest = m.group(2)
    m2 = main_re.search(rest)
    if not m2:
        continue
    main = m2.group(1).strip()
    # Determine destination path
    rel = p.relative_to(root)
    if rel.name == 'index.html':
        dest = site_content / rel.parent / '_index.md'
    else:
        dest = site_content / rel.with_suffix('.md')
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(f"---\ntitle: '{title}'\n---\n\n" + main)
print('Converted', len(html_files), 'files')
