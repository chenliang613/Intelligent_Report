"""Export Markdown source reports as standalone, offline-readable HTML."""
import argparse
from datetime import datetime
from html import escape
from pathlib import Path
from zoneinfo import ZoneInfo
from markdown_it import MarkdownIt
try:
    from .generate_reports import ROOT, month_window, report_names
except ImportError:
    from generate_reports import ROOT, month_window, report_names

HTML_NAMES = {
    'report1-model-development.md': '模型发展报告.html',
    'report2-agent-development.md': '智能体发展报告.html',
    'report3-industry-adoption.md': '行业智能化发展报告.html',
}
STYLE = '''
*{box-sizing:border-box}body{margin:0;background:#f2f5f9;color:#253247;
font:16px/1.8 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif}
main{max-width:1100px;margin:32px auto;padding:40px;background:white;border-radius:12px}
h1{font-size:2em;color:#12365b;line-height:1.4}h2{border-bottom:1px solid #ccd7e3;padding-bottom:8px;color:#18476f}
a{color:#1767a3;overflow-wrap:anywhere}table{border-collapse:collapse;width:100%;font-size:.9em}
th,td{border:1px solid #cdd6df;padding:9px;overflow-wrap:anywhere}th{background:#eaf0f6}
.table-scroll{overflow-x:auto}blockquote{border-left:4px solid #4284ad;margin-left:0;padding-left:16px}
pre{overflow:auto;background:#f3f6f9;padding:16px}img{max-width:100%}
@media(max-width:700px){main{margin:0;padding:20px;border-radius:0}h1{font-size:1.6em}}
@media print{body{background:white}main{margin:0;padding:0}h1,h2,h3{break-after:avoid}thead{display:table-header-group}}
'''


def render(source, title):
    body = MarkdownIt('commonmark', {'html': False}).enable('table').render(source)
    body = body.replace('<table>', '<div class="table-scroll"><table>').replace('</table>', '</table></div>')
    return (f'<!doctype html>\n<html lang="zh-CN"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; style-src \'unsafe-inline\'; img-src data:;">'
            f'<title>{escape(title)}</title><style>{STYLE}</style></head><body><main>{body}</main></body></html>\n')


def export(directory, selection='all'):
    directory = Path(directory)
    sources = [directory / name for name in report_names(selection)]
    outputs = {}
    for source in sources:
        filename = HTML_NAMES[source.name]
        outputs[directory / filename] = render(source.read_text(), f'{directory.name} {filename[:-5]}')
    for destination, content in outputs.items():
        destination.write_text(content, encoding='utf-8')
        print(f'已生成 {destination}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--month', default='')
    parser.add_argument('--report', choices=['all', 'model', 'agent', 'industry'], default='all')
    args = parser.parse_args()
    month = month_window(args.month, datetime.now(ZoneInfo('Asia/Shanghai')).date())[0]
    export(ROOT / 'reports' / month, args.report)
