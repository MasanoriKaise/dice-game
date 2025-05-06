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
- ドメイン駆動設計（DDD）に基づいたクリーンな設計

## 必要要件

- Python 3.8以上
- [uv](https://github.com/astral-sh/uv) パッケージマネージャ

## インストール

このプロジェクトは[uv](https://github.com/astral-sh/uv)を使用して管理されています。

```bash
# リポジトリのクローン
git clone https://github.com/MasanoriKaise/dice-game.git
cd dice-game

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
python -m src.infrastructure.console_ui
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
# すべてのテストを実行
pytest -v

# テストカバレッジを確認
pytest --cov=src --cov-report=term-missing
```

### コードの品質管理

このプロジェクトは以下の品質管理ツールを使用しています：

- **pytest**: ユニットテストとテストカバレッジ
- **GitHub Actions**: 継続的インテグレーション（CI）

## プロジェクト構造

プロジェクトはドメイン駆動設計（DDD）の原則に従って構造化されています：

```
dice-game/
├── src/
│   ├── domain/           # ドメイン層
│   │   ├── __init__.py
│   │   └── dice.py      # サイコロのドメインモデル
│   ├── application/      # アプリケーション層
│   │   ├── __init__.py
│   │   └── dice_service.py  # ユースケース
│   └── infrastructure/   # インフラストラクチャ層
│       ├── __init__.py
│       └── console_ui.py # UI実装
├── tests/               # テストコード
│   ├── __init__.py
│   ├── domain/          # ドメインのテスト
│   │   ├── __init__.py
│   │   └── test_dice.py
│   ├── application/     # アプリケーションのテスト
│   │   ├── __init__.py
│   │   └── test_dice_service.py
│   └── infrastructure/  # インフラストラクチャのテスト
│       ├── __init__.py
│       └── test_console_ui.py
├── .github/             # GitHub関連の設定
│   └── workflows/       # GitHub Actions
│       └── python-app.yml
├── pyproject.toml      # プロジェクト設定
└── README.md          # このファイル
```

### アーキテクチャ

このプロジェクトは以下の3層アーキテクチャに基づいています：

1. **ドメイン層** (`src/domain/`)
   - ビジネスロジックの中心
   - サイコロのコアロジックを含む
   - `DiceFace`値オブジェクトと`Dice`エンティティを提供

2. **アプリケーション層** (`src/application/`)
   - ユースケースの実装
   - ドメインサービスの調整
   - サイコロを振るユースケースを提供

3. **インフラストラクチャ層** (`src/infrastructure/`)
   - 外部インターフェースの実装
   - コンソールUIの提供
   - アニメーション表示の実装

## 貢献

1. このリポジトリをフォークする
2. 新しいブランチを作成する (`git checkout -b feature/amazing-feature`)
3. 変更をコミットする (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュする (`git push origin feature/amazing-feature`)
5. プルリクエストを作成する

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 作者

- Masanori Kaise - [GitHub](https://github.com/MasanoriKaise)