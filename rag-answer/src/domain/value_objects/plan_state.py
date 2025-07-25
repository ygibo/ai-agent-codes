from typing import Annotated, Sequence, TypedDict
from domain.value_objects.subtask import SubTask
import operator


class PlanState(TypedDict):
    question: str
    plan: list[str]
    current_step: int
    subtask_results: Annotated[Sequence[SubTask], operator.add]
    last_answer: str
