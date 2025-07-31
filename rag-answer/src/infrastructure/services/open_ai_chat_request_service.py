import openai
from domain.services.chat_request_service_interface import ChatRequestServiceInterface
from domain.value_objects.chat_message import ChatMessage
from domain.value_objects.tool import Tool


class OpenAIChatRequestService(ChatRequestServiceInterface):
    def __init__(self, api_key: str, model: str):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model
    
    def _to_tool_definition(self, tool: Tool) -> dict[str, dict[str, str] | str]:
        return {
            "type": "function",
            "function": {
                "name": tool.tool_name,
                "description": tool.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        arg_name: arg_definition.to_dict()
                        for arg_name, arg_definition in tool.arg_definitions.items()
                    }
                }
            }
        }

    def get_message_content(self) -> str:
        pass

    def select_tool(self, tools: list[Tool], message: ChatMessage) -> Tool:
        pass
    
    def get_output_model(self, response_model: Type[BaseModel]) -> Type[BaseModel]:
        return response_model

    def request(self, user_message: str, tools: list[Tool], response_model: Optional[Type[BaseModel]] = None) -> ChatMessage | Tool | BaseModel:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": user_message}],
            tools=[self._to_tool_definition(tool) for tool in tools]
        )
        return response.choices[0].message
