from dataclasses import dataclass

from errorinsight.extractor import ErrorLine


@dataclass
class ErrorAnalysis:
    error_line: ErrorLine
    description: str
    cause_candidate: str
    check_point: str