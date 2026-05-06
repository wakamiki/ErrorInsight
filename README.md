# ErrorInsight

## 概要

ErrorInsight は、クリップボードから取得した複数行ログから怪しいエラー行を抽出し、原因候補をCLI上に表示する学習用ツールです。

v1では、Python / Java / C# の代表的なエラー行を対象に、例外名やエラーキーワードに基づくルールベースの原因候補推測を行います。

## 目的

このプロジェクトは、Python と CLI 開発の学習を目的とした開発プロジェクトです。

単に動くコードを作るだけでなく、以下の観点を重視します。

- 要件定義から実装までの開発プロセスを理解する
- 入力、抽出、分析、表示の責務を分離する
- 保守しやすい構成を考える
- 小さい単位で実装と確認を進める
- 早い段階から自動テストを導入してテスト作成方法を学ぶ

## v1スコープ

### v0.5

- クリップボードから複数行ログを取得する
- エラーらしいキーワードを含む行を抽出する
- 抽出した行をCLI上に表示する

### v1

- 抽出したエラー行ごとに原因候補を表示する
- Python / Java / C# の代表的なエラーに対応する
- 判断できない場合は「不明」として表示する
- 元ログ上の行番号付きで抽出結果を表示する

### v1で扱わないこと

- クリップボード以外からのログ文字列取得
- Java / C# / Python 以外のエラー文対応
- 言語ごとの切り替え機能
- エラー文ハイライト表示
- エラー件数集計
- エラー傾向分析
- GUI化
- データベース保存
- 外部AI API連携

## 起動方法

v1では、インストール済みCLIコマンドとして以下で起動できることを完了条件とします。

```bash
errorinsight
```

開発中の確認用として、将来的に以下の起動も想定します。

```bash
python -m errorinsight
```

## 想定出力

```text
=== ErrorInsight Result ===

[1] Line 12
Error:
ValueError: invalid literal for int() with base 10: 'abc'

Cause Candidate:
数値に変換できない文字列を int() に渡している可能性があります。
```

エラー行が見つからない場合は、そのことをCLI上に表示します。

## 判定キーワード

v1では、以下のようなキーワードを検出対象として想定します。

- `error`
- `exception`
- `traceback`
- `failed`
- `fatal`
- `nullpointerexception`
- `nullreferenceexception`
- `valueerror`
- `typeerror`
- `nameerror`
- `indexerror`
- `keyerror`
- `importerror`
- `zerodivisionerror`
- `filenotfoundexception`
- `ioexception`
- `invalidoperationexception`

キーワードの追加や調整は、処理の中に直接散らばらせず、変更しやすい形を意識します。

## 使用予定ライブラリ

| ライブラリ | 用途 | 方針 |
| --- | --- | --- |
| `pyperclip` | クリップボード取得 | v0.5から使用する |
| `pytest` | 自動テスト | v0.5から使用する |
| `Typer` | CLI作成 | v1では保留し、必要になった段階で検討する |

## 実装方針

- 責務分離を学ぶため、処理ごとにファイルを分ける
- まずは v0.5 として、クリップボード取得、エラー行抽出、表示までを実装する
- v0.5 が確認できてから、v1 の原因候補推測を追加する
- 最初から複雑なクラス設計にはせず、関数ベースで実装する
- 外部AI API連携は v1 では実装せず、将来拡張として扱う

## 想定ディレクトリ構成

```text
ErrorInsight/
├── errorinsight/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── clipboard.py
│   ├── extractor.py
│   ├── analyzer.py
│   └── presenter.py
├── tests/
│   ├── test_extractor.py
│   ├── test_analyzer.py
│   └── test_presenter.py
├── docs/
│   ├── 01_requirements.md
│   ├── 02_external-design.md
│   ├── 03_internal-design.md
│   ├── 04_implementation-plan.md
│   ├── 05_test-plan.md
│   ├── 06_retrospective.md
│   └── 07_daily-work-log.md
├── pyproject.toml
├── .gitignore
├── AGENTS.md
└── README.md
```

## セットアップ

現時点では、実装前のためセットアップ手順は未確定です。

Python パッケージ構成と `pyproject.toml` を追加した段階で、インストール方法、実行方法、テスト実行方法を追記します。

## テスト方針

- 早い段階から `pytest` による自動テストを導入する
- まずは入力と出力が明確な処理からテストする
- 優先対象は `extractor.py`、`analyzer.py`、`presenter.py`
- クリップボード取得やCLIコマンド起動は、最初は手動テストで確認する

## ドキュメント

| ファイル | 役割 |
| --- | --- |
| `docs/01_requirements.md` | 要件定義 |
| `docs/02_external-design.md` | 外部設計 |
| `docs/03_internal-design.md` | 内部設計 |
| `docs/04_implementation-plan.md` | 実装計画 |
| `docs/05_test-plan.md` | テスト計画 |
| `docs/06_retrospective.md` | 振り返り |
| `docs/07_daily-work-log.md` | 日次作業記録 |

## 開発上の注意

- v1 の範囲を事前合意なく広げない
- 不要なリファクタリングを行わない
- 大きな変更をまとめて入れない
- Python 初学者でも追いやすい実装を優先する
- 難解な書き方より、読みやすさを優先する
- 文章ファイルはUTF-8で作成・編集する
