# 09 配布計画

## 目的

ErrorInsight `01.00.00` を、GitHubに慣れていない日本語ユーザーでも利用しやすい形で配布する。

配布時は、開発用のGitHub構成と利用者向けの配布構成を分離し、解凍後に迷わず起動できる構成を目指す。

---

## 配布先

- GitHub Releases
- Vector

---

## 配布形式

- ZIP形式
- 配布用パッケージを別途作成する
- GitHub上の開発用ファイル構成をそのまま配布しない
- Python同梱版のみを配布対象とする
- 利用者に別途Pythonインストールを求めない

---

## 起動方法

利用者は、配布パッケージ内の以下のファイルから起動する。

```text
Start_ErrorInsight.bat
```

起動用ファイル名は、初心者にも目的が分かりやすいように英単語を省略しすぎない名前にする。

---

## 説明資料

配布パッケージには、以下の利用者向け資料を同梱する。

- 操作説明PDF
- スクリーンショット付きの操作説明
- サンプルログ

操作説明では、以下を明記する。

- `Start_ErrorInsight.bat` を起動してから、エラーログをコピーすること
- 起動後は画面を閉じず、Enter で繰り返し解析できること
- 終了する場合はコンソールを閉じるか、`q` を入力して Enter を押すこと
- PC終了後、PC再起動後、コンソールを閉じた後、または `q` + Enter で終了した後は、再度 `Start_ErrorInsight.bat` を起動する必要があること
- クリップボード内のテキストをローカルで読み取ること
- 外部通信しないこと
- 保存や送信を行わないこと
- 判断できるのはエラー行から見て取れる範囲であること

配布用文書では「無料版」「有料版」という表記は使わず、配布対象ソフトを `ErrorInsight` と表記する。
有料機能を持つ別ソフトは `ErrorInsight Plus` として扱い、ErrorInsightとは別ソフトとして説明する。

---

## 安全性表示

利用者が不安を感じにくいように、次の点も説明する。

- 外部APIに送信しない
- ログを保存しない
- 履歴を保存しない
- 課金処理を行わない
- ライセンス認証を行わない

---

## 配布構成方針

GitHub構成と配布構成は分離する。

GitHub repository は、開発履歴、ソースコード、テスト、設計docsを管理する場所とする。
配布用ZIPは、利用者が使うために必要なファイルだけを整理して配置する。

利用者が直接読む説明資料やサンプルログ名は、日本語を使用する。
ただし、起動用bat、プログラムが参照するフォルダ、ライセンスファイルなどは、文字化けやパス問題を避けるため英数字を基本とする。

### 想定配布構成

```text
ErrorInsight/
├── Start_ErrorInsight.bat
├── はじめにお読みください.txt
├── app/
│   ├── errorinsight/
│   ├── pyperclip/
│   └── wcwidth/
├── python/
├── sample_logs/
│   ├── サンプルログ_Python.txt
│   ├── サンプルログ_Java.txt
│   ├── サンプルログ_CSharp.txt
│   ├── サンプルログ_JavaScript.txt
│   ├── サンプルログ_SQL.txt
│   └── サンプルログ_エラーなし.txt
├── docs/
│   ├── 操作説明書.pdf
│   └── screenshots/
└── licenses/
```

### 主要フォルダの役割

- `Start_ErrorInsight.bat`: 利用者が起動するためのファイル
- `app/`: ErrorInsight本体と実行に必要なPythonライブラリを置く
- `app/errorinsight/`: ErrorInsight本体コード
- `app/pyperclip/`: クリップボード読み取り用ライブラリ
- `app/wcwidth/`: ターミナル表示幅調整用ライブラリ
- `python/`: 同梱Python本体
- `sample_logs/`: 動作確認用の自作サンプルログ
- `docs/`: 操作説明PDFやスクリーンショットを置く
- `licenses/`: ErrorInsight本体、Python、第三者ライブラリのライセンス表記を置く

### 同梱Pythonの方針

配布パッケージには Windows向けの Python embeddable package を同梱する。

利用者に別途Pythonのインストールを求めない。

同梱Pythonの `python313._pth` には、配布用 `app` フォルダを読み込めるように以下を追加する。

```text
..\app
```

これにより、同梱Pythonから `app/errorinsight`、`app/pyperclip`、`app/wcwidth` を読み込めるようにする。

### 配布前に除外するもの

ZIP化前に、以下の開発・生成物は削除する。

- `__pycache__/`
- `*.pyc`
- `.gitkeep`

これらは動作に必須ではなく、利用者向け配布物には含めない。

### ライセンス構成

```text
licenses/
├── ErrorInsight_LICENSE.txt
├── NOTICE.txt
├── THIRD_PARTY_NOTICES.txt
├── PYTHON_LICENSE.txt
├── PYPERCLIP_LICENSE.txt
└── WCWIDTH_LICENSE.txt
```

- `ErrorInsight_LICENSE.txt`: ErrorInsight本体のBSD 3-Clause License
- `NOTICE.txt`: 公式配布元、問い合わせ先、改変版・再配布版に関する注意
- `THIRD_PARTY_NOTICES.txt`: 使用ライブラリ一覧
- `PYTHON_LICENSE.txt`: Python本体のライセンス
- `PYPERCLIP_LICENSE.txt`: pyperclip のライセンス
- `WCWIDTH_LICENSE.txt`: wcwidth のライセンス

Python本体を同梱するため、Pythonのライセンス表記も追加する。

---

## サンプルログ方針

配布パッケージには、動作確認用のサンプルログを同梱する。

### サンプルログの種類

- 公式ドキュメント由来のエラー例
- 自作ログ

現時点の配布パッケージでは、著作権や個人情報のリスクを避けるため、自作ログを同梱する。
公式ドキュメント由来のエラー例を使う場合は、出典とライセンスを確認してから追加する。

### 同梱サンプルログ

- `サンプルログ_Python.txt`
- `サンプルログ_Java.txt`
- `サンプルログ_CSharp.txt`
- `サンプルログ_JavaScript.txt`
- `サンプルログ_SQL.txt`
- `サンプルログ_エラーなし.txt`

### 注意点

- 公式ドキュメント由来の内容を使う場合は、出典やライセンスに注意する
- 長文引用を避け、必要最小限のエラー例として扱う
- 自作ログは、実在する個人情報、パス、APIキー、業務情報を含めない
- サンプルログは、初心者がコピーしてすぐ試せる内容にする

---

## 配布前チェック

- `Start_ErrorInsight.bat` から起動できる
- 起動後に Enter で繰り返し解析できる
- コンソールを閉じるか、`q` + Enter で終了できる
- Python / Java / C# / JavaScript / SQL のサンプルログで動作する
- エラーなしログでメッセージが表示される
- 起動時に `動作モード: ローカル実行` と `外部通信: なし` が表示される
- 操作説明PDFの手順通りに動作する
- ZIPを別フォルダに展開して動作確認する
- 不要な開発用ファイルを含めていない
- ライセンス表記を同梱している

---

## 今回含めないもの

- GUI
- インストーラー
- 自動アップデート
- 外部AI API連携
- 課金処理
- ライセンス認証
- ErrorInsight Plus の詳細分析機能

---

## 将来検討するもの

- exe化
- Windows向けインストーラー
- PyPI / pipx 配布
- 操作説明PDFのデザイン改善
