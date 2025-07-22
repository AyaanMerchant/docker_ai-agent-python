from fastapi import APIRouter, Depends
from sqlmodel import Session
from api.chat.models import ChatMessagePayload, ChatMessage
from api.db import get_session
router = APIRouter()

@router.get("/api/chat/")
def chat_health():
    return {"status": "ok"}

@router.post("/", response_model=ChatMessage)
def chat_create_message(payload: ChatMessagePayload, session: Session = Depends(get_session)):
    data = payload.model_dump() # pydantic -> dict
    print(data)
    obj_instance = ChatMessage.model_validate(data)
    session.add(obj_instance)
    session.commit()
    session.refresh(obj_instance)

    return obj_instance