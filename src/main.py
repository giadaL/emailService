from smtplib import SMTPException, SMTPServerDisconnected, SMTPResponseException, SMTPConnectError

from fastapi import FastAPI, Response
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE

from src.schemas import SendEmailDto
from src.service import send_ssl

app = FastAPI()


@app.post("/send")
async def send(send_email_dto: SendEmailDto) -> Response:
    """
    Sends an email to a receiver with message created from template provided
    """
    try:
        res = send_ssl(send_email_dto.to, send_email_dto.template_name)
        return Response(status_code=res["status_code"], content=str(res), media_type="application/json")
    except (SMTPException, SMTPServerDisconnected, SMTPResponseException, SMTPConnectError):
        return Response(status_code=HTTP_503_SERVICE_UNAVAILABLE)
