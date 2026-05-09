from errorinsight.extractor import ErrorLine, extract_error_lines


def test_extract_error_lines_returns_single_error_line():
    log: str = "Start\nValueError: invalid literal\nEnd"
    result: list[ErrorLine] = extract_error_lines(log)
    assert len(result) == 1
    assert result[0].line_number == 2
    assert result[0].text == "ValueError: invalid literal"


def test_extract_error_lines_returns_multiple_error_lines():
    log_lines: str = (
        "ERROR failed to connect\nnormal log\nFileNotFoundException: file missing\n"
    )
    result: list[ErrorLine] = extract_error_lines(log_lines)
    assert len(result) == 2
    assert result[0].line_number == 1
    assert result[0].text == "ERROR failed to connect"
    assert result[1].line_number == 3
    assert result[1].text == "FileNotFoundException: file missing"


def test_extract_error_lines_returns_empty_list_when_no_error():
    log_no_error: str = "Start\nLoading\nFinished"
    result: list[ErrorLine] = extract_error_lines(log_no_error)
    assert len(result) == 0


def test_extract_error_lines_matches_uppercase_error():
    log_uppercase: str = "ERROR failed to connect\n"
    result: list[ErrorLine] = extract_error_lines(log_uppercase)
    assert len(result) == 1
    assert result[0].line_number == 1
    assert result[0].text == "ERROR failed to connect"
