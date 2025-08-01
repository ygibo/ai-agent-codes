from pydantic import BaseModel, Field


class SearchOutput(BaseModel):
    file_name: str = Field(..., description="ファイル名")
    content: str = Field(..., description="ファイルの内容")

    # TODO: 以下の関数は検索ツールに依存しているので明示的に値を設定するよう変更する
    @classmethod
    def from_hit(cls, hit: dict) -> "SearchOutput":
        return cls(
            file_name=hit["_source"]["file_name"],
            content=hit["_source"]["content"]
        )
    
    """
    @classmethod
    def from_point(cls, point: ScorePoint) -> "SearchOutput":
        if point.payload is None:
            raise ValueError("payload is None")
        return cls(
            file_name=point.payload["file_name"],
            content=point.payload["content"]
        )
    """