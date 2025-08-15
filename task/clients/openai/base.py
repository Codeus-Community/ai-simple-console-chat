from abc import ABC

from task.clients.base import AIClient


class BaseOpenAIClient(AIClient, ABC):

    def __init__(self, endpoint: str, model_name: str, system_prompt: str, api_key: str):
        if not api_key or api_key.strip() == "":
            raise ValueError("API key cannot be null or empty")
        super().__init__(
            endpoint=endpoint,
            model_name=model_name,
            system_prompt=system_prompt,
            api_key=f"Bearer {api_key}"
        )