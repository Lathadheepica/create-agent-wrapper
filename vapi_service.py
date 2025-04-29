import requests

VAPI_URL = "https://api.vapi.ai/assistant"
VAPI_AUTH_TOKEN = "your_vapi_auth_token"

async def create_vapi_agent(agent_name: str, voice_id: str, additional_params: dict):
    headers = {
        "Authorization": f"Bearer {VAPI_AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "name": agent_name,
        "voice": {
            "provider": "azure",
            "voiceId": voice_id
        },
        **additional_params  # Merge any extra params passed
    }
    
    response = requests.post(VAPI_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}
