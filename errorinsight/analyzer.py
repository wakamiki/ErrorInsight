from dataclasses import dataclass

from errorinsight.analysis_rule import AnalysisRule
from errorinsight.analysis_rules import (
    COMMON_ANALYSIS_RULES,
    CSHARP_ANALYSIS_RULES,
    JAVA_ANALYSIS_RULES,
    JAVASCRIPT_ANALYSIS_RULES,
    PYTHON_ANALYSIS_RULES,
    SQL_ANALYSIS_RULES,
)
from errorinsight.extractor import ErrorLine


@dataclass
class ErrorAnalysis:
    error_line: ErrorLine
    language_hint: str  # エラーの言語のヒント（例："Python", "Java"など）
    description: str  # エラーの説明
    cause_candidate: str  # 原因の候補
    check_point: str  # 確認すべきポイント
    hint: str | None


SQL_LANGUAGE_HINT_KEYWORDS: tuple[str, ...] = (
    "sqlstate",
    "ora-",
    "duplicate key",
    "constraint",
    "relation does not exist",
    "no such table",
    "syntax error at or near",
    "unknown column",
    "access denied for user",
)

PYTHON_LANGUAGE_HINT_KEYWORDS: tuple[str, ...] = (
    "traceback (most recent call last):",
    '.py", line',
    "modulenotfounderror",
    "indentationerror",
    "valueerror",
    "attributeerror",
    "modulenotfounderror",
    "indentationerror",
    "unboundlocalerror",
    "unicodeencodeerror",
    "unicodedecodeerror",
)
JAVASCRIPT_LANGUAGE_HINT_KEYWORDS: tuple[str, ...] = (
    "uncaught",
    "cannot read properties",
    "undefined",
    ".js:",
    "cannot read properties",
    "cannot set properties",
    "is not a function",
    "uncaught (in promise)",
    "unhandledpromiserejection",
    "enoent",
    "eaddrinuse",
    "econnrefused",
)

JAVA_LANGUAGE_HINT_KEYWORDS: tuple[str, ...] = (
    "java.lang.",
    "java.io.",
    "exception in thread",
    ".java:",
    "nullpointerexception",
    "nullpointerexception",
    "classnotfoundexception",
    "nosuchmethoderror",
    "noclassdeffounderror",
    "unsupportedclassversionerror",
    "numberformatexception",
)

CSHARP_LANGUAGE_HINT_KEYWORDS: tuple[str, ...] = (
    "system.",
    ".cs:line",
    "nullreferenceexception",
    "invalidoperationexception",
    "nullreferenceexception",
    "argumentnullexception",
    "invalidoperationexception",
    "fileloadexception",
    "typeloadexception",
    "typeinitializationexception",
    "system.io.",
    "microsoft.",
)


def detect_language_hint(log: str) -> str:
    # エラー文から言語っぽさを推定する
    if any(keyword in log.lower() for keyword in SQL_LANGUAGE_HINT_KEYWORDS):
        return "SQL"
    elif any(keyword in log.lower() for keyword in PYTHON_LANGUAGE_HINT_KEYWORDS):
        return "Python"
    elif any(keyword in log.lower() for keyword in JAVA_LANGUAGE_HINT_KEYWORDS):
        return "Java"
    elif any(keyword in log.lower() for keyword in CSHARP_LANGUAGE_HINT_KEYWORDS):
        return "C#"
    elif any(keyword in log.lower() for keyword in JAVASCRIPT_LANGUAGE_HINT_KEYWORDS):
        return "JavaScript"
    else:
        return "不明"


def get_prioritized_rules(language_hint: str) -> list[AnalysisRule]:
    # 言語ヒントに応じて、先に見るルール一覧を決める
    if "SQL" == language_hint:
        return SQL_ANALYSIS_RULES + COMMON_ANALYSIS_RULES
    if "Python" == language_hint:
        return PYTHON_ANALYSIS_RULES + COMMON_ANALYSIS_RULES
    if "JavaScript" == language_hint:
        return JAVASCRIPT_ANALYSIS_RULES + COMMON_ANALYSIS_RULES
    if "Java" == language_hint:
        return JAVA_ANALYSIS_RULES + COMMON_ANALYSIS_RULES
    if "C#" == language_hint:
        return CSHARP_ANALYSIS_RULES + COMMON_ANALYSIS_RULES
    if "不明" == language_hint:
        return COMMON_ANALYSIS_RULES
    return COMMON_ANALYSIS_RULES


def extract_hint(rule: AnalysisRule, error_text: str) -> str | None:
    if rule.hint_rule is None:
        return None
    match = rule.hint_rule.pattern.search(error_text)
    if match is None:
        return None
    return rule.hint_rule.template.format(**match.groupdict())


def analyze_error_line(error_line: ErrorLine, language_hint: str) -> ErrorAnalysis:
    rules: list[AnalysisRule] = get_prioritized_rules(language_hint)
    for rule in rules:
        if rule.keyword in error_line.text.lower():
            result_check_point: str = rule.check_point
            hint = extract_hint(rule, error_line.text)
            return ErrorAnalysis(
                error_line=error_line,
                language_hint=language_hint,
                description=rule.description,
                cause_candidate=rule.cause_candidate,
                check_point=result_check_point,
                hint=hint,
            )
    return ErrorAnalysis(
        error_line=error_line,
        language_hint=language_hint,
        description="ErrorInsightでは、このエラー種別を判断できませんでした。",
        cause_candidate="不明",
        check_point="エラー行の前後や直前に変更したコードを確認してください。",
        hint=None,
    )


# 実際にルールを当てて ErrorAnalysis を返す
