from errorinsight.analyzer import ErrorAnalysis
from errorinsight.extractor import ErrorLine
from errorinsight.presenter import (
    format_clipboard_empty_message,
    format_clipboard_read_error_message,
    format_exit_message,
    format_loop_prompt,
    format_no_error_lines_message,
    format_result,
    format_startup_message,
)


def test_format_startup_message() -> None:
    result: str = format_startup_message()
    assert result == "ErrorInsight\n動作モード: ローカル実行\n外部通信: なし"


def test_format_clipboard_empty_message() -> None:
    result: str = format_clipboard_empty_message()
    assert (
        result
        == "クリップボードにログが見つかりませんでした。エラーログをコピーしてから Enter を押してください。"
    )


def test_format_clipboard_read_error_message() -> None:
    result: str = format_clipboard_read_error_message()
    assert (
        result
        == "クリップボードを読み取れませんでした。ログをコピーしてから Enter を押してください。"
    )


def test_format_loop_prompt() -> None:
    result: str = format_loop_prompt()
    assert result == "ログをコピーして Enter を押してください。終了する場合は q を入力して Enter を押してください。"


def test_format_exit_message() -> None:
    result: str = format_exit_message()
    assert result == "ErrorInsight を終了します。"


def test_format_no_error_lines_message() -> None:
    result: str = format_no_error_lines_message()
    assert result == "エラーらしい行は見つかりませんでした。"


def test_format_result_with_no_error_line() -> None:
    analysis_lines: list[ErrorAnalysis] = []
    result: str = format_result(analysis_lines)
    assert result == "エラーらしい行は見つかりませんでした。"
    assert not result.endswith("\n")


def test_format_result_with_error_line() -> None:
    analysis_lines: list[ErrorAnalysis] = [
        ErrorAnalysis(
            error_line=ErrorLine(line_number=1, text="SyntaxError: invalid syntax"),
            language_hint="不明",
            description="不明なエラーです。",
            cause_candidate="不明",
            check_point="エラー行の前後を確認してください。",
            hint=None,
        ),
    ]
    result: str = format_result(analysis_lines)
    assert (
        result == "\n1行目       : SyntaxError: invalid syntax\n"
        "言語        : 不明\n"
        "説明        : 不明なエラーです。\n"
        "原因候補    : 不明\n"
        "確認ポイント: エラー行の前後を確認してください。"
    )
    assert not result.endswith("\n")


def test_format_result_with_error_lines() -> None:
    analysis_lines: list[ErrorAnalysis] = [
        ErrorAnalysis(
            error_line=ErrorLine(line_number=1, text="SyntaxError: invalid syntax"),
            language_hint="不明",
            description="不明なエラーです。",
            cause_candidate="不明",
            check_point="エラー行の前後を確認してください。",
            hint=None,
        ),
        ErrorAnalysis(
            error_line=ErrorLine(
                line_number=5, text="NameError: name 'x' is not defined"
            ),
            language_hint="Python",
            description="名前が見つからないエラーです。",
            cause_candidate="変数名や関数名が定義されていない可能性があります。",
            check_point="名前のスペルや定義位置を確認してください。",
            hint=None,
        ),
    ]
    result: str = format_result(analysis_lines)
    assert (
        result == "\n1行目       : SyntaxError: invalid syntax\n"
        "言語        : 不明\n"
        "説明        : 不明なエラーです。\n"
        "原因候補    : 不明\n"
        "確認ポイント: エラー行の前後を確認してください。\n"
        "\n5行目       : NameError: name 'x' is not defined\n"
        "言語        : Python\n"
        "説明        : 名前が見つからないエラーです。\n"
        "原因候補    : 変数名や関数名が定義されていない可能性があります。\n"
        "確認ポイント: 名前のスペルや定義位置を確認してください。"
    )
    assert not result.endswith("\n")
