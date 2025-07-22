from fastapi import FastAPI
import os
from contextlib import asynccontextmanager
from api.db import init_db
from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router)

API_KEY = os.environ.get("API_KEY")
My_Project = os.environ.get("MY_PROJECT") or "This is my project"
if not API_KEY:
    raise NotImplementedError("'API_KEY' is not set")

@app.get("/")
def read_root():
    return {"message": "Hello World Ayaan Merchant - JBS Consulting", "Project Name": My_Project, "API Key": API_KEY}