from pydantic import BaseModel, Field
from domain.value_objects.tool_result import ToolResult


class Subtask(BaseModel):
    task_name: str = Field(..., description="サブタスクの名前")
    tool_results: list[list[ToolResult]] = Field(..., description="サブタスクの結果")
    reflection_results: list[ReflectionResult] = Field(..., description="サブタスクの評価結果")
    is_completed: bool = Field(..., description="サブタスクが完了したかどうか")
    subtask_answer: str = Field(..., description="サブタスクの回答")
    challenge_count: int = Field(..., description="サブタスクの挑戦回数")