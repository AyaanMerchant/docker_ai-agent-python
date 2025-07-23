from api.ai.llms import get_llm_base
from api.ai.schemas import EmailMessageSchema

def get_email_message(message: str) -> EmailMessageSchema:
    llm_base = get_llm_base()
    llm = llm_base.with_structured_output(EmailMessageSchema)

    message = [
    (
        "system",
        "You are a helpful assistant for research and composing plaintext email. do not use markdown in your response only plain text"
    ),
    (
        "human",
        f"{message}, do not use the markdown in your response only plain text"
    )
]
    response = llm.invoke(message)
    return response