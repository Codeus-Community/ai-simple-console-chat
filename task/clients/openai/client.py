from openai import OpenAI, AsyncOpenAI
from task.clients.openai.base import BaseOpenAIClient
from task.models.message import Message
from task.models.role import Role


class OpenAIClient(BaseOpenAIClient):

    def __init__(self, endpoint: str, model_name: str, system_prompt: str, api_key: str):
        super().__init__(endpoint, model_name, system_prompt, api_key)
        self._client = OpenAI(api_key=api_key)
        self._async_client = AsyncOpenAI(api_key=api_key)

    def get_completion(self, messages: list[Message], **kwargs) -> Message:
        messages_dicts = [
            {"role": "system", "content": self._system_prompt},
            *[message.to_dict() for message in messages]
        ]
        response = self._client.chat.completions.create(
            model=self._model_name,
            messages=messages_dicts
        )
        content = response.choices[0].message.content
        print(content)
        return Message(role=Role.AI, content=content)

    async def stream_completion(self, messages: list[Message], **kwargs) -> Message:
        messages_dicts = [
            {"role": "system", "content": self._system_prompt},
            *[message.to_dict() for message in messages]
        ]

        content = []

        stream = await self._async_client.chat.completions.create(
            model=self._model_name,
            stream=True,
            messages=messages_dicts
        )

        async for chunk in stream:
            if delta_content := chunk.choices[0].delta.content:
                content.append(delta_content)
                print(delta_content, end='')

        print()
        return Message(role=Role.AI, content="".join(content))
