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
        # 1. Prepare headers dict with:
        #   - "Authorization" (self api key)
        #   - "Content-Type" ("application/json")
        # 2. Prepare messages list:
        #   - create messages_dicts list with system message first:
        #     [{"role": "system", "content": self._system_prompt}, *[message.to_dict() for message in messages]]
        # 3. Prepare request data dict:
        #   - "model" (self model_name)
        #   - "messages" (messages_dicts)
        # 4. Execute post request to AI API `requests.post(url=self._endpoint, headers=headers, json=request_data)`
        # 5.1. If response status code is 200 then:
        #   - get response json
        #   - get choices: `choices = data.get("choices", [])`
        #   - if choices are present:
        #       - get content: `content = choices[0].get("message", {}).get("content")`
        #       - print content
        #       - return AI message (role assistant, content is generated content)
        #   - raise ValueError("No Choice has been present in the response")
        # 5.2. Otherwise raise Exception(f"HTTP {response.status_code}: {response.text}")
        raise NotImplementedError

    async def stream_completion(self, messages: list[Message], **kwargs) -> Message:
        #TODO:
        # https://platform.openai.com/docs/api-reference/chat
        # 1. Prepare headers dict with:
        #   - "Authorization" (self api key)
        #   - "Content-Type" ("application/json")
        # 2. Prepare messages list:
        #   - create messages_dicts list with system message first:
        #     [{"role": "system", "content": self._system_prompt}, *[message.to_dict() for message in messages]]
        # 3. Prepare request data dict:
        #   - "model" (self model_name)
        #   - "stream" (True)
        #   - "messages" (messages_dicts)
        # 4. Initialize empty contents list to collect streamed text chunks
        # 5. Create aiohttp ClientSession using `async with aiohttp.ClientSession() as session:`
        # 6. Execute async POST request using `async with session.post(url=self._endpoint, headers=headers, json=request_data) as response:`
        # 7.1. If response status is 200:
        #   - iterate through response content lines using `async for line in response.content:`
        #   - decode each line: `line_str = line.decode('utf-8').strip()`
        #   - check if line starts with "data: " (SSE format)
        #   - extract data: `data = line_str[6:].strip()`
        #   - if data is NOT "[DONE]":
        #       - get content snippet using self._get_content_snippet(data)
        #       - print content snippet without newline (end='')
        #       - append content snippet to contents list
        #   - otherwise print empty line (for formatting)
        # 7.2. Otherwise:
        #   - get error text: `error_text = await response.text()`
        #   - print error: f"{response.status} {error_text}"
        # 8. Return AI message with joined contents: `Message(role=Role.AI, content=''.join(contents))`
        raise NotImplementedError

    def _get_content_snippet(self, data: str) -> str:
        """
        Extract content from streaming data chunk.
        """
        #TODO:
        # 1. Parse JSON data: `data = json.loads(data)`
        # 2. Get choices from data: `choices = data.get("choices")`
        # 3. If choices exist (use walrus operator: `if choices := data.get("choices"):`):
        #   - get delta from first choice: `delta = choices[0].get("delta", {})`
        #   - return content from delta: `delta.get("content", '')`
        # 4. Otherwise return empty string
        raise NotImplementedError