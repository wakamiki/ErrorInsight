from dataclasses import dataclass


@dataclass
class ErrorLine:
    line_number: int
    text: str


ERROR_KEYWORDS: tuple[str, ...] = (
    "error",
    "exception",
    "traceback",
    "failed",
    "fatal",
    "nullpointerexception",
    "nullreferenceexception",
    "valueerror",
    "typeerror",
    "nameerror",
    "indexerror",
    "keyerror",
    "importerror",
    "zerodivisionerror",
    "illegalargumentexception",
    "numberformatexception",
    "indexoutofboundsexception",
    "indexoutofrangeexception",
    "filenotfoundexception",
    "ioexception",
    "invalidoperationexception",
)


def extract_error_lines(log: str) -> list[ErrorLine]:
    error_lines: list[ErrorLine] = []
    log_lines: list[str] = log.splitlines()
    for line_number, line in enumerate(log_lines, start=1):
        normalized_line: str = line.lower()
        if any(keyword in normalized_line for keyword in ERROR_KEYWORDS):
            error_lines.append(ErrorLine(line_number=line_number, text=line))

    return error_lines
