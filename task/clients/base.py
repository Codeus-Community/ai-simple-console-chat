from abc import ABC, abstractmethod

from task.models.message import Message


class AIClient(ABC):

    def __init__(self, endpoint: str, model_name: str, api_key: str, system_prompt: str):
        if not api_key or api_key.strip() == "":
            raise ValueError("API key cannot be null or empty")

        self._api_key = api_key
        self._endpoint = endpoint
        self._model_name = model_name
        self._system_prompt = system_prompt

    @abstractmethod
    def get_completion(self, messages: list[Message], **kwargs) -> Message:
        """
        Send synchronous request to AI API and return AI response.
        """
        ...

    @abstractmethod
    async def stream_completion(self, messages: list[Message], **kwargs) -> Message:
        """
        Send asynchronous request to AI API and return AI response.
        """
        ...