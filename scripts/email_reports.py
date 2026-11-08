"""Send the selected monthly PDFs via an authenticated SMTP server."""
import argparse
from datetime import datetime
from email.message import EmailMessage
import os
from pathlib import Path
import smtplib
import ssl
from zoneinfo import ZoneInfo
from generate_reports import ROOT, month_window, report_names

PDF_NAMES = {
    'report1-model-development.md': '模型发展报告.pdf',
    'report2-agent-development.md': '智能体发展报告.pdf',
    'report3-industry-adoption.md': '行业智能化发展报告.pdf',
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--month', default='')
    parser.add_argument('--report', choices=['all', 'model', 'agent', 'industry'], default='all')
    args = parser.parse_args()
    required = ['SMTP_HOST', 'SMTP_USERNAME', 'SMTP_PASSWORD', 'SMTP_FROM']
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        raise RuntimeError('缺少邮件配置：' + ', '.join(missing))
    month = month_window(args.month, datetime.now(ZoneInfo('Asia/Shanghai')).date())[0]
    message = EmailMessage()
    message['Subject'] = f'{month} AI 行业月度报告'
    message['From'] = os.environ['SMTP_FROM']
    message['To'] = 'chenliang613@apache.org'
    message.set_content(f'附件为 {month} 的 PDF 报告，请查收。')
    for name in report_names(args.report):
        pdf = ROOT / 'reports' / month / PDF_NAMES[name]
        message.add_attachment(pdf.read_bytes(), maintype='application', subtype='pdf', filename=pdf.name)
    port = int(os.environ.get('SMTP_PORT') or '465')
    context = ssl.create_default_context()
    if port == 465:
        server = smtplib.SMTP_SSL(os.environ['SMTP_HOST'], port, context=context, timeout=60)
    else:
        server = smtplib.SMTP(os.environ['SMTP_HOST'], port, timeout=60)
        server.starttls(context=context)
    with server:
        server.login(os.environ['SMTP_USERNAME'], os.environ['SMTP_PASSWORD'])
        refused = server.send_message(message)
        if refused:
            raise RuntimeError('邮件服务器拒绝收件人')
    print('邮件已提交 SMTP 服务器：chenliang613@apache.org')


if __name__ == '__main__':
    main()
