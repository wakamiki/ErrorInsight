from errorinsight.extractor import ErrorLine
from errorinsight.presenter import format_result


def test_format_result_with_error_line() -> None:
    error_lines: list[ErrorLine] = [
        ErrorLine(line_number=1, text="SyntaxError: invalid syntax"),
    ]
    result: str = format_result(error_lines)
    assert result == " 1行目: SyntaxError: invalid syntax"
    assert not result.endswith("\n")


def test_format_result_with_error_lines() -> None:
    error_lines: list[ErrorLine] = [
        ErrorLine(line_number=1, text="SyntaxError: invalid syntax"),
        ErrorLine(line_number=5, text="NameError: name 'x' is not defined"),
    ]
    result: str = format_result(error_lines)
    assert (
        result
        == " 1行目: SyntaxError: invalid syntax\n 5行目: NameError: name 'x' is not defined"
    )
    assert not result.endswith("\n")


def test_format_result_with_no_error_line() -> None:
    error_lines: list[ErrorLine] = []
    result: str = format_result(error_lines)
    assert result == "エラーらしい行は見つかりませんでした。"
    assert not result.endswith("\n")
