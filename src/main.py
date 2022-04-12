from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_503_SERVICE_UNAVAILABLE
from smtplib import SMTPException, SMTPServerDisconnected, SMTPResponseException, SMTPConnectError

from modelsDto import SendEmailDto
from service import send_ssl

app = FastAPI()


@app.post("/send")
async def send(send_email_dto: SendEmailDto) -> Response:
    """
    Sends an email to a receiver with message created from template provided
    """
    try:
        send_ssl(send_email_dto.to, send_email_dto.template_name)
        return Response(status_code=HTTP_200_OK)
    except (SMTPException, SMTPServerDisconnected, SMTPResponseException, SMTPConnectError):
        return Response(status_code=HTTP_503_SERVICE_UNAVAILABLE)
