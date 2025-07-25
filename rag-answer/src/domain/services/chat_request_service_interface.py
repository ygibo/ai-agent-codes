from abc import ABC, abstractmethod
from domain.value_objects.chat_message import ChatMessage
from domain.value_objects.tool import Tool


class ChatRequestServiceInterface(ABC):
    @abstractmethod
    def request(
        self,
        user_message: str,
        tools: list[Tool]
    ) -> ChatMessage | Tool:
        """
        ユーザーのメッセージと使用可能ツールを受け取り、
        チャットメッセージもしくは選択されたツールを返す
        """
        pass