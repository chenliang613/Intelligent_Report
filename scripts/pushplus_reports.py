"""Notify PushPlus with links to the selected monthly PDFs."""
import argparse
from datetime import datetime
import json
import os
from urllib.parse import quote
import urllib.request
from zoneinfo import ZoneInfo
from generate_reports import ROOT, month_window, report_names

PDF_NAMES = {
    'report1-model-development.md': '模型发展报告.pdf',
    'report2-agent-development.md': '智能体发展报告.pdf',
    'report3-industry-adoption.md': '行业智能化发展报告.pdf',
}


def build_content(month, selection, repository, revision, run_id):
    lines = [f'## {month} 月度报告已生成', '']
    for name in report_names(selection):
        filename = PDF_NAMES[name]
        pdf = ROOT / 'reports' / month / filename
        if not pdf.is_file():
            raise RuntimeError(f'PDF 不存在：{filename}')
        path = quote(f'reports/{month}/{filename}', safe='/')
        lines.append(f'- [{filename}](https://github.com/{repository}/blob/{revision}/{path})')
    lines += ['', f'[Actions 附件下载](https://github.com/{repository}/actions/runs/{run_id})',
              '', '私有仓库链接需登录有访问权限的 GitHub 账号。']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--month', default='')
    parser.add_argument('--report', choices=['all', 'model', 'agent', 'industry'], default='all')
    args = parser.parse_args()
    token = os.environ.get('PUSHPLUS_TOKEN')
    if not token:
        raise RuntimeError('请配置 Actions Secret PUSHPLUS_TOKEN')
    month = month_window(args.month, datetime.now(ZoneInfo('Asia/Shanghai')).date())[0]
    content = build_content(month, args.report, os.environ['GITHUB_REPOSITORY'],
                            os.environ['REPORT_REVISION'], os.environ['GITHUB_RUN_ID'])
    payload = {'token': token, 'title': f'{month} AI 月度报告',
               'content': content, 'template': 'markdown', 'channel': 'mail'}
    request = urllib.request.Request('https://www.pushplus.plus/send',
                data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(request, timeout=60) as response:
        result = json.load(response)
    if result.get('code') != 200:
        raise RuntimeError(f"PushPlus 未接受推送，错误码：{result.get('code')}")
    print('PushPlus 已接受推送请求；最终送达状态请在 PushPlus 查看。')


if __name__ == '__main__':
    main()
