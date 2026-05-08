from errorinsight.clipboard import get_clipboard_text
from errorinsight.extractor import ErrorLine, extract_error_lines


def main() -> None:
    clipboard_text = get_clipboard_text()
    error_lines: list[ErrorLine] = extract_error_lines(clipboard_text)

    for error_line in error_lines:
        print(f"Line {error_line.line_number}: {error_line.text}")
