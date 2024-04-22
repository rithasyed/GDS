from langflow.load import run_flow_from_json
TWEAKS = {
  "Prompt-yiUKA": {},
  "File-P4ufU": {},
  "ChatInput-a4J9H": {},
  "ChatOutput-ddfSM": {},
  "TextOutput-pFwo3": {},
  "GoogleGenerativeAIModel-6ejWo": {}
}

result = run_flow_from_json(flow="Untitled document (2).json",
                            input_value="message",
                            tweaks=TWEAKS)