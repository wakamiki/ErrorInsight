# ErrorInsight

## 概要

ErrorInsight は、クリップボードから取得した複数行ログから怪しいエラー行を抽出し、エラー行から見て取れる範囲で簡易的な原因候補をCLI上に表示する学習用ツールです。

この Public repository では、無料版として公開する範囲を扱います。  
有料版の複雑な詳細分析機能は、Private repository で管理する予定です。

## 目的

このプロジェクトは、Python と CLI 開発の学習を目的とした開発プロジェクトです。

単に動くコードを作るだけでなく、以下の観点を重視します。

- 要件定義から実装までの開発プロセスを理解する
- 入力、抽出、表示の責務を分離する
- 保守しやすい構成を考える
- 小さい単位で実装と確認を進める
- 早い段階から自動テストを導入してテスト作成方法を学ぶ

## 無料版スコープ

この Public repository では、`01.00.00` の無料版完成を目標とします。

### できること

- クリップボードから複数行ログを取得する
- エラーらしいキーワードを含む行を抽出する
- 抽出した行をCLI上に表示する
- 元ログ上の行番号付きで表示する
- 抽出したエラー行ごとに簡易説明を表示する
- 抽出したエラー行ごとに原因候補を表示する
- よくある確認ポイントを表示する
- 判断できない場合は「不明」と表示する
- エラー行が見つからない場合に、そのことを表示する

### 扱わないこと

- クリップボード以外からのログ文字列取得
- エラー行から見て取れない複雑な原因推測
- コード全体や実行環境を踏まえた診断
- 修正コードの自動生成
- 言語ごとの切り替え機能
- エラー文ハイライト表示
- エラー件数集計
- エラー傾向分析
- GUI化
- データベース保存
- 外部AI API連携
- 課金処理
- ライセンス認証

## 有料版について

有料版では、無料版の簡易分析を超えた、より詳しい調査支援機能を提供する予定です。

有料版の具体的な仕様、複雑な分析ロジック、課金処理、ライセンス認証は Private repository で管理します。

有料版は `02.00.00` 以降として扱います。

## バージョン方針

ErrorInsight では、バージョンを `00.00.00` 形式で表記します。

- `00.50.00`: Version 0.5
- `01.00.00`: 無料版 Version 1
- `02.00.00`: 有料版 Version 2
- 小さな変更では一番右の数字を更新する
- 重要な機能追加では必ず右から3桁目である中央の数字を1つ上げる
- 例: `00.00.00` から重要な機能追加をした場合は `00.01.00` にする
- 大きな変更になるほど左側の数字を更新する

詳細な履歴は `docs/00_version-history.md` に記録します。

## 起動方法

無料版では、インストール済みCLIコマンドとして以下で起動できることを目指します。

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
説明: 値の変換に失敗した可能性があります。
原因候補: 数値に変換できない文字列をint()などに渡している可能性があります。
確認ポイント: 入力値、型変換前の文字列、空文字や想定外の値が入っていないかを確認してください。
```

エラー行が見つからない場合は、そのことをCLI上に表示します。

## 判定キーワード

無料版では、以下のようなキーワードを検出対象として想定します。

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
| `pyperclip` | クリップボード取得 | 無料版から使用する |
| `pytest` | 自動テスト | 無料版から使用する |
| `Typer` | CLI作成 | 必要になった段階で検討する |

## 実装方針

- この Public repository では無料版を完成させる
- 責務分離を学ぶため、処理ごとにファイルを分ける
- まずはクリップボード取得、エラー行抽出、簡易分析、表示までを実装する
- 最初から複雑なクラス設計にはせず、関数ベースで実装する
- 有料版の複雑な詳細分析機能は Private repository 側で扱う

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
│   ├── 00_version-history.md
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
| `docs/00_version-history.md` | バージョン表記ルール・履歴 |
| `docs/01_requirements.md` | 要件定義 |
| `docs/02_external-design.md` | 外部設計 |
| `docs/03_internal-design.md` | 内部設計 |
| `docs/04_implementation-plan.md` | 実装計画 |
| `docs/05_test-plan.md` | テスト計画 |
| `docs/06_retrospective.md` | 振り返り |
| `docs/07_daily-work-log.md` | 日次作業記録 |

## 開発上の注意

- Public repository には無料版として公開してよい内容だけを置く
- 有料版の複雑な分析ロジック、課金処理、ライセンス認証は置かない
- 不要なリファクタリングを行わない
- 大きな変更をまとめて入れない
- Python 初学者でも追いやすい実装を優先する
- 難解な書き方より、読みやすさを優先する
- 文章ファイルはUTF-8で作成・編集する
