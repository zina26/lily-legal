#!/usr/bin/env python3
"""Build the terms page from Markdown using the existing privacy page style.

Only the paragraph, H1/H2, bold, and link syntax used by this document is
supported. Unsupported block syntax fails instead of silently losing content.
"""
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parent.parent


def inline(value):
    pattern = r'\[([^\]]+)\]\(([^)]+)\)|\*\*(.+?)\*\*'
    parts = []
    end = 0
    for match in re.finditer(pattern, value):
        parts.append(html.escape(value[end:match.start()]))
        label, url, bold = match.groups()
        if url is not None:
            if not url.startswith(('https://', 'mailto:')):
                raise ValueError(f'Unsupported link: {url}')
            parts.append(f'<a href="{html.escape(url, quote=True)}">{html.escape(label)}</a>')
        else:
            parts.append(f'<strong>{html.escape(bold)}</strong>')
        end = match.end()
    parts.append(html.escape(value[end:]))
    return ''.join(parts)


def build():
    source = (ROOT / 'terms-of-service.md').read_text()
    blocks = source.strip().split('\n\n')
    assert blocks[0] == '# Lily Terms of Service'
    date = blocks[1]
    assert date.startswith('Effective date: ')
    toc, body = [], []
    section_open = False
    for block in blocks[2:]:
        if block.startswith('## '):
            match = re.fullmatch(r'## (\d+)\. (.+)', block)
            if not match:
                raise ValueError(f'Unsupported heading: {block}')
            number, title = match.groups()
            if int(number) != len(toc) + 1:
                raise ValueError('Section numbering is not sequential')
            if section_open:
                body.append('</section>')
            body.append(f'<section id="s{number}"><h2>{inline(block[3:])}</h2>')
            toc.append(f'<li><a href="#s{number}">{html.escape(title)}</a></li>')
            section_open = True
        else:
            if re.search(r'(?m)^(#|[-*] |\d+\. |```|>)', block):
                raise ValueError(f'Unsupported block: {block}')
            body.append(f'<p>{inline(block)}</p>')
    if section_open:
        body.append('</section>')
    assert len(toc) == 16
    privacy = (ROOT / 'privacy.html').read_text()
    css = re.search(r'<style>(.*?)</style>', privacy, re.S).group(1)
    extra_css = '''
  a:focus-visible { outline: 2px solid var(--accent); outline-offset: 4px; }
  p, a { overflow-wrap: anywhere; }
  @media (max-width: 560px) {
    .wrap { padding: 32px 20px 64px; }
  }
'''
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Lily Terms of Service: personal reflection, AI limitations, your content, subscriptions, and your rights.">
<title>Lily — Terms of Service</title>
<style>{css}{extra_css}</style>
</head>
<body>
<div class="wrap">
<header><h1>Lily Terms of Service</h1><p class="updated">{html.escape(date)}</p></header>
<main id="content" tabindex="-1">
{chr(10).join(body)}
</main>
</div>
</body>
</html>
'''
    (ROOT / 'terms.html').write_text(page)


if __name__ == '__main__':
    build()
