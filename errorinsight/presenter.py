from wcwidth import wcswidth

from errorinsight.analyzer import ErrorAnalysis

LABEL_WIDTH = 12


def display_width(text: str) -> int:
    word_width = wcswidth(text)
    if word_width == -1:
        return len(text)
    return word_width


def pad_label(label: str, width: int) -> str:
    label_width = display_width(label)
    padding_size = width - label_width
    return label + " " * padding_size


def format_result(analysis_lines: list[ErrorAnalysis]) -> str:
    if not analysis_lines:
        return "エラーらしい行は見つかりませんでした。"
    result_lines: list[str] = []
    for analysis_line in analysis_lines:
        result_lines.append("")
        result_lines.append(
            pad_label(f"{analysis_line.error_line.line_number}行目", LABEL_WIDTH)
            + ": "
            + analysis_line.error_line.text
        )
        result_lines.append(pad_label("言語", LABEL_WIDTH) + ": " + analysis_line.language_hint)
        result_lines.append(
            pad_label("説明", LABEL_WIDTH) + ": " + analysis_line.description
        )
        result_lines.append(
            pad_label("原因候補", LABEL_WIDTH) + ": " + analysis_line.cause_candidate
        )
        result_lines.append(
            pad_label("確認ポイント", LABEL_WIDTH) + ": " + analysis_line.check_point
        )
        if analysis_line.hint is not None:
            result_lines.append(
                pad_label("ヒント",LABEL_WIDTH) + ": " + analysis_line.hint
            )
    return "\n".join(result_lines)
