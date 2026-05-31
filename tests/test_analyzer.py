from errorinsight.analysis_rules import PYTHON_ANALYSIS_RULES
from errorinsight.analyzer import analyze_error_line, extract_hint
from errorinsight.extractor import ErrorLine


def test_analyze_error_line_returns_python_attribute_error_analysis() -> None:
    error_line = ErrorLine(
        line_number=2,
        text="AttributeError: 'NoneType' object has no attribute 'split'",
    )

    result = analyze_error_line(error_line, "Python")

    assert result.language_hint == "Python"
    assert result.description == "存在しない機能や値を使おうとした可能性があります。"
    assert result.cause_candidate == "メソッド名や属性名の間違い、None参照、型違いの可能性があります。"
    assert result.check_point == "対象オブジェクトの型、属性名・メソッド名、Noneになっていないかを確認してください。"
    assert result.hint is not None
    assert "NoneType" in result.hint
    assert "split" in result.hint


def test_analyze_error_line_returns_unknown_analysis_when_no_rule_matches() -> None:
    error_line = ErrorLine(line_number=1, text="UnknownCriticalProblem")

    result = analyze_error_line(error_line, "Python")

    assert result.language_hint == "Python"
    assert result.description == "ErrorInsightでは、このエラー種別を判断できませんでした。"
    assert result.cause_candidate == "不明"
    assert result.check_point == "エラー行の前後や直前に変更したコードを確認してください。"
    assert result.hint is None


def test_extract_hint_returns_hint_when_pattern_matches() -> None:
    rule = next(rule for rule in PYTHON_ANALYSIS_RULES if rule.keyword == "attributeerror")

    result = extract_hint(
        rule,
        "AttributeError: 'NoneType' object has no attribute 'split'",
    )

    assert result is not None
    assert "NoneType" in result
    assert "split" in result


def test_extract_hint_returns_none_when_pattern_does_not_match() -> None:
    rule = next(rule for rule in PYTHON_ANALYSIS_RULES if rule.keyword == "attributeerror")

    result = extract_hint(rule, "AttributeError")

    assert result is None
