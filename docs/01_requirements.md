# Requirements

## システム名

ErrorInsight
(エラーログ抽出CLIツール)

## 目的

Python / Java / C# のエラーログから怪しいエラー行を抽出し、確認しやすくする。
あわせて、Python・CLIアプリ開発・設計分離・テスト作成の学習を目的とする。

## 背景

学習や開発中に発生するエラーログは、そのままでは見づらく、読むべき箇所が分かりづらい。
そのため、ログからエラーらしい行を抽出し、行番号付きで確認できるツールを作成する。

## リポジトリ方針

### Public repository

この repository では、無料版として公開してよい機能を扱う。

### Private repository

有料版の具体的な分析ロジック、課金処理、ライセンス認証、外部AI API連携は Private repository で管理する。

## 無料版スコープ

### 無料版の主目的

クリップボード内の Python / Java / C# のログから、よくあるエラー文を高速に拾い、エラー行のみをCLI上に表示する。

### 無料版でできること

- クリップボード内の複数行ログを取得できる
- エラーらしいキーワードを含む行を抽出できる
- 抽出した行をCLI上に表示できる
- 元ログ上の行番号を表示できる
- エラー行が見つからない場合に、そのことを表示できる

### 無料版でやらないこと

- クリップボード以外からのログ文字列の取得
- 原因候補の詳細表示
- Java / C# / Python 以外のエラー文対応
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

有料版では、抽出したエラー行に対する原因候補表示や、より詳しい調査支援機能を提供する予定。
有料版の詳細仕様と実装は Private repository で管理する。

## 無料版で扱うログの前提

- 複数行のテキストログを対象とする
- 入力された文字列を1行ずつ確認する
- 大文字・小文字の違いは区別せずに判定する

## 無料版の判定ルール

* error
* exception
* traceback
* failed
* fatal
* nullpointerexception
* nullreferenceexception
* valueerror
* typeerror
* nameerror
* indexerror
* keyerror
* importerror
* zerodivisionerror
* illegalargumentexception
* numberformatexception
* indexoutofboundsexception
* indexoutofrangeexception
* filenotfoundexception
* ioexception
* invalidoperationexception

## 無料版の出力形式

- 抽出した行をCLI上に表示する
- 元ログ上の行番号を表示する
- 該当行がない場合は、見つからなかったことを表示する

## 無料版の完了条件

- クリップボードにコピーした複数行ログを読み込める
- Python / Java / C# の代表的なエラー行を抽出できる
- 抽出したエラー行を元ログの行番号付きで表示できる
- エラー行が見つからない場合は、そのことを表示できる
- 開発中にログをコピーして実行するだけで、読むべき箇所を絞り込める

## 対象ユーザー

- 開発者本人
- ログを手早く確認したい人

## 入力

- クリップボードから入力

## 出力

- CLI表示

## 機能要件

- クリップボード内のログ複数行を読み込めること
- エラーを含む行を抽出できること
- 抽出結果をCLI上に表示できること
- 軽量で開発画面を邪魔せず手早く使えること

## 非機能要件

- CLIで動作すること
- Pythonで実装すること
- 処理が理解しやすい構成であること
- Public repository に有料版の具体的な内部実装を含めないこと

## やらないこと

- グラフ表示
- GUI化
- データベース保存
- 有料版の詳細分析ロジックの公開
