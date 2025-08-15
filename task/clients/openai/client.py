from openai import OpenAI, AsyncOpenAI
from task.clients.openai.base import BaseOpenAIClient
from task.models.message import Message
from task.models.role import Role


class OpenAIClient(BaseOpenAIClient):

    def __init__(self, endpoint: str, model_name: str, system_prompt: str, api_key: str):
        #TODO:
        # https://github.com/openai/openai-python
        # 1. Call to __init__ of super class
        # 2. Initialize OpenAI client: `self._client = OpenAI(api_key=api_key)`
        # 3. Initialize AsyncOpenAI client: `self._async_client = AsyncOpenAI(api_key=api_key)`
        raise NotImplementedError

    def get_completion(self, messages: list[Message], **kwargs) -> Message:
        #TODO:
        # https://platform.openai.com/docs/api-reference/chat/create
        # 1. Prepare messages list with system message first:
        #   - create messages_dicts list: [{"role": "system", "content": self._system_prompt}, *[message.to_dict() for message in messages]]
        # 2. Create completion using OpenAI client:
        #   - call `self._client.chat.completions.create()` with:
        #     - model=self._model_name
        #     - messages=messages_dicts
        # 3. Extract content from response: `content = response.choices[0].message.content`
        # 4. Print content
        # 5. Return AI message: `Message(role=Role.AI, content=content)`
        raise NotImplementedError

    async def stream_completion(self, messages: list[Message], **kwargs) -> Message:
        #TODO:
        # https://platform.openai.com/docs/api-reference/chat/create
        # 1. Prepare messages list with system message first:
        #   - create messages_dicts list: [{"role": "system", "content": self._system_prompt}, *[message.to_dict() for message in messages]]
        # 2. Initialize empty content list to collect streamed chunks
        # 3. Create streaming completion using AsyncOpenAI client:
        #   - call `await self._async_client.chat.completions.create()` with:
        #     - model=self._model_name
        #     - stream=True
        #     - messages=messages_dicts
        # 4. Iterate through stream chunks using `async for chunk in stream:`
        # 5. For each chunk, check if delta content exists using walrus operator:
        #   - `if delta_content := chunk.choices[0].delta.content:`
        #   - append delta_content to content list
        #   - print delta_content without newline (end='')
        # 6. Print empty line (for formatting)
        # 7. Return AI message with joined content: `Message(role=Role.AI, content="".join(content))`
        raise NotImplementedError