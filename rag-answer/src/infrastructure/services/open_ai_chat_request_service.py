import openai
from pydantic import BaseModel
from typing import Type
import logging

logger = logging.getLogger(__name__)

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

    def _to_messages(self, system_prompt: str, messages: list[ChatMessage]) -> list[dict[str, str]]:
        _messages = [
            {"role": "system", "content": system_prompt}
        ]
        for chat_message in messages:
            _messages.append(
                {
                    "role": chat_message.role,
                    "content": chat_message.content
                }
            )
        return _messages

    def get_message(
        self,
        system_prompt: str,
        messages: list[ChatMessage]
    ) -> str:
        messages = self._to_messages(system_prompt, messages)
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.0,
                seed=42
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error getting message content: {e}")
            raise e

    def select_tools(
        self,
        system_prompt: str,
        messages: list[ChatMessage],
        tools: list[Tool]
    ) -> Tool:
        messages = self._to_messages(system_prompt, messages)
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=[self._to_tool_definition(tool) for tool in tools],
                temperature=0.0,
                seed=42
            )
        except Exception as e:
            logger.error(f"Error selecting tool: {e}")
            raise e
    
        # for tool_call in response.choices[0].message.tool_calls:


    def get_output_model(
        self,
        system_prompt: str,
        messages: list[ChatMessage],
        response_format: Type[BaseModel]
    ) -> Type[BaseModel]:
        messages = self._to_messages(system_prompt, messages)
        try:
            response = self.client.chat.completions.parse(
                model=self.model,
                messages=messages,
                response_format=response_format,
                temperature=0.0,
                seed=42
            )
        except Exception as e:
            logger.error(f"Error getting output model: {e}")
            raise e
        return response.choices[0].message.parsed
