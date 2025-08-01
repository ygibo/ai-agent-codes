from domain.services.prompt_service import PromptService
from domain.services.tool_service import ToolService
from domain.services.chat_request_service_interface import ChatRequestServiceInterface
from domain.value_objects.execution_state import ExecutionState
from domain.value_objects.tool import Tool
from domain.value_objects.chat_message import ChatMessage, ChatRole


class SubTaskExecutionService:
    def __init__(
        self,
        prompt_service: PromptService,
        tool_service: ToolService,
        chat_request_service: ChatRequestServiceInterface
    ):
        self.prompt_service = prompt_service
        self.tool_service = tool_service
        self.chat_request_service = chat_request_service

    def select_tools(
        self,
        execution_state: ExecutionState
    ) -> list[ToolCall]:
        system_prompt = self.prompt_service.get_tool_selection_system_prompt()
        user_prompt = self.prompt_service.get_tool_selection_user_prompt(
            question=execution_state["question"],
            plan=execution_state["plan"],
            subtask=execution_state["subtask"]
        )
        messages = [
            ChatMessage(role=ChatRole.USER, content=user_prompt)
        ]
        tools: list[ToolCall] = self.chat_request_service.select_tools(
            system_prompt=system_prompt,
            messages=messages,
            tools=self.tool_service.get_tools()
        )
        return tools

    def execute_tools(
        self,
        execution_state: ExecutionState
    ) -> list[ToolResult]:
        pass