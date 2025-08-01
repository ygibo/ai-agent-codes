from pydantic import BaseModel, Field
from typing import Any
from domain.value_objects.chat_role import ChatRole


class ChatMessage(BaseModel):
    role: ChatRole = Field(..., description="メッセージの役割")
    content: str = Field(..., description="メッセージの内容")

    def to_dict(self) -> dict[str, str]:
        return {
            "role": self.role,
            "content": self.content
        }


