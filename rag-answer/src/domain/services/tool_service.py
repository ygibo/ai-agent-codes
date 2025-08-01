from domain.value_objects.tool import Tool

class ToolService:
    def __init__(self):
        self.tools: list[Tool] = []

    def register_tool(self, tool: Tool):
        self.tools.append(tool)

    def get_tools(self) -> list[Tool]:
        return self.tools
