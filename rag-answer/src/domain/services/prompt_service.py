from domain.value_objects.prompts import *


class PromptService:
    def __init__(self):
        pass

    def get_create_plan_system_prompt(self) -> str:
        return PLANNER_SYSTEM_PROMPT
    
    def get_create_plan_user_prompt(self, question: str) -> str:
        return PLANNER_USER_PROMPT.format(question=question)

    def get_tool_selection_user_prompt(self, question: str, plan: str, subtask: str) -> str:
        return SUBTASK_TOOL_SELECTION_USER_PROMPT.format(
            question=question,
            plan=plan,
            subtask=subtask
        )

    def get_user_prompt(self, prompt_name: str) -> str:
        return self.prompt_repository.get_user_prompt(prompt_name)