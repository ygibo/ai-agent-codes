from domain.services.prompt_service import PromptService
from domain.services.chat_request_service_interface import ChatRequestServiceInterface
from domain.value_objects.plan_state import PlanState
from domain.value_objects.plan import Plan


class PlanService:
    def __init__(
        self,
        prompt_service: PromptService,
        chat_request_service: ChatRequestServiceInterface
    ):
        self.prompt_service = prompt_service
        self.chat_request_service = chat_request_service

    def create_plan(self, plan_state: PlanState) -> Plan:

        