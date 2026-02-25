from domain.value_objects.tool import Tool, ArgDefinition
from domain.services.plan_service import PlanService
from domain.value_objects.plan_state import PlanState
from domain.services.subtask_execution_service import SubTaskExecutionService
from domain.value_objects.execution_state import ExecutionState
from domain.services.prompt_service import PromptService
from domain.services.tool_service import ToolService
from domain.value_objects.plan import Plan
from infrastructure.services.open_ai_chat_request_service import OpenAIChatRequestService
import os
from dotenv import load_dotenv

load_dotenv()


def get_chat_request_service():
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_CHAT_MODEL")
    return OpenAIChatRequestService(
        api_key=api_key,
        model=model
    )

def test_create_plan():
    chat_request_service = get_chat_request_service()
    plan_service = PlanService(
        prompt_service=PromptService(),
        tool_service=ToolService(),
        chat_request_service=chat_request_service
    )
    question = """
お世話になっております。

現在、XYZシステムの利用を検討しており、以下の2点についてご教示いただければと存じます。

1. パスワードに利用可能な文字の制限について
当該システムにてパスワードを設定する際、使用可能な文字の範囲（例：英数字、記号、文字数制限など）について詳しい情報をいただけますでしょうか。安全かつシステムでの認証エラーを防ぐため、具体的な仕様を確認したいと考えております。

2. 最新リリースの取得方法について
最新のアップデート情報をどのように確認・取得できるかについてもお教えいただけますと幸いです。

お忙しいところ恐縮ですが、ご対応のほどよろしくお願い申し上げます。
"""
    plan_state = PlanState(
        question=question,
        plan=[]
    )
    print(plan_state)
    plan = plan_service.create_plan(plan_state)
    print(plan)

def get_tool_service():
    tool_service = ToolService()
    manual_search_tool = Tool(
        tool_name="seach_xyz_manual",
        description="""XYZシステムのドキュメントをキーワード検索する関数。エラーコードや固有名詞が質問に含まれる場合は、この関数を使用しキーワード検索を行う。""",
        arg_definitions={
            "keywords": ArgDefinition(
                arg_type="string",
                arg_description="全文検索用のキーワード"
            )
        },
        function=lambda: print("manual_search")
    )

    qa_search_tool = Tool(
        tool_name="search_xyz_qa",
        description="""XYZシステムの過去の質問回答ペアを検索する""",
        arg_definitions={
            "question": ArgDefinition(
                arg_type="string",
                arg_description="検索クエリ"
            )
        },
        function=lambda: print("qa_search")
    )

    tool_service.register_tool(manual_search_tool)
    tool_service.register_tool(qa_search_tool)
    return tool_service

def test_select_tools():
    chat_request_service = get_chat_request_service()
    tool_service = get_tool_service()
    subtask_execution_service = SubTaskExecutionService(
        prompt_service=PromptService(),
        tool_service=tool_service,
        chat_request_service=chat_request_service
    )
    plan = Plan(
        subtasks=[
            'XYZシステムのパスワード設定における使用可能な文字の種類（英数字、記号など）について調べる',
            'XYZシステムのパスワード設定における文字数制限について調べる',
            'XYZシステムの最新リリース情報を確認する方法について調べる',
            'XYZシステムの最新リリースを取得する方法について調べる'
        ]
    )
    for subtask in plan.subtasks:
        tool_calls: list[ToolCall] = subtask_execution_service.select_tools(
            execution_state=ExecutionState(
                question="パスワードを忘れました",
                plan=plan,
                subtask=subtask
            )
        )
        print(tool_calls)

if __name__ == "__main__":
    # test_create_plan()
    test_select_tools()