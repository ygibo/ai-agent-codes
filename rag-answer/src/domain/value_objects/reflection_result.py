from pydantic import BaseModel, Field


class ReflectionResult(BaseModel):
    advice: str = Field(
        ...,
        description="評価がNGの場合は、別のツールを試す、別の文言でツールを試す等、なぜNGなのかどうしたら改善できるかアドバイスを作成してください。\
        アドバイスの内容は過去のアドバイスと計画内の他のサブタスクと重複しないようにしてください。\
        アドバイスの内容を元にツール選択・実行からやり直します。
    )
    is_completed: bool = Field(
        ...,
        description="ツールの実行結果と回答からサブタスクに対して正しく解答できているかの評価結果
    )
