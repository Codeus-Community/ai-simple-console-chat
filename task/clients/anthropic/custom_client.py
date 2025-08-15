import json
import aiohttp
import requests

from task.clients.base import AIClient
from task.models.message import Message
from task.models.role import Role


class CustomAnthropicAIClient(AIClient):

    def get_completion(self, messages: list[Message], **kwargs) -> Message:
        #TODO:
        # https://docs.anthropic.com/en/api/messages-examples
        # 1. Prepare headers dict with:
        #   - "x-api-key" (self api key)
        #   - "Content-Type" ("application/json")
        #   - "anthropic-version" ("2023-06-01")
        # 2. Prepare request data dict:
        #   - "model" (self model_name)
        #   - "system" (self system_prompt)
        #   - "max_tokens" (1024)
        #   - "messages" ([message.to_dict() for message in messages])
        # 3. Execute post request to AI API `requests.post(url=self._endpoint, headers=headers, json=request_data)`
        # 4.1. If response status code is 200 then:
        #   - get response json
        #   - get content block
        #   - if content blocks are present:
        #       - get content: "".join(block.get("text", "") for block in content_blocks if block.get("type") == "text")
        #       - print content
        #       - return AI message (role assistant, content is generated content)
        #   - raise ValueError("No content blocks present in the response")
        # 4.2. Otherwise raise Exception(f"HTTP {response.status_code}: {response.text}")
        raise NotImplementedError

    async def stream_completion(self, messages: list[Message], **kwargs) -> Message:
        #TODO:
        # https://docs.anthropic.com/en/docs/build-with-claude/streaming
        # 1. Prepare headers dict with:
        #   - "x-api-key" (self api key)
        #   - "Content-Type" ("application/json")
        #   - "anthropic-version" ("2023-06-01")
        # 2. Prepare request data dict:
        #   - "model" (self model_name)
        #   - "system" (self system_prompt)
        #   - "max_tokens" (kwargs.get("max_tokens", 1024))
        #   - "stream" (True)
        #   - "messages" ([msg.to_dict() for msg in messages])
        # 3. Initialize empty contents list to collect streamed text chunks
        # 4. Create aiohttp ClientSession using `async with aiohttp.ClientSession() as session:`
        # 5. Execute async POST request using `async with session.post(url=self._endpoint, headers=headers, json=request_data) as response:`
        # 6.1. If response status is 200:
        #   - iterate through response content lines using `async for line in response.content:`
        #   - decode each line: `line_str = line.decode('utf-8').strip()`
        #   - check if line starts with "data: " (SSE format)
        #   - extract JSON data: `data = line_str[6:].strip()`
        #   - parse JSON data: `parsed_data = json.loads(data)`
        #   - get event type: `event_type = parsed_data.get("type")`
        #   - if event_type == "content_block_delta":
        #       - get delta: `delta = parsed_data.get("delta", {})`
        #       - if delta.get("type") == "text_delta":
        #           - get text content: `text_content = delta.get("text", "")`
        #           - if text_content is not empty:
        #               - print text_content without newline (end='')
        #               - append text_content to contents list
        #   - else if event_type is `message_stop` then break from the loop
        # 6.2. Otherwise:
        #   - get error text: `error_text = await response.text()`
        #   - print error: f"{response.status} {error_text}"
        # 7. Print empty line (for formatting)
        # 8. Return AI message with joined contents: `Message(role=Role.AI, content=''.join(contents))`
        raise NotImplementedError