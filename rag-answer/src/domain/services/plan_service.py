from domain.services.prompt_service import PromptService
from domain.services.chat_request_service_interface import ChatRequestServiceInterface
from domain.value_objects.plan_state import PlanState
from domain.value_objects.plan import Plan
from domain.value_objects.chat_role import ChatRole
from domain.value_objects.chat_message import ChatMessage
from domain.services.tool_service import ToolService


class PlanService:
    def __init__(
        self,
        prompt_service: PromptService,
        tool_service: ToolService,
        chat_request_service: ChatRequestServiceInterface
    ):
        self.prompt_service = prompt_service
        self.tool_service = tool_service
        self.chat_request_service = chat_request_service

    def create_plan(self, plan_state: PlanState) -> Plan:
        system_prompt = self.prompt_service.get_create_plan_system_prompt()
        user_prompt = self.prompt_service.get_create_plan_user_prompt(plan_state["question"])
        messages = [
            ChatMessage(role=ChatRole.USER, content=user_prompt)
        ]
        plan: Plan = self.chat_request_service.get_output_model(system_prompt, messages, Plan)
        return plan