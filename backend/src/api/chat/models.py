from sqlmodel import Field, SQLModel
from pydantic import BaseModel

class ChatMessagePayload(BaseModel):
    message: str

class ChatMessage(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    message: str

