from typing import Annotated, Sequence, TypedDict, operator
from domain.value_objects.search_output import SearchOutput
from domain.value_objects.reflection_result import ReflectionResult


class ExecutionState(TypedDict):
    question: str
    plan: list[str]
    subtask: str
    is_completed: bool
    messages: list[str]
    challenge_count: int
    tool_results: Annotated[Sequence[Sequence[SearchOutput]], operator.add]
    reflection_results: Annotated[Sequence[ReflectionResult], operator.add]
    subtask_answer: str
