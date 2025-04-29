from pydantic import BaseModel
from typing import Dict, Any

class AgentRequest(BaseModel):
    api: str
    agent_name: str
    voice_id: str
    additional_params: Dict[str, Any] = {}
