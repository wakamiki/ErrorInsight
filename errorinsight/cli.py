from errorinsight.analyzer import (
    ErrorAnalysis,
    analyze_error_line,
)
from errorinsight.clipboard import get_clipboard_text
from errorinsight.extractor import ErrorLine, extract_error_lines
from errorinsight.presenter import (
    format_clipboard_empty_message,
    format_clipboard_read_error_message,
    format_result,
    format_startup_message,
)
from errorinsight.language_detector import detect_language_hint


def main() -> None:
    print(format_startup_message())
    try:
        clipboard_text: str = get_clipboard_text()
    except Exception:
        print(format_clipboard_read_error_message())
        return

    if not clipboard_text.strip():
        print(format_clipboard_empty_message())
        return

    language_hint: str = detect_language_hint(clipboard_text)
    error_lines: list[ErrorLine] = extract_error_lines(clipboard_text)
    analysis_lines: list[ErrorAnalysis] = [
        analyze_error_line(error_line, language_hint) for error_line in error_lines
    ]
    result_lines: str = format_result(analysis_lines)
    print(result_lines)
