# Dice Game 🎲

シンプルなコマンドラインサイコロゲームです。ASCII artのアニメーションで、サイコロを振る様子を表現します。

```
┌─────┐
│ ●   │
│  ●  │
│   ● │
└─────┘

サイコロが転がっています...
```

## 機能

- サイコロを振るアニメーション表示
- ASCII artによる美しいサイコロの目の表現
- 1から6までのランダムな数値生成

## インストール

このプロジェクトは[uv](https://github.com/astral-sh/uv)を使用して管理されています。

```bash
# 仮想環境の作成とアクティベート
uv venv
source .venv/bin/activate  # Unix系の場合
# Windows の場合: .venv\Scripts\activate

# プロジェクトのインストール
uv pip install -e .
```

## 使い方

インストール後、以下のいずれかの方法でサイコロを振ることができます：

```bash
# コマンドラインツールとして実行
dice

# または、Pythonモジュールとして実行
python -m src.saikoro
```

## 開発

### 環境セットアップ

```bash
# 開発用の依存関係をインストール
uv venv
source .venv/bin/activate
uv pip install -e .
```

### テストの実行

```bash
pytest -v
```

## プロジェクト構造

```
dice-game/
├── src/
│   ├── __init__.py
│   └── saikoro.py      # メインのゲームロジック
├── tests/
│   └── test_saikoro.py # テストコード
├── pyproject.toml      # プロジェクト設定
└── README.md          # このファイル
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。