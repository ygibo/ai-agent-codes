from pydantic import BaseModel, Field


class WorkflowResult(BaseModel):
    question: str = Field(..., description="ユーザーの質問")
    plan: list[str] = Field(..., description="エージェントの計画")
    subtasks: list[SubTask] = Field(..., description="サブタスクのリスト")
    answer: str = Field(..., description="最終的な回答")
