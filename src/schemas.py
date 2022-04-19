from uuid import UUID

from pydantic import BaseModel


class SendEmailDto(BaseModel):
    to: str
    template_name: str


class TemplateDTO(BaseModel):
    base64: str
    filename: str
    id: UUID


class TemplateInfoDTO(BaseModel):
    id: UUID
    subject: str
    attachments: list[UUID]
    filename: str


class AttachmentDTO(BaseModel):
    base64: str
    filename: str
    mimetype: str
