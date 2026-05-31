from errorinsight.language_detector import (
    COMBINATION_HINT_SCORE,
    LANGUAGE_CSHARP,
    LANGUAGE_JAVA,
    LANGUAGE_JAVASCRIPT,
    LANGUAGE_PYTHON,
    LANGUAGE_SQL,
    LANGUAGE_UNKNOWN,
    STRONG_HINT_SCORE,
    WEAK_HINT_SCORE,
    calculate_language_scores,
    decide_language_hint,
    detect_language_hint,
)


def test_detect_language_hint_returns_python() -> None:
    log: str = (
        "Traceback (most recent call last):\n"
        "AttributeError: 'NoneType' object has no attribute 'split'"
    )

    result: str = detect_language_hint(log)

    assert result == LANGUAGE_PYTHON


def test_detect_language_hint_returns_java() -> None:
    log: str = (
        'Exception in thread "main" java.lang.NullPointerException: '
        'Cannot invoke "User.getName()" because "user" is null'
    )

    result: str = detect_language_hint(log)

    assert result == LANGUAGE_JAVA


def test_detect_language_hint_returns_csharp() -> None:
    log: str = (
        "System.NullReferenceException: "
        "Object reference not set to an instance of an object."
    )

    result: str = detect_language_hint(log)

    assert result == LANGUAGE_CSHARP


def test_detect_language_hint_returns_javascript() -> None:
    log: str = "Uncaught TypeError: Cannot read properties of undefined"

    result: str = detect_language_hint(log)

    assert result == LANGUAGE_JAVASCRIPT


def test_detect_language_hint_returns_sql() -> None:
    log: str = "SQLSTATE[42S02]: relation does not exist"

    result: str = detect_language_hint(log)

    assert result == LANGUAGE_SQL


def test_detect_language_hint_prioritizes_java_for_java_file_error() -> None:
    log: str = "java.io.FileNotFoundException: config.yml"

    result: str = detect_language_hint(log)

    assert result == LANGUAGE_JAVA


def test_detect_language_hint_prioritizes_csharp_for_system_io_error() -> None:
    log: str = "System.IO.FileNotFoundException: config.yml"

    result: str = detect_language_hint(log)

    assert result == LANGUAGE_CSHARP


def test_detect_language_hint_prioritizes_javascript_for_uncaught_reference_error() -> None:
    log: str = "Uncaught ReferenceError: user is not defined"

    result: str = detect_language_hint(log)

    assert result == LANGUAGE_JAVASCRIPT


def test_decide_language_hint_returns_unknown_when_score_is_low() -> None:
    language_scores: dict[str, int] = {
        LANGUAGE_PYTHON: WEAK_HINT_SCORE,
        LANGUAGE_JAVA: 0,
        LANGUAGE_CSHARP: 0,
        LANGUAGE_JAVASCRIPT: 0,
        LANGUAGE_SQL: 0,
    }

    result: str = decide_language_hint(language_scores)

    assert result == LANGUAGE_UNKNOWN


def test_decide_language_hint_returns_unknown_when_score_is_tied() -> None:
    language_scores: dict[str, int] = {
        LANGUAGE_PYTHON: STRONG_HINT_SCORE,
        LANGUAGE_JAVA: STRONG_HINT_SCORE,
        LANGUAGE_CSHARP: 0,
        LANGUAGE_JAVASCRIPT: 0,
        LANGUAGE_SQL: 0,
    }

    result: str = decide_language_hint(language_scores)

    assert result == LANGUAGE_UNKNOWN


def test_calculate_language_scores_adds_strong_hint_score() -> None:
    scores: dict[str, int] = calculate_language_scores(
        "traceback (most recent call last):"
    )

    assert scores[LANGUAGE_PYTHON] == STRONG_HINT_SCORE


def test_calculate_language_scores_adds_weak_hint_score() -> None:
    scores: dict[str, int] = calculate_language_scores("valueerror")

    assert scores[LANGUAGE_PYTHON] == WEAK_HINT_SCORE


def test_calculate_language_scores_adds_combination_hint_score() -> None:
    scores: dict[str, int] = calculate_language_scores(
        "traceback (most recent call last):\nattributeerror"
    )

    assert scores[LANGUAGE_PYTHON] == STRONG_HINT_SCORE * 2 + COMBINATION_HINT_SCORE
