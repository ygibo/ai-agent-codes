import abc
from domain.services.plan_service import PlanService
from domain.services.execution_service import ExecutionService
from domain.services.workflow_service_interface import WorkflowServiceInterface


class WorkflowFactoryInterface(abc.ABC):
    def __init__(self, plan_service: PlanService, execution_service: ExecutionService):
        self.plan_service = plan_service
        self.execution_service = execution_service

    @abc.abstractmethod
    def create_workflow(self) -> WorkflowServiceInterface:
        # ワークフローの作成を行う
        pass
