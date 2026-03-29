from fastapi import FastAPI
from dotenv import load_dotenv
from pathlib import Path
from pydantic import BaseModel
import os
from tavily import TavilyClient

load_dotenv(Path(__file__).parent / ".env")

app = FastAPI()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

class ResearchRequest(BaseModel):
    company: str

@app.get("/")
def home():
    return {"message": "CompeteIQ backend is running"}

@app.post("/research")
def research(request: ResearchRequest):
    results = tavily.search(
        query=f"{request.company} company overview funding news 2025",
        max_results=5
    )
    return {
        "company": request.company,
        "results": results["results"]
    }
