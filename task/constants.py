import os

DEFAULT_SYSTEM_PROMPT = "You are an assistant who answers concisely and informatively."

OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

ANTHROPIC_API_KEY=os.getenv('ANTHROPIC_API_KEY', '')
ANTHROPIC_ENDPOINT = "https://api.anthropic.com/v1/messages"