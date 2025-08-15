from openai import OpenAI, AsyncOpenAI
from task.clients.openai.base import BaseOpenAIClient
from task.models.message import Message
from task.models.role import Role


class OpenAIClient(BaseOpenAIClient):

    def __init__(self, endpoint: str, model_name: str, system_prompt: str, api_key: str):
        #TODO:
        # Call to __init__ of super class
        # Add OpenAI and AsyncOpenAI clients https://github.com/openai/openai-python (In readme you can find samples
        # with both of these clients)
        # Useful link with request/response samples https://platform.openai.com/docs/api-reference/chat
        raise NotImplementedError

    def get_completion(self, messages: list[Message], **kwargs) -> Message:
        #TODO:
        # - Prepare message history with System prompt
        # - Call client
        # - Print response to console
        # - Return AI message
        raise NotImplementedError

    async def stream_completion(self, messages: list[Message], **kwargs) -> Message:
        #TODO:
        # - Prepare message history with System prompt
        # - Call client with streaming mode
        # - Handle stream with chunks
        # - Print response to console
        # - Return AI message
        raise NotImplementedError
