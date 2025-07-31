from abc import ABC, abstractmethod
from domain.value_objects.chat_message import ChatMessage
from domain.value_objects.tool import Tool


class ChatRequestServiceInterface(ABC):
    @abstractmethod
    def get_message(
        self,
        system_prompt: str,
        messages: list[ChatMessage]
    ) -> str:
        pass
    
    @abstractmethod
    def select_tool(
        self,
        system_prompt: str,
        messages: list[ChatMessage],
        tools: list[Tool]
    ) -> Tool:
        pass
    
    @abstractmethod
    def get_output_model(
        self,
        system_prompt: str,
        messages: list[ChatMessage],
        response_format: Type[BaseModel]
    ) -> Type[BaseModel]:
        pass
        