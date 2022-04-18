from smtplib import SMTPException, SMTPServerDisconnected, SMTPResponseException, SMTPConnectError

import uvicorn
from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_503_SERVICE_UNAVAILABLE

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


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True, access_log=False)
