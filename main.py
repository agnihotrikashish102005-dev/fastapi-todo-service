from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import httpx
import os

load_dotenv()   # ye line add karo

app = FastAPI()

DJANGO_API_URL = "http://127.0.0.1:8000/api/tasks/"
DJANGO_TOKEN = os.getenv("DJANGO_TOKEN")

HEADERS = {
    "Authorization": f"Token {DJANGO_TOKEN}"
}

@app.get("/tasks")
async def get_tasks():
    async with httpx.AsyncClient() as client:
        response = await client.get(DJANGO_API_URL, headers=HEADERS)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Django API error")
    
    return response.json()