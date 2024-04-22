import requests
from typing import Optional

BASE_API_URL = "http://127.0.0.1:7861/api/v1/run"
FLOW_ID = "86c37db6-f637-4629-b61b-39a9bb736f16"
# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}
TWEAKS = {
  "ChatInput-ip4Yg": {},
  "ChatOutput-NsEdB": {},
  "MemoryComponent-koNnY": {},
  "Prompt-PKR99": {},
  "TextOutput-m5Sal": {},
  "OpenAIModel-itZwJ": {}
}

def run_flow(message: str,
  flow_id: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  api_key: Optional[str] = None) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param flow_id: The ID of the flow to run
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/{flow_id}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if api_key:
        headers = {"x-api-key": api_key}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

# Setup any tweaks you want to apply to the flow
message = "message"

print(run_flow(message=message, flow_id=FLOW_ID, tweaks=TWEAKS))