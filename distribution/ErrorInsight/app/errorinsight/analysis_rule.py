import re
from dataclasses import dataclass


@dataclass
class HintRule:
    pattern: re.Pattern[str]  # エラー本文から情報を抜くための正規表現
    template: str  # 抜き出した情報をどう表示するか


@dataclass
class AnalysisRule:
    keyword: str  # エラー行に含まれていたら、このルールを使う判定文字列
    language_hint: str  # エラーの言語のヒント（例："Python", "Java"など）
    description: str  # エラーの簡易説明
    cause_candidate: str  # 原因候補
    check_point: str  # 確認ポイント
    hint_rule: (
        HintRule | None
    )  # 原因候補からさらに詳しい情報を抜き出すためのルール。なければNone
