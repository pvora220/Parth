from fastapi import FastAPI

from backend.ai.agent import AIAgent

app = FastAPI(title="OSINT Cyber Intelligence Platform")
agent = AIAgent()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/investigate/{target}")
async def investigate(target: str):
    return await agent.investigate(target)
