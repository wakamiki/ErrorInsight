# 07 テスト仕様書

## 目的

ErrorInsight無料版の具体的なテストケースを定義する。

本書では、入力値、実行内容、期待結果を明確化し、手動テストおよび自動テストで確認できる状態を作る。

---

# TS-001 起動メッセージ表示

## 対象

- `format_startup_message`

## テスト内容

起動時メッセージを生成する。

## 入力

なし

## 実行

`format_startup_message()` を実行する。

## 期待結果

以下が含まれる。

```txt
ErrorInsight
動作モード: ローカル実行
外部通信: なし
```

---

# TS-002 空クリップボード

## 対象

* `cli.py`
* `format_clipboard_empty_message`

## テスト内容

クリップボードが空の場合の処理確認。

## 入力

空文字列

## 実行

CLIを起動する。

## 期待結果

空入力用メッセージを表示して終了する。

---

# TS-003 クリップボード読み取り失敗

## 対象

* `cli.py`
* `format_clipboard_read_error_message`

## テスト内容

クリップボード読み取り失敗時の処理確認。

## 入力

クリップボード取得例外

## 実行

`pyperclip.paste()` を失敗させる。

## 期待結果

読み取り失敗メッセージを表示して終了する。

---

# TS-004 通常文章入力

## 対象

* `extract_error_lines`
* `format_no_error_lines_message`

## テスト内容

通常の日本語文章入力時の確認。

## 入力

```txt
今日は良い天気です。
```

## 実行

CLIを起動する。

## 期待結果

エラー行なしメッセージを表示する。

---

# TS-005 error 行抽出

## 対象

* `extract_error_lines`

## テスト内容

`error` を含む行の抽出確認。

## 入力

```txt
normal line
error occurred
```

## 実行

`extract_error_lines()` を実行する。

## 期待結果

`error occurred` が抽出される。

---

# TS-006 exception 行抽出

## 対象

* `extract_error_lines`

## テスト内容

`exception` を含む行の抽出確認。

## 入力

```txt
NullPointerException
```

## 実行

`extract_error_lines()` を実行する。

## 期待結果

該当行が抽出される。

---

# TS-007 traceback 行抽出

## 対象

* `extract_error_lines`

## テスト内容

`traceback` を含む行の抽出確認。

## 入力

```txt
Traceback (most recent call last):
```

## 実行

`extract_error_lines()` を実行する。

## 期待結果

該当行が抽出される。

---

# TS-008 大文字小文字無視抽出

## 対象

* `extract_error_lines`

## テスト内容

大文字・小文字を区別しない抽出確認。

## 入力

```txt
ERROR
Error
error
```

## 実行

`extract_error_lines()` を実行する。

## 期待結果

すべて抽出される。

---

# TS-009 Python言語判定

## 対象

* `detect_language_hint`

## テスト内容

Pythonログの言語判定確認。

## 入力

```txt
Traceback (most recent call last):
AttributeError
```

## 実行

`detect_language_hint()` を実行する。

## 期待結果

```txt
Python
```

を返す。

---

# TS-010 Java言語判定

## 対象

* `detect_language_hint`

## テスト内容

Javaログの言語判定確認。

## 入力

```txt
Exception in thread
java.lang.NullPointerException
```

## 実行

`detect_language_hint()` を実行する。

## 期待結果

```txt
Java
```

を返す。

---

# TS-011 C#言語判定

## 対象

* `detect_language_hint`

## テスト内容

C#ログの言語判定確認。

## 入力

```txt
System.NullReferenceException
```

## 実行

`detect_language_hint()` を実行する。

## 期待結果

```txt
C#
```

を返す。

---

# TS-012 JavaScript言語判定

## 対象

* `detect_language_hint`

## テスト内容

JavaScriptログの言語判定確認。

## 入力

```txt
Uncaught TypeError
```

## 実行

`detect_language_hint()` を実行する。

## 期待結果

```txt
JavaScript
```

を返す。

---

# TS-013 SQL言語判定

## 対象

* `detect_language_hint`

## テスト内容

SQLログの言語判定確認。

## 入力

```txt
SQLSTATE syntax error
```

## 実行

`detect_language_hint()` を実行する。

## 期待結果

```txt
SQL
```

を返す。

---

# TS-014 unknown 判定

## 対象

* `decide_language_hint`

## テスト内容

スコア不足時の確認。

## 入力

```python
{
    "Python": 1,
    "Java": 0,
    "C#": 0,
    "JavaScript": 0,
    "SQL": 0,
}
```

## 実行

`decide_language_hint()` を実行する。

## 期待結果

```txt
不明
```

を返す。

---

# TS-015 同点判定

## 対象

* `decide_language_hint`

## テスト内容

最高点同点時の確認。

## 入力

```python
{
    "Python": 5,
    "Java": 5,
    "C#": 0,
    "JavaScript": 0,
    "SQL": 0,
}
```

## 実行

`decide_language_hint()` を実行する。

## 期待結果

```txt
不明
```

を返す。

---

# TS-016 強いヒント加点

## 対象

* `calculate_language_scores`

## テスト内容

強いヒントの加点確認。

## 入力

```txt
traceback (most recent call last):
```

## 実行

`calculate_language_scores()` を実行する。

## 期待結果

Pythonに `+5` 加点される。

---

# TS-017 弱いヒント加点

## 対象

* `calculate_language_scores`

## テスト内容

弱いヒントの加点確認。

## 入力

```txt
valueerror
```

## 実行

`calculate_language_scores()` を実行する。

## 期待結果

Pythonに `+1` 加点される。

---

# TS-018 組み合わせヒント加点

## 対象

* `calculate_language_scores`

## テスト内容

組み合わせヒント加点確認。

## 入力

```txt
traceback (most recent call last):
attributeerror
```

## 実行

`calculate_language_scores()` を実行する。

## 期待結果

Pythonに組み合わせヒント分 `+3` 加点される。

---

# TS-019 結果表示

## 対象

* `format_result`

## テスト内容

分析結果表示確認。

## 入力

簡易分析結果リスト

## 実行

`format_result()` を実行する。

## 期待結果

以下が表示される。

* 行番号
* エラー行
* 推定言語
* 簡易説明
* 原因候補
* 確認ポイント

---

# TS-020 複数エラー行表示

## 対象

* `format_result`

## テスト内容

複数エラー行表示確認。

## 入力

複数ErrorLine

## 実行

`format_result()` を実行する。

## 期待結果

すべてのエラー行が表示される。

---

# TS-021 エラー行なし表示

## 対象

* `format_no_error_lines_message`

## テスト内容

エラー行なしメッセージ確認。

## 入力

エラー行0件

## 実行

メッセージ生成関数を実行する。

## 期待結果

エラー行なしメッセージを返す。

---

# TS-022 手動CLI確認

## 対象

* CLI全体

## テスト内容

CLI実行確認。

## 入力

Python / Java / C# / JavaScript / SQL ログ

## 実行

```bash
errorinsight
```

または

```bash
ei
```

## 期待結果

* 起動メッセージが表示される
* 起動後にログをコピーして Enter で解析できる
* 続けて別ログをコピーして Enter で再解析できる
* コンソールを閉じるか、`q` + Enter で終了できる
* 言語判定できる
* 簡易分析できる
* 異常終了しない
