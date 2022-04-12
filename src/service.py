import smtplib as smtp

import ssl
import codecs

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from config import UseDotNotation, SMTP_CONFIG

MOCKED_TEMPLATES = UseDotNotation({
    "template1": {
        "subject": "Confirm Account",
        "file": "mocked_template_file.html",
        "attachment": []
    }
})


def _build_message(to, template):
    tmessage = MIMEMultipart("alternative")
    tmessage["Subject"] = template["subject"]
    tmessage["To"] = to
    tmessage["From"] = "My APP"
    f = codecs.open(f"mock/{template['file']}", "r")
    message = f.read()
    msg = MIMEText(message, "html")
    for f in template["attachment"]:
        file_info = UseDotNotation(f)
        file = file_info.filePath
        openedFile = open(file)
        mimref = MIMEBase("application", file_info.mimeType)
        mimref.set_payload(openedFile.read())
        encoders.encode_base64(mimref)
        mimref.add_header(f"Content-Disposition", f"attachment;filename={file_info.fileName}")
        tmessage.attach(mimref)

    tmessage.attach(msg)
    return tmessage


def send_ssl(to, template):
    mocked_template = UseDotNotation(MOCKED_TEMPLATES.template1)
    host, port, userName, password = SMTP_CONFIG.values()
    context = ssl.create_default_context()
    with smtp.SMTP_SSL(host, 465, context=context) as server:
        server.login(userName, password)
        message = _build_message(to, mocked_template)
        server.sendmail("MyApp", to, message.as_string())

