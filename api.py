from flask import Flask, request, jsonify
import requests
from typing import Optional

app = Flask(__name__)

BASE_API_URL = "http://127.0.0.1:7861/api/v1/run"
FLOW_ID = "57278424-13d8-4578-b101-a43528064750"
TWEAKS = {
    "Prompt-yiUKA": {},
    "File-P4ufU": {},
    "ChatInput-a4J9H": {},
    "ChatOutput-ddfSM": {},
    "TextOutput-pFwo3": {},
    "GoogleGenerativeAIModel-6ejWo": {}
}

def post_flow(message: str,
              flow_id: str,
              output_type: str = "chat",
              input_type: str = "chat",
              tweaks: Optional[dict] = None,
              api_key: Optional[str] = None) -> dict:
    """
    Run a flow with a given message and optional tweaks using POST method.

    :param message: The message to send to the flow
    :param flow_id: The ID of the flow to run
    :param output_type: The type of output expected from the flow
    :param input_type: The type of input message
    :param tweaks: Optional tweaks to customize the flow
    :param api_key: Optional API key for authentication
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/{flow_id}"
    
    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    
    if tweaks:
        payload["tweaks"] = tweaks
    
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["x-api-key"] = api_key

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

@app.route('/chatbot', methods=['POST'])
def post_flow_route():
    request_data = request.json
    
    message = request_data.get('message', '')
    output_type = request_data.get('output_type', 'chat')
    input_type = request_data.get('input_type', 'chat')
    tweaks = request_data.get('tweaks', None)
    api_key = request_data.get('api_key', None)

    response = post_flow(message=message, flow_id=FLOW_ID, output_type=output_type,
                         input_type=input_type, tweaks=tweaks, api_key=api_key)
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
