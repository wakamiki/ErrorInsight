from errorinsight.extractor import ErrorLine


def format_result(error_lines: list[ErrorLine]) -> str:
    if not error_lines:
        return "エラーらしい行は見つかりませんでした。"
    result_lines: list[str] = []
    for error_line in error_lines:
        result_lines.append(f" {error_line.line_number}行目: {error_line.text}")
    return "\n".join(result_lines)
