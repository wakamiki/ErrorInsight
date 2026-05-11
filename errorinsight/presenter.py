from errorinsight.analyzer import ErrorAnalysis


def format_result(analysis_lines: list[ErrorAnalysis]) -> str:
    if not analysis_lines:
        return "エラーらしい行は見つかりませんでした。"
    result_lines: list[str] = []
    for analysis_line in analysis_lines:
        result_lines.append(
            f" {analysis_line.error_line.line_number}行目: {analysis_line.error_line.text}"
        )
        result_lines.append(f"説明: {analysis_line.description}")
        result_lines.append(f"原因候補: {analysis_line.cause_candidate}")
        result_lines.append(f"確認ポイント: {analysis_line.check_point}")
    return "\n".join(result_lines)
