from dataclasses import dataclass


@dataclass(frozen=True)
class CombinationHint:
    keywords: tuple[str, ...]


SQL_STRONG_HINTS: tuple[str, ...] = (
    "sqlstate",
    "ora-",
    "relation does not exist",
    "no such table",
    "duplicate key value violates unique constraint",
    "duplicate key",
    "syntax error at or near",
    "unknown column",
    "access denied for user",
)

SQL_WEAK_HINTS: tuple[str, ...] = (
    "constraint",
    "syntax error",
    "permission denied",
    "error",
    "failed",
)

SQL_COMBINATION_HINTS: tuple[CombinationHint, ...] = (
    CombinationHint(keywords=("duplicate key", "constraint")),
    CombinationHint(keywords=("sqlstate", "constraint")),
    CombinationHint(keywords=("sqlstate", "syntax error")),
    CombinationHint(keywords=("access denied", "user")),
)

PYTHON_STRONG_HINTS: tuple[str, ...] = (
    "traceback (most recent call last):",
    '.py", line',
    "modulenotfounderror",
    "indentationerror",
    "attributeerror",
    "modulenotfounderror",
    "indentationerror",
    "unboundlocalerror",
    "unicodeencodeerror",
    "unicodedecodeerror",
)

PYTHON_WEAK_HINTS: tuple[str, ...] = (
    "valueerror",
    "typeerror",
    "nameerror",
    "indexerror",
    "keyerror",
    "importerror",
    "zerodivisionerror",
    "filenotfounderror",
    "permissionerror",
    "runtimeerror",
    "syntaxerror",
)

PYTHON_COMBINATION_HINTS: tuple[CombinationHint, ...] = (
    CombinationHint(keywords=("traceback (most recent call last):", "attributeerror")),
    CombinationHint(keywords=("traceback (most recent call last):", "valueerror")),
    CombinationHint(keywords=("traceback (most recent call last):", "typeerror")),
    CombinationHint(keywords=("traceback (most recent call last):", "nameerror")),
    CombinationHint(
        keywords=("traceback (most recent call last):", "modulenotfounderror")
    ),
    CombinationHint(keywords=("traceback (most recent call last):", '.py", line')),
    CombinationHint(keywords=('.py", line', "in <module>")),
)

JAVASCRIPT_STRONG_HINTS: tuple[str, ...] = (
    "uncaught",
    "cannot read properties",
    "cannot set properties",
    "is not a function",
    "uncaught (in promise)",
    "unhandledpromiserejection",
    "npm err!",
    "[vite]",
    "[vue warn]",
    "objects are not valid as a react child",
    "invalid hook call",
    "hydration failed",
    "enoent",
    "eaddrinuse",
    "econnrefused",
    "etimedout",
)

JAVASCRIPT_WEAK_HINTS: tuple[str, ...] = (
    "undefined",
    "referenceerror",
    "syntaxerror",
    "unexpected token",
    "unexpected end of input",
    "module not found",
    "failed prop type",
    "identifier has already been declared",
    "invalid dom property",
    "ng0",
)

JAVASCRIPT_COMBINATION_HINTS: tuple[CombinationHint, ...] = (
    CombinationHint(keywords=("uncaught", "typeerror")),
    CombinationHint(keywords=("uncaught", "referenceerror")),
    CombinationHint(keywords=("uncaught", "syntaxerror")),
    CombinationHint(keywords=("cannot read properties", "undefined")),
    CombinationHint(keywords=("cannot read properties", "null")),
    CombinationHint(keywords=("cannot set properties", "undefined")),
    CombinationHint(keywords=("npm err!", "enoent")),
    CombinationHint(keywords=("npm err!", "eaddrinuse")),
    CombinationHint(keywords=("npm err!", "econnrefused")),
    CombinationHint(keywords=("[vite]", "failed to resolve import")),
    CombinationHint(keywords=("[vue warn]", "component")),
    CombinationHint(keywords=("failed prop type", "react")),
    CombinationHint(keywords=("hydration failed", "server")),
    CombinationHint(keywords=("objects are not valid as a react child", "react")),
    CombinationHint(keywords=("invalid hook call", "hooks")),
    CombinationHint(keywords=("unexpected token", "json")),
)

JAVA_STRONG_HINTS: tuple[str, ...] = (
    "java.lang.",
    "java.io.",
    "java.util.",
    "java.sql.",
    "exception in thread",
    ".java:",
    "nullpointerexception",
    "classnotfoundexception",
    "nosuchmethoderror",
    "noclassdeffounderror",
    "unsupportedclassversionerror",
    "numberformatexception",
)

JAVA_WEAK_HINTS: tuple[str, ...] = (
    "runtimeexception",
    "illegalstateexception",
    "indexoutofboundsexception",
    "arrayindexoutofboundsexception",
    "stringindexoutofboundsexception",
    "classcastexception",
    "filenotfoundexception",
    "ioexception",
    "sqlexception",
    "parseexception",
    "securityexception",
    "assertionerror",
    "exception",
    "runtimeexception",
    "illegalargumentexception",
)

JAVA_COMBINATION_HINTS: tuple[CombinationHint, ...] = (
    CombinationHint(keywords=("exception in thread", "java.lang.")),
    CombinationHint(keywords=("exception in thread", "nullpointerexception")),
    CombinationHint(keywords=("java.lang.", "nullpointerexception")),
    CombinationHint(keywords=(".java:", "exception")),
    CombinationHint(keywords=(".java:", "at ")),
    CombinationHint(keywords=("caused by:", "java.lang.")),
    CombinationHint(keywords=("java.sql.", "sqlexception")),
    CombinationHint(keywords=("classnotfoundexception", "classpath")),
    CombinationHint(keywords=("noclassdeffounderror", "classpath")),
    CombinationHint(keywords=("unsupportedclassversionerror", "java runtime")),
)

CSHARP_STRONG_HINTS: tuple[str, ...] = (
    "system.",
    "microsoft.",
    ".cs:line",
    "nullreferenceexception",
    "invalidoperationexception",
    "argumentnullexception",
    "fileloadexception",
    "typeloadexception",
    "typeinitializationexception",
    "system.io.",
)

CSHARP_WEAK_HINTS: tuple[str, ...] = (
    "argumentexception",
    "indexoutofrangeexception",
    "filenotfoundexception",
    "directorynotfoundexception",
    "ioexception",
    "unauthorizedaccessexception",
    "invalidcastexception",
    "jsonexception",
    "sqlexception",
    "applicationexception",
    "systemexception",
    "xmlexception",
    "serializationexception",
)

CSHARP_COMBINATION_HINTS: tuple[CombinationHint, ...] = (
    CombinationHint(keywords=("system.", "nullreferenceexception")),
    CombinationHint(keywords=("system.", "invalidoperationexception")),
    CombinationHint(keywords=("system.", "argumentnullexception")),
    CombinationHint(keywords=(".cs:line", "exception")),
    CombinationHint(keywords=("at ", ".cs:line")),
    CombinationHint(keywords=("microsoft.", "exception")),
    CombinationHint(keywords=("system.io.", "filenotfoundexception")),
    CombinationHint(keywords=("system.text.json", "jsonexception")),
    CombinationHint(keywords=("typeinitializationexception", "inner exception")),
    CombinationHint(
        keywords=(
            "object reference not set to an instance of an object",
            "nullreferenceexception",
        )
    ),
)

LANGUAGE_PYTHON = "Python"
LANGUAGE_JAVA = "Java"
LANGUAGE_CSHARP = "C#"
LANGUAGE_JAVASCRIPT = "JavaScript"
LANGUAGE_SQL = "SQL"
LANGUAGE_UNKNOWN = "不明"

STRONG_HINT_SCORE = 5
WEAK_HINT_SCORE = 1
COMBINATION_HINT_SCORE = 3
MIN_LANGUAGE_SCORE = 3

# normalized_log は小文字化済みのログ本文を受け取る
def calculate_language_scores(normalized_log: str) -> dict[str, int]:
    # スコア計算
    language_scores: dict[str, int] = {
        LANGUAGE_PYTHON: 0,
        LANGUAGE_JAVA: 0,
        LANGUAGE_CSHARP: 0,
        LANGUAGE_JAVASCRIPT: 0,
        LANGUAGE_SQL: 0,
    }
    hint_maps = [
    (
        {
            LANGUAGE_SQL: SQL_STRONG_HINTS,
            LANGUAGE_PYTHON: PYTHON_STRONG_HINTS,
            LANGUAGE_JAVA: JAVA_STRONG_HINTS,
            LANGUAGE_CSHARP: CSHARP_STRONG_HINTS,
            LANGUAGE_JAVASCRIPT: JAVASCRIPT_STRONG_HINTS,
        },
        STRONG_HINT_SCORE,
    ),
    (
        {
            LANGUAGE_SQL: SQL_WEAK_HINTS,
            LANGUAGE_PYTHON: PYTHON_WEAK_HINTS,
            LANGUAGE_JAVA: JAVA_WEAK_HINTS,
            LANGUAGE_CSHARP: CSHARP_WEAK_HINTS,
            LANGUAGE_JAVASCRIPT: JAVASCRIPT_WEAK_HINTS,
        },
        WEAK_HINT_SCORE,
    ),
    ]
    for hint_map, score in hint_maps:
        for language, hints in hint_map.items():
            for keyword in hints:
                if keyword in normalized_log:
                    language_scores[language] += score

    combination_hint_map = {
            LANGUAGE_SQL: SQL_COMBINATION_HINTS,
            LANGUAGE_PYTHON: PYTHON_COMBINATION_HINTS,
            LANGUAGE_JAVA: JAVA_COMBINATION_HINTS,
            LANGUAGE_CSHARP: CSHARP_COMBINATION_HINTS,
            LANGUAGE_JAVASCRIPT: JAVASCRIPT_COMBINATION_HINTS,
        }

    for language, combination_hints in combination_hint_map.items():
        for combination_hint in combination_hints:
            if all(keyword in normalized_log for keyword in combination_hint.keywords):
                language_scores[language] += COMBINATION_HINT_SCORE

    return language_scores

def decide_language_hint(language_scores: dict[str, int]) -> str:
    # スコアからLANGUAGE_HINTを特定
    max_score = max(language_scores.values())

    if max_score < MIN_LANGUAGE_SCORE:
        return LANGUAGE_UNKNOWN

    top_languages = [
        language
        for language, score in language_scores.items()
        if score == max_score
    ]

    if len(top_languages) == 1:
        return top_languages[0]

    return LANGUAGE_UNKNOWN



def detect_language_hint(log: str) -> str:
    # エラー文から言語っぽさを推定する
    normalized_log = log.lower()
    language_scores = calculate_language_scores(normalized_log)
    return decide_language_hint(language_scores)
