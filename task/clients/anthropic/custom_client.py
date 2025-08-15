import json
import aiohttp
import requests

from task.clients.base import AIClient
from task.models.message import Message
from task.models.role import Role


class CustomAnthropicAIClient(AIClient):

    def get_completion(self, messages: list[Message], **kwargs) -> Message:
        headers = {
            "x-api-key": self._api_key,
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01"
        }
        request_data = {
            "model": self._model_name,
            "system": self._system_prompt,
            "max_tokens": kwargs.get("max_tokens", 1024),
            "messages": [message.to_dict() for message in messages]
        }

        response = requests.post(url=self._endpoint, headers=headers, json=request_data)

        if response.status_code == 200:
            data = response.json()
            content_blocks = data.get("content", [])
            if content_blocks:
                content = "".join(block.get("text", "") for block in content_blocks if block.get("type") == "text")
                print(content)
                return Message(Role.AI, content)
            raise ValueError("No content blocks present in the response")
        else:
            raise Exception(f"HTTP {response.status_code}: {response.text}")

    async def stream_completion(self, messages: list[Message], **kwargs) -> Message:
        headers = {
            "x-api-key": self._api_key,
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01"
        }
        request_data = {
            "model": self._model_name,
            "system": self._system_prompt,
            "max_tokens": kwargs.get("max_tokens", 1024),
            "stream": True,
            "messages": [msg.to_dict() for msg in messages]
        }
        contents = []

        async with aiohttp.ClientSession() as session:
            async with session.post(url=self._endpoint, headers=headers, json=request_data) as response:
                if response.status == 200:
                    async for line in response.content:
                        line_str = line.decode('utf-8').strip()
                        if line_str.startswith("data: "):
                            data = line_str[6:].strip()
                            parsed_data = json.loads(data)
                            event_type = parsed_data.get("type")

                            if event_type == "content_block_delta":
                                delta = parsed_data.get("delta", {})
                                if delta.get("type") == "text_delta":
                                    text_content = delta.get("text", "")
                                    if text_content:
                                        print(text_content, end='')
                                        contents.append(text_content)
                            elif event_type == "message_stop":
                                break
                else:
                    error_text = await response.text()
                    print(f"{response.status} {error_text}")

                print()
                return Message(role=Role.AI, content=''.join(contents))

