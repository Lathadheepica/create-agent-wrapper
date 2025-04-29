from retell import Retell

RETELL_API_KEY = "your_retell_api_key"

client = Retell(api_key=RETELL_API_KEY)

async def create_retell_agent(agent_name: str, voice_id: str, additional_params: dict):
    response = client.agent.create(
        response_engine=additional_params.get("response_engine", {}),
        voice_id=voice_id,
        agent_name=agent_name,
        **additional_params  # Merge any extra params passed
    )
    
    return response
