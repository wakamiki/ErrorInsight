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
    "uncaught",
    "unhandledpromiserejection",
    "cannot read properties",
    "cannot set properties",
    "is not a function",
    "module not found",
    "enoent",
    "eaddrinuse",
    "econnrefused",
    "etimedout",
    "npm err",
    "vite",
    "vue warn",
    "ng0",
    "failed prop type",
    "hydration failed",
    "invalid hook call",
    "invalid dom property",
    "objects are not valid as a react child",
    "sqlstate",
    "duplicate key",
    "constraint",
    "syntax error",
    "no such table",
    "unknown column",
    "column does not exist",
    "relation does not exist",
    "table already exists",
    "data too long",
    "invalid input syntax",
    "access denied for user",
    "password authentication failed",
    "ambiguous column",
    "cannot insert null",
    "invalid identifier",
    "ora-",
    "permission denied",
)


def extract_error_lines(log: str) -> list[ErrorLine]:
    error_lines: list[ErrorLine] = []
    log_lines: list[str] = log.splitlines()
    for line_number, line in enumerate(log_lines, start=1):
        normalized_line: str = line.lower()
        if any(keyword in normalized_line for keyword in ERROR_KEYWORDS):
            error_lines.append(ErrorLine(line_number=line_number, text=line))

    return error_lines
