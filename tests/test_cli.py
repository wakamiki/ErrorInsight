from errorinsight import cli


def test_main_shows_empty_clipboard_message(monkeypatch, capsys) -> None:
    monkeypatch.setattr(cli, "get_clipboard_text", lambda: "")
    inputs = iter(["", "q"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    cli.main()

    captured = capsys.readouterr()
    assert "ErrorInsight" in captured.out
    assert "クリップボードにログが見つかりませんでした。" in captured.out
    assert "ErrorInsight を終了します。" in captured.out


def test_main_shows_clipboard_read_error_message(monkeypatch, capsys) -> None:
    def raise_clipboard_error() -> str:
        raise RuntimeError("clipboard error")

    monkeypatch.setattr(cli, "get_clipboard_text", raise_clipboard_error)
    inputs = iter(["", "q"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    cli.main()

    captured = capsys.readouterr()
    assert "ErrorInsight" in captured.out
    assert "クリップボードを読み取れませんでした。" in captured.out


def test_main_shows_no_error_lines_message(monkeypatch, capsys) -> None:
    monkeypatch.setattr(cli, "get_clipboard_text", lambda: "今日は良い天気です。")
    inputs = iter(["", "q"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    cli.main()

    captured = capsys.readouterr()
    assert "ErrorInsight" in captured.out
    assert "エラーらしい行は見つかりませんでした。" in captured.out


def test_main_shows_analysis_result(monkeypatch, capsys) -> None:
    log = (
        "Traceback (most recent call last):\n"
        "AttributeError: 'NoneType' object has no attribute 'split'"
    )
    monkeypatch.setattr(cli, "get_clipboard_text", lambda: log)
    inputs = iter(["", "q"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    cli.main()

    captured = capsys.readouterr()
    assert "2行目" in captured.out
    assert "言語        : Python" in captured.out
    assert "説明        : 存在しない機能や値を使おうとした可能性があります。" in captured.out
    assert "ヒント      : " in captured.out


def test_main_can_run_twice_before_exit(monkeypatch, capsys) -> None:
    logs = iter(
        [
            "今日は良い天気です。",
            "Traceback (most recent call last):\n"
            "AttributeError: 'NoneType' object has no attribute 'split'",
        ]
    )
    inputs = iter(["", "", "q"])
    monkeypatch.setattr(cli, "get_clipboard_text", lambda: next(logs))
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    cli.main()

    captured = capsys.readouterr()
    assert "エラーらしい行は見つかりませんでした。" in captured.out
    assert "2行目" in captured.out
    assert "ErrorInsight を終了します。" in captured.out
