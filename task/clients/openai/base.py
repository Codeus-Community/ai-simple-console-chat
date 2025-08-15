from abc import ABC

from task.clients.base import AIClient


class BaseOpenAIClient(AIClient, ABC):

    def __init__(self, endpoint: str, model_name: str, system_prompt: str, api_key: str):
        #TODO:
        # Make validation for `api_key` (the same as in parent class)
        # Call to __init__ of super class
        # The `api_key` should be formatted according to Open AI specification https://platform.openai.com/docs/guides/text
        raise NotImplementedError