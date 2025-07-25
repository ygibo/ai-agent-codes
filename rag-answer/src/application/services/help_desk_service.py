

class HelpDeskService:
    def __init__(self, workflow_service: WorkflowServiceInterface):
        self.workflow_service = workflow_service

    def get_help_desk_info(self):
        pass
    
    def execute(self, client_message: str):
        pass