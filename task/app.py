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
    conversation = Conversation()

    print("Type your question or 'exit' to quit.")
    while True:
        user_input = input("➡️ ").strip()

        if user_input.lower() == "exit":
            print("Exiting the chat. Goodbye!")
            break

        conversation.add_message(Message(Role.USER, user_input))

        print("🤖: ", end="")
        if stream:
            ai_message = await client.stream_completion(conversation.get_messages())
        else:
            ai_message = client.get_completion(conversation.get_messages())

        conversation.add_message(ai_message)


anthropic_client = AnthropicAIClient(
    endpoint=ANTHROPIC_ENDPOINT,
    model_name='claude-sonnet-4-20250514',
    api_key=ANTHROPIC_API_KEY,
    system_prompt=DEFAULT_SYSTEM_PROMPT,
)
anthropic_custom_client = CustomAnthropicAIClient(
    endpoint=ANTHROPIC_ENDPOINT,
    model_name='claude-sonnet-4-20250514',
    api_key=ANTHROPIC_API_KEY,
    system_prompt=DEFAULT_SYSTEM_PROMPT,
)
openai_client = OpenAIClient(
    endpoint=OPENAI_ENDPOINT,
    model_name='gpt-5',
    api_key=OPENAI_API_KEY,
    system_prompt=DEFAULT_SYSTEM_PROMPT,
)
openai_custom_client = CustomOpenAIClient(
    endpoint=OPENAI_ENDPOINT,
    model_name='gpt-5',
    api_key=OPENAI_API_KEY,
    system_prompt=DEFAULT_SYSTEM_PROMPT,
)

asyncio.run(
    start(True, anthropic_custom_client)
)
