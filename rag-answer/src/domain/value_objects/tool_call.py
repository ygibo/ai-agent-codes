from pydantic import BaseModel, Field

class ToolCall(BaseModel):
    tool_call_id: str = Field(..., description="ツールの呼び出しID")
    tool_name: str = Field(..., description="ツールの名前")
    args: dict[str, str] = Field(..., description="ツールの引数")

    def to_dict(self) -> dict[str, str]:
        return {
            "tool_name": self.tool_name,
            "args": self.args
        }