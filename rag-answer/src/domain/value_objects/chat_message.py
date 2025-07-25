from pydantic import BaseModel, Field
from typing import Any


class ChatMessage(BaseModel):
    role: str = Field(..., description="メッセージの役割")
    content: str = Field(..., description="メッセージの内容")

    def to_dict(self) -> dict[str, str]:
        return {
            "role": self.role,
            "content": self.content
        }


