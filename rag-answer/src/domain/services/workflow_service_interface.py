import abc
from domain.services.plan_service import PlanService
from domain.services.execution_service import ExecutionService


class WorkflowServiceInterface(abc.ABC):
    def __init__(self, plan_service: PlanService, execution_service: ExecutionService):
        self.plan_service = plan_service
        self.execution_service = execution_service

    @abc.abstractmethod
    def execute(self, question: str) -> PlanState:
        pass