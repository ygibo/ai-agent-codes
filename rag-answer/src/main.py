from domain.value_objects.tool import Tool, ArgDefinition


#!/usr/bin/env python3
def search_tool(query: str) -> list[str]:
    return ["search_result1", "search_result2"]

search_tool = Tool(
    tool_name="search_tool",
    description="検索ツール",
    arg_definitions={
        "query": ArgDefinition(
            arg_type="str",
            arg_description="検索クエリ"
        )
    },
    function=search_tool
)

def main():
    print(search_tool.to_dict())

if __name__ == "__main__":
    main()