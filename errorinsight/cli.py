from errorinsight.analyzer import (
    ErrorAnalysis,
    analyze_error_line,
    detect_language_hint,
)
from errorinsight.clipboard import get_clipboard_text
from errorinsight.extractor import ErrorLine, extract_error_lines
from errorinsight.presenter import format_result


def main() -> None:
    clipboard_text: str = get_clipboard_text()
    language_hint: str = detect_language_hint(clipboard_text)
    error_lines: list[ErrorLine] = extract_error_lines(clipboard_text)
    analysis_lines: list[ErrorAnalysis] = [
        analyze_error_line(error_line, language_hint) for error_line in error_lines
    ]
    result_lines: str = format_result(analysis_lines)
    print(result_lines)
