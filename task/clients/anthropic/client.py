from anthropic import Anthropic, AsyncAnthropic
from task.clients.base import AIClient
from task.models.message import Message
from task.models.role import Role


class AnthropicAIClient(AIClient):

    def __init__(self, endpoint: str, model_name: str, api_key: str, system_prompt: str):
        #TODO:
        # Call to __init__ of super class
        # Add Anthropic and AsyncAnthropic clients https://github.com/anthropics/anthropic-sdk-python (In readme you can find
        # samples with both of these clients)
        # Useful links with request/response samples:
        #   - https://docs.anthropic.com/en/api/overview
        #   - https://docs.anthropic.com/en/api/messages
        raise NotImplementedError

    def get_completion(self, messages: list[Message], **kwargs) -> Message:
        #TODO:
        # - Add System prompt
        # - Call client
        # - Print response to console
        # - Return AI message
        raise NotImplementedError

    async def stream_completion(self, messages: list[Message], **kwargs) -> Message:
        #TODO:
        # - Add System prompt
        # - Call client with streaming mode
        # - Handle stream with chunks
        # - Print response to console
        # - Return AI message
        raise NotImplementedError

