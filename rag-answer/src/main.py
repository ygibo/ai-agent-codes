from domain.value_objects.tool import Tool, ArgDefinition
from domain.services.plan_service import PlanService
from domain.value_objects.plan_state import PlanState
from domain.services.prompt_service import PromptService
from domain.services.tool_service import ToolService
from infrastructure.services.open_ai_chat_request_service import OpenAIChatRequestService
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    # dotenv から api_key と model を取得
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_CHAT_MODEL")

    plan_service = PlanService(
        prompt_service=PromptService(),
        tool_service=ToolService(),
        chat_request_service=OpenAIChatRequestService(
            api_key=api_key,
            model=model
        )
    )
    plan_state = PlanState(
        question="AとBの違いについて教えて",
        plan=[]
    )
    print(plan_state)
    plan = plan_service.create_plan(plan_state)
    print(plan)


if __name__ == "__main__":
    main()