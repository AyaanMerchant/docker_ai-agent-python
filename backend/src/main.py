from fastapi import FastAPI
import os

API_KEY = os.environ.get("API_KEY")
My_Project = os.environ.get("MY_PROJECT") or "This is my project"
if not API_KEY:
    raise NotImplementedError("'API_KEY' is not set")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World Ayaan Merchant - JBS Consulting", "Project Name": My_Project, "API Key": API_KEY}