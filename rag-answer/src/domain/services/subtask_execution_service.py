


class SubTaskExecutionService:
    def __init__(
        self,
        chat_request_service: ChatRequestServiceInterface
    ):
        self.chat_request_service = chat_request_service

    def get_execution_info(self):
        pass