"""Export generated monthly Markdown reports to PDFs with Chinese fonts."""
import argparse
import json
from pathlib import Path
import tempfile
from markdown_it import MarkdownIt
from playwright.sync_api import sync_playwright

STYLE = '''@page { size: A4; margin: 18mm 15mm 20mm; }
body { font-family: "Noto Sans CJK SC", "PingFang SC", sans-serif; font-size: 10pt; line-height: 1.65; color: #253247; }
h1 { font-size: 23pt; color: #12365b; } h2 { font-size: 16pt; border-bottom: 1px solid #bccbd9; padding-bottom: 5px; }
h3 { font-size: 12pt; } h1,h2,h3,h4 { break-after: avoid; }
table { border-collapse: collapse; width: 100%; font-size: 8pt; table-layout: fixed; }
th,td { border: 1px solid #cdd6df; padding: 5px; overflow-wrap: anywhere; }
th { background: #eaf0f6; } thead { display: table-header-group; }
tr { break-inside: avoid; } a { color: #185b98; overflow-wrap: anywhere; }
blockquote { border-left: 3px solid #4284ad; margin-left: 0; padding-left: 12px; }
pre,code { white-space: pre-wrap; overflow-wrap: anywhere; } img { max-width: 100%; }
'''


def export(directory):
    directory = Path(directory).resolve()
    sources = sorted(directory.glob('report*.md'))
    if len(sources) != 3:
        raise ValueError('必须存在三份 Markdown 报告')
    markdown = MarkdownIt('commonmark', {'html': False}).enable('table')
    with tempfile.TemporaryDirectory() as temporary, sync_playwright() as runner:
        browser = runner.chromium.launch()
        page = browser.new_page()
        # Report content cannot execute scripts or load external resources.
        page.route('**/*', lambda route: route.abort())
        for source in sources:
            page.set_content('<!doctype html><html lang="zh-CN"><meta charset="utf-8">'
                             f'<style>{STYLE}</style><body>{markdown.render(source.read_text())}</body></html>')
            page.evaluate('document.fonts.ready')
            target = Path(temporary) / source.with_suffix('.pdf').name
            page.pdf(path=str(target), print_background=True, display_header_footer=True,
                     header_template='<span></span>', footer_template='''<div style="width:100%;text-align:center;font-size:8px;color:#667788"><span class="pageNumber"></span> / <span class="totalPages"></span></div>''', prefer_css_page_size=True)
        browser.close()
        for target in Path(temporary).glob('*.pdf'):
            (directory / target.name).write_bytes(target.read_bytes())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--month', default='')
    args = parser.parse_args()
    from generate_reports import ROOT, month_window
    from datetime import datetime
    from zoneinfo import ZoneInfo
    month = month_window(args.month, datetime.now(ZoneInfo('Asia/Shanghai')).date())[0]
    export(ROOT / 'reports' / month)
