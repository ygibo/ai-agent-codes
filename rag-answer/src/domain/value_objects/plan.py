from pydantic import BaseModel, Field


class Plan(BaseModel):
    subtasks: list[str] = Field(..., description="問題を解決するためのサブタスクのリスト")

