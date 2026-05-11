from dataclasses import dataclass

from errorinsight.analysis_rule import AnalysisRule
from errorinsight.extractor import ErrorLine


@dataclass
class ErrorAnalysis:
    error_line: ErrorLine
    language_hint: str  # エラーの言語のヒント（例："Python", "Java"など）
    description: str  # エラーの説明
    cause_candidate: str  # 原因の候補
    check_point: str  # 確認すべきポイント

SQL_LANGUAGE_HINT_KEYWORDS: tuple[str, ...] = (
    "sqlstate",
    "ora-",
    "duplicate key",
    "constraint",
    "relation does not exist",
    "no such table",
    "syntax error at or near",
)

PYTHON_LANGUAGE_HINT_KEYWORDS: tuple[str, ...] = (
    "traceback (most recent call last):",
    '.py", line',
    "modulenotfounderror",
    "indentationerror",
    "valueerror",
)
JAVA_LANGUAGE_HINT_KEYWORDS: tuple[str, ...] = (
    "java.lang.",
    "java.io.",
    "exception in thread",
    ".java:",
    "nullpointerexception",
)

CSHARP_LANGUAGE_HINT_KEYWORDS: tuple[str, ...] = (
    "system.",
    ".cs:line",
    "nullreferenceexception",
    "invalidoperationexception",
)

JAVASCRIPT_LANGUAGE_HINT_KEYWORDS: tuple[str, ...] = (
    "uncaught",
    "cannot read properties",
    "undefined",
    ".js:",
)


def detect_language_hint(log: str) -> str:
    #エラー文から言語っぽさを推定する
    if any(keyword in log.lower() for keyword in SQL_LANGUAGE_HINT_KEYWORDS):
        return "SQL"
    elif any(keyword in log.lower() for keyword in PYTHON_LANGUAGE_HINT_KEYWORDS)   :
        return "Python"
    elif any(keyword in log.lower() for keyword in JAVA_LANGUAGE_HINT_KEYWORDS):
        return "Java"
    elif any(keyword in log.lower() for keyword in CSHARP_LANGUAGE_HINT_KEYWORDS):
        return "C#"
    elif any(keyword in log.lower() for keyword in JAVASCRIPT_LANGUAGE_HINT_KEYWORDS):
        return "JavaScript"
    else:
        return "不明"

def get_prioritized_rules(error_line: ErrorLine) -> list[AnalysisRule]:
    # 言語ヒントに応じて、先に見るルール一覧を決める
    return []

def analyze_error_line(error_line: ErrorLine, language_hint: str) -> ErrorAnalysis:
    if "valueerror" in error_line.text.lower():
        return ErrorAnalysis(
            error_line=error_line,
            language_hint=language_hint,
            description=VALUE_ERROR_DESCRIPTION,
            cause_candidate=VALUE_ERROR_CAUSE_CANDIDATE,
            check_point=VALUE_ERROR_CHECK_POINT,
        )
    return ErrorAnalysis(
        error_line=error_line,
        language_hint=language_hint,
        description="ErrorInsightでは、このエラー種別を判断できませんでした。",
        cause_candidate="不明",
        check_point="エラー行の前後や直前に変更したコードを確認してください。",
    )
#実際にルールを当てて ErrorAnalysis を返す
