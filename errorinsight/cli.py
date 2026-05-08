from errorinsight.clipboard import get_clipboard_text
from errorinsight.extractor import ErrorLine, extract_error_lines
from errorinsight.presenter import format_result


def main() -> None:
    clipboard_text = get_clipboard_text()
    error_lines: list[ErrorLine] = extract_error_lines(clipboard_text)
    result_lines: str = format_result(error_lines)
    print(result_lines)
