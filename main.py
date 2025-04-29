from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Union

from app.services.vapi_service import create_vapi_agent
from app.services.retell_service import create_retell_agent

app = FastAPI()

class AgentRequest(BaseModel):
    api: str
    agent_name: str
    voice_id: str
    additional_params: dict = {}

@app.post("/create-agent")
async def create_agent(request: AgentRequest):
    if request.api == "vapi":
        return await create_vapi_agent(request.agent_name, request.voice_id, request.additional_params)
    elif request.api == "retell":
        return await create_retell_agent(request.agent_name, request.voice_id, request.additional_params)
    else:
        raise HTTPException(status_code=400, detail="Invalid API type. Choose 'vapi' or 'retell'.")
