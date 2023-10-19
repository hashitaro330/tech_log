# Sphinx プロジェクトの立ち上げ方

## Sphinx とは

    python製のドキュメント生成ツール
    reSTやmarkdownで書かれたファイルをHTMLなど変換する。
    github Pagesと連携することで、github上でドキュメントを公開できる。

## インストールとクイックスタート

python 環境がインストールされていることが前提

以下のコマンドでインストールされているか確認して、されていなければインストールする。

> $ python -V

pip で sphinx を install

> $ pip install sphinx

sphinx の quickstar を実行。対話形式で設定

> $ sphinx-quickstart

Build してみる

> $ make html

build/html/index.html をブラウザで開くと、quickstart の画面が確認できる。

## md ファイルでドキュメント作成

まず事前準備として、myst-parser をインストール

> pip install --upgrade myst-parser

conf.py を修正

以下を追加する

```
extensions = [
    'myst_parser'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
```

## 実行手順

make html を実行することで、更新される
