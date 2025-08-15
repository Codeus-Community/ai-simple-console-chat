import json
import aiohttp
import requests

from task.clients.openai.base import BaseOpenAIClient
from task.models.message import Message
from task.models.role import Role


class CustomOpenAIClient(BaseOpenAIClient):

    def get_completion(self, messages: list[Message], **kwargs) -> Message:
        #TODO:
        # https://platform.openai.com/docs/api-reference/chat
        # - Prepare headers with authorization and content type
        # - Prepare message history with System prompt
        # - Execute post request to AI API (use `requests`)
        # - Parse response
        # - Print response to console
        # - Return AI message
        raise NotImplementedError

    async def stream_completion(self, messages: list[Message], **kwargs) -> Message:
        #TODO:
        # https://platform.openai.com/docs/api-reference/chat
        # - Prepare headers with authorization and content type
        # - Prepare message history with System prompt
        # - Execute post request to AI API (use `aihttp`)
        # - Handle stream with chunks
        # - Parse response
        # - Print chunks to console
        # - Return AI message
        raise NotImplementedError
