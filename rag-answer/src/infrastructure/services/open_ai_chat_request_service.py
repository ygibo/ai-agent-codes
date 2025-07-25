import openai
from domain.services.chat_request_service_interface import ChatRequestServiceInterface
from domain.value_objects.chat_message import ChatMessage
from domain.value_objects.tool import Tool


class OpenAIChatRequestService(ChatRequestServiceInterface):
    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)
            
