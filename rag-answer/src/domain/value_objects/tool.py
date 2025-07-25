from pydantic import BaseModel, Field
from typing import Any, Callable


class ArgDefinition(BaseModel):
    arg_type: str = Field(..., description="引数の型")
    arg_description: str = Field(..., description="引数の説明")

    def to_dict(self) -> dict[str, str]:
        return {
            "type": self.arg_type,
            "description": self.arg_description
        }

class Tool(BaseModel):
    tool_name: str = Field(..., description="ツールの名前")
    description: str = Field(..., description="ツールの説明")
    arg_definitions: dict[str, ArgDefinition] = Field(..., description="引数の定義")
    function: Callable = Field(..., description="ツールの関数")

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.function(*args, **kwargs)

    def to_dict(self) -> dict[str, dict[str, str] | str]:
        return {
            "tool_name": self.tool_name,
            "description": self.description,
            "arg_definitions": {
                arg_name: str(arg_definition)
                for arg_name, arg_definition in self.arg_definitions.items()
            }
        }