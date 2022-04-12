from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from modelsDto import SendEmailDto

app = FastAPI()


@app.post("/send")
async def send(send_email_dto: SendEmailDto) -> Response:
    """
    Sends an email to a list of receivers with message created from template provided
    """
    return Response(status_code=HTTP_200_OK) if True else Response(status_code=HTTP_400_BAD_REQUEST)
