# Implementation Plan

## 実装方針

- この Public repository では無料版を実装する
- 無料版完成を `01.00.00` として扱う
- 有料版は `02.00.00` 以降として Private repository で扱う
- 責務分離を学ぶため、処理ごとにファイルを分けて実装する
- まずはクリップボード取得、エラー行抽出、コンソール表示までを実装する
- 最初から複雑なクラス設計にはせず、関数ベースで実装する
- 各ファイルは1つの責務に集中させる
- 有料版の詳細分析機能は Public repository では実装しない
- クリップボード取得には `pyperclip` を使用する
- 自動テストには `pytest` を使用する
- CLIフレームワークは無料版では必須にせず、必要になった段階で `Typer` の導入を検討する

## 使用予定ライブラリ

| ライブラリ | 用途 | 採用理由 |
|---|---|---|
| `pyperclip` | クリップボード取得 | 無料版の入力元がクリップボードのため |
| `pytest` | 自動テスト | 抽出・表示処理のテスト作成方法を学ぶため |
| `Typer` | CLI作成 | 将来、オプションやヘルプ表示を整えるため |

### 無料版での扱い

- `pyperclip` と `pytest` は無料版から使用する
- `Typer` は無料版では保留し、標準的なエントリーポイント設定で `errorinsight` コマンド起動を実現する

## 実装順序

### 無料版

1. Pythonパッケージ構成を作る
2. `errorinsight` コマンドで起動できる設定を作る
3. クリップボードから文字列を取得する
4. ログ文字列からエラー候補行を抽出する
5. 抽出結果をコンソールに表示する
6. エラーなしの場合の表示を確認する
7. 自動テストを追加する

### バージョン目安

- `00.10.00`: CLI最小起動
- `00.20.00`: クリップボード取得
- `00.50.00`: クリップボード取得とエラー行抽出の接続
- `01.00.00`: 無料版完成

### 有料版

有料版は Private repository 側で実装する。
Public repository では、具体的な分析ロジックや課金処理を扱わない。

## タスク分解

### 1. パッケージ構成の作成

- `errorinsight/` ディレクトリを作成する
- `__init__.py` を作成する
- `__main__.py` を作成する

### 2. CLI起動設定

- `pyproject.toml` を作成する
- `errorinsight` コマンドで起動できるようにする
- 短縮コマンド `ei` でも起動できるようにする
- `errorinsight` 実行時に `cli.main` が呼ばれるようにする

### 3. クリップボード取得

- `clipboard.py` にクリップボード取得処理を実装する
- 取得できた文字列を `cli.py` に返す
- 空の場合の扱いを確認する

### 4. エラー行抽出

- `extractor.py` に `ErrorLine` を定義する
- `extractor.py` に判定キーワードを定義する
- ログ文字列を行単位で確認する
- キーワードを含む行を `list[ErrorLine]` として行番号付きで返す

### 5. 表示処理

- `presenter.py` に表示用文字列の整形処理を実装する
- エラー行がある場合の表示を作る
- エラー行がない場合の表示を作る

### 6. 自動テスト

- `tests/test_extractor.py` を作成する
- `tests/test_presenter.py` を作成する
- 入力と出力が明確な処理からテストする

## 変更対象ファイル

| ファイル | 責務 |
|---|---|
| `pyproject.toml` | `errorinsight` コマンドとして起動できる設定 |
| `errorinsight/__init__.py` | Pythonパッケージとして扱うためのファイル |
| `errorinsight/__main__.py` | `python -m errorinsight` 実行時の入口 |
| `errorinsight/cli.py` | CLI全体の処理順を制御する |
| `errorinsight/clipboard.py` | クリップボードからログ文字列を取得する |
| `errorinsight/extractor.py` | ログ文字列からエラー候補行を抽出する |
| `errorinsight/presenter.py` | CLI表示用の文字列を組み立てる |
| `tests/test_extractor.py` | 抽出処理の自動テスト |
| `tests/test_presenter.py` | 表示整形処理の自動テスト |

## 動作確認方法

### 無料版

- クリップボードに複数行ログをコピーする
- `errorinsight` を実行する
- エラーらしい行だけが表示されることを確認する
- 元ログ上の行番号が表示されることを確認する
- エラー行がない場合に、見つからなかったことが表示されることを確認する
- `pytest` で抽出処理と表示処理の自動テストが通ることを確認する

## 注意点

- Public repository では有料版の詳細分析機能を実装しない
- `cli.py` に抽出ルールを直接書かない
- `extractor.py` は表示用文字列を作らない
- `presenter.py` は `print` せず、表示用文字列を返す
- 変更は小さい単位で行い、動作確認しながら進める
- 有料版の具体的な仕様は `docs/docs-local/pro-feature-scope.md` に退避し、Private repository で扱う
