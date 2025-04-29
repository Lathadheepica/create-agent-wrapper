# Create Agent API Wrapper

This repository provides a unified wrapper around two agent creation APIs: VAPI and Retell.

#Structure
create-agent-wrapper/
├── app/
│   ├── services/
│   │   ├── vapi_service.py
│   │   └── retell_service.py
│   └── schemas.py
├── main.py
├── requirements.txt
└── README.md

### Setup

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the FastAPI app: `uvicorn main:app --reload`.

### Usage

- To create an agent, make a POST request to `/create-agent` with the following JSON body:
  ```json
  {
    "api": "vapi",
    "agent_name": "MyAgent",
    "voice_id": "azure-voice-id",
    "additional_params": {}
  }


### **Explanation of Standardization:**

- **Agent Name:** This will be the same across both APIs (`agent_name`).
- **Voice ID:** Voice ID will be passed for both APIs in the same way.
- **Additional Params:** The `additional_params` field will allow you to pass any extra parameters (like transcription settings, models, etc.) that might be specific to either VAPI or Retell.

This structure keeps the endpoint simple for external users, allowing them to choose which backend API to use and submit all necessary data in a standardized format.
