import smtplib as smtp
import ssl
from base64 import b64decode
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import UseDotNotation, SMTP_CONFIG
from src.template_client import get_template_file, get_template_info, get_template_attachments


def _build_message(to, template):
    tmessage = MIMEMultipart("alternative")
    tmessage["Subject"] = template["subject"]
    tmessage["To"] = to
    tmessage["From"] = "My APP"

    msg = MIMEText(template["message"].decode('UTF-8'), "html")
    for f in template["attachment"]:
        file_info = UseDotNotation(f)
        mimref = MIMEBase("application", file_info.mimetype)
        mimref.set_payload(file_info.file)
        encoders.encode_base64(mimref)
        mimref.add_header(f"Content-Disposition", f"attachment;filename={file_info.filename}")
        tmessage.attach(mimref)

    tmessage.attach(msg)
    return tmessage


def send_ssl(to, template_name):
    template_file, error = get_template_file(template_name)
    template_file = UseDotNotation(template_file)
    if error:
        return error
    if template_file:
        infos, error = get_template_info(template_file.id)
        if error:
            return error
        infos = UseDotNotation(infos)
        file = b64decode(template_file.base64)
        attachments, error = get_template_attachments(template_file.id)
        if error:
            return error
        template = {
            "subject": infos.subject,
            "message": file,
            "attachment": [
                {
                    "file": b64decode(at["base64"]),
                    "mimetype": at["mimetype"],
                    "filename": at["filename"]
                }
                for at in attachments
            ]
        }
        host, port, userName, password = SMTP_CONFIG.values()
        context = ssl.create_default_context()
        with smtp.SMTP_SSL(host, 465, context=context) as server:
            server.login(userName, password)
            message = _build_message(to, template)
            server.sendmail("MY PYTHON SENDER", to, message.as_string())
            return {"status_code": 200, "message": "sent"}

    return {"status_code": 500, "message": "something went wrong"}
