from pydantic import BaseModel


class SendEmailDto(BaseModel):
    to: str
    template_name: str

