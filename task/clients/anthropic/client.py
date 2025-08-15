from anthropic import Anthropic, AsyncAnthropic
from task.clients.base import AIClient
from task.models.message import Message
from task.models.role import Role


class AnthropicAIClient(AIClient):

    def __init__(self, endpoint: str, model_name: str, api_key: str, system_prompt: str):
        #TODO:
        # 1. Call to __init__ of super class
        # 2. Add self._client = Anthropic(api_key=api_key)
        # 3. Add self._async_client = AsyncAnthropic(api_key=api_key)
        # Add Anthropic and AsyncAnthropic clients https://github.com/anthropics/anthropic-sdk-python (In readme you can find
        # samples with both of these clients)
        # Useful links with request/response samples:
        #   - https://docs.anthropic.com/en/api/overview
        #   - https://docs.anthropic.com/en/api/messages
        raise NotImplementedError

    def get_completion(self, messages: list[Message], **kwargs) -> Message:
        #TODO:
        # 1. Call client, use `self._client.messages.create` with such params:
        #   - system=self._system_prompt
        #   - max_tokens=1024
        #   - model=self._model_name
        #   - messages=[msg.to_dict() for msg in messages]
        # 2. Iterate through response content and if content type is `text` then concat it
        # 3. Print content to console
        # 4. Return AI message (role assistant, content is generated content)
        raise NotImplementedError

    async def stream_completion(self, messages: list[Message], **kwargs) -> Message:
        #TODO:
        # 1. Call client, use `await self._async_client.messages.create` with such params:
        #   - system=self._system_prompt
        #   - max_tokens=1024
        #   - model=self._model_name
        #   - stream=True
        #   - messages=[msg.to_dict() for msg in messages]
        # 2. Iterate through chunks in generated stream (async for chunk in stream)
        # 2.1. If chunk type is `content_block_delta` then:
        #   - Check if `hasattr(chunk, 'delta') and hasattr(chunk.delta, 'text')` and if yes then:
        #       - get delta text (chunk.delta.text) and assign to `delta_content`
        #       - collect content to array (later we will need to join all the parts into one string with content)
        #       - print chunk content to console `print(delta_content, end='')`
        # 3. Print empty row
        # 4. Return AI message (role assistant, content is generated content)
        raise NotImplementedError

