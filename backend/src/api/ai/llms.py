import os
from langchain_openai import ChatOpenAI

OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL") or None
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME") or "gpt-4o-mini"
if not OPENAI_API_KEY:
    raise NotImplementedError("OPENAI_API_KEY is not set")


def get_llm_base():
    openai_params = {
    "model": OPENAI_MODEL_NAME,
    "api_key": OPENAI_API_KEY
    }
    if OPENAI_BASE_URL:
        openai_params["base_url"] = OPENAI_BASE_URL
    return ChatOpenAI(**openai_params)

