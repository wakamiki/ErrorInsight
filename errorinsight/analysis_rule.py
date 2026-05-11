from dataclasses import dataclass


@dataclass
class AnalysisRule:
    keyword: str  # エラー行に含まれていたら、このルールを使う判定文字列
    language_hint: str  # エラーの言語のヒント（例："Python", "Java"など）
    description: str  # エラーの簡易説明
    cause_candidate: str  # 原因候補
    check_point: str  # 確認ポイント
