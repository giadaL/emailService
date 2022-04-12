from pydantic import BaseModel


class SendEmailDto(BaseModel):
    to: list[str]
    template_name: str
