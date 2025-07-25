from pydantic import BaseModel, Field


class ToolResult(BaseModel):
    tool_name: str = Field(..., description="ツールの名前")
    args: str = Field(..., description="ツールの引数")
    results: list[SearchOutput] = Field(..., description="ツールの結果")
