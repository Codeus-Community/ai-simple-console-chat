import asyncio

from task.clients.anthropic.client import AnthropicAIClient
from task.clients.anthropic.custom_client import CustomAnthropicAIClient
from task.clients.base import AIClient
from task.clients.openai.client import OpenAIClient
from task.clients.openai.custom_client import CustomOpenAIClient
from task.constants import DEFAULT_SYSTEM_PROMPT, OPENAI_ENDPOINT, ANTHROPIC_API_KEY, ANTHROPIC_ENDPOINT, OPENAI_API_KEY
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role


async def start(stream: bool, client: AIClient) -> None:
    #TODO:
    # Main chat loop that handles user interaction with AI clients.
    # 1. Create a new Conversation object to maintain chat history
    # 2. Print to console: `Type your question or 'exit' to quit.`
    # 3. Create infinite `while` loop
    # 4. Get user input from console, use `input` method
    # 5. If user_input is `exit` then `break` the loop
    # 6. Add user message to conversation (role is "user", content is user_input)
    # 7.1. If `stream` is true than call `client.stream_completion` with messages (it's async, don't forget to await)
    # 7.2. Otherwise call `client.get_completion` with messages
    # 7.3. Get Assistant message and add it to the conversation
    raise NotImplementedError


#TODO:
# Create instances of AIClient:
#   - OpenAIClient:
#       - endpoint=OPENAI_ENDPOINT
#       - model_name='gpt-5'
#       - api_key=OPENAI_API_KEY
#       - system_prompt=DEFAULT_SYSTEM_PROMP
#   - CustomOpenAIClient (config the same as above)
#   - AnthropicAIClient
#       - endpoint=ANTHROPIC_ENDPOINT
#       - model_name='claude-sonnet-4-20250514'
#       - api_key=ANTHROPIC_API_KEY
#       - system_prompt=DEFAULT_SYSTEM_PROMP
#   - CustomAnthropicAIClient (config the same as above)
# ----
# Run application:
#   Use asyncio.run() method to run the application (call `start` method in `run`)
raise NotImplementedError


#TODO:
# Test that your application works with different clients, additionally try to print in clients full request and
# response to to check the data that you send and get