#!/usr/bin/env python3
import sys
import pathlib
import markdown
from weasyprint import HTML, CSS

src = pathlib.Path(sys.argv[1])
dst = pathlib.Path(sys.argv[2])

md_text = src.read_text(encoding="utf-8")
html_body = markdown.markdown(
    md_text,
    extensions=["tables", "fenced_code", "sane_lists"],
)

css = """
@page {
  size: A4;
  margin: 18mm 16mm 20mm 16mm;
  @bottom-center {
    content: "Finece — Confidential analyst work product  •  page " counter(page) " / " counter(pages);
    font-size: 8pt;
    color: #666;
    font-family: "Noto Sans CJK TC", "WenQuanYi Zen Hei", sans-serif;
  }
}
html { font-size: 10pt; }
body {
  font-family: "Noto Sans CJK TC", "Noto Serif CJK TC", "WenQuanYi Zen Hei", sans-serif;
  color: #1a1a1a;
  line-height: 1.45;
}
h1 {
  font-size: 18pt;
  border-bottom: 2px solid #0b3d91;
  color: #0b3d91;
  padding-bottom: 4pt;
  margin: 0 0 6pt 0;
}
h2 {
  font-size: 12pt;
  color: #0b3d91;
  margin: 14pt 0 4pt 0;
  border-bottom: 1px solid #cccccc;
  padding-bottom: 2pt;
}
h3 { font-size: 11pt; margin: 10pt 0 4pt 0; }
strong { color: #0b3d91; }
blockquote {
  background: #f4f6fb;
  border-left: 3px solid #0b3d91;
  margin: 6pt 0;
  padding: 6pt 10pt;
  font-size: 9.5pt;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 6pt 0;
  font-size: 9pt;
}
th, td {
  border: 1px solid #cccccc;
  padding: 4pt 6pt;
  vertical-align: top;
  text-align: left;
}
th {
  background: #eef2f9;
  color: #0b3d91;
}
tr:nth-child(even) td { background: #fafbfd; }
hr { border: none; border-top: 1px solid #cccccc; margin: 10pt 0; }
ol, ul { padding-left: 18pt; }
li { margin: 2pt 0; }
code {
  background: #f4f4f4;
  padding: 1pt 3pt;
  border-radius: 2pt;
  font-family: "DejaVu Sans Mono", monospace;
  font-size: 9pt;
}
.cover-meta {
  font-size: 9pt;
  color: #555;
  margin-top: -2pt;
}
"""

html_doc = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head><meta charset="utf-8"><title>5274 Quick Take</title></head>
<body>{html_body}</body>
</html>"""

HTML(string=html_doc).write_pdf(
    str(dst),
    stylesheets=[CSS(string=css)],
    optimize_size=(),
)
print(f"Wrote {dst}")
