from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from api.chat.models import ChatMessagePayload, ChatMessage, ChatMessageList
from api.ai.services import get_email_message
from api.ai.schemas import EmailMessageSchema
from api.db import get_session
from typing import List

router = APIRouter()

@router.get("/")
def chat_health():
    return {"status": "ok"}


# curl http://localhost:8000/api/chat/recent/
@router.get("/recent/", response_model=List[ChatMessageList])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10]
    return results

#curl -X POST -d "{\"message\": \"Hello, world!\"}" -H "Content-Type: application/json" http://localhost:3001/api/chat/ 
#curl -X POST -d "{\"message\": \give me the summary of why its good to go outside\"}" -H "Content-Type: application/json" http://localhost:3001/api/chat/         
#curl -X POST -d "{\"message\": \"Hello, world!\"}" -H "Content-Type: application/json "https://docker-ai-agent-test-dhiym.ondigitalocean.app/api/chat/
@router.post("/", response_model=EmailMessageSchema)
def chat_create_message(payload: ChatMessagePayload, session: Session = Depends(get_session)):
    data = payload.model_dump() # pydantic -> dict
    print(data)
    obj_instance = ChatMessage.model_validate(data)
    session.add(obj_instance)
    session.commit()
    # session.refresh(obj_instance)
    response = get_email_message(payload.message)
    return response