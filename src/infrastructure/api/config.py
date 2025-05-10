"""APIの設定"""

# API設定
API_HOST = "0.0.0.0"
API_PORT = 8000

# CORS設定
CORS_ORIGINS = [
    "http://localhost:3000",  # React開発サーバー
]

# 環境設定
ENV = "development"  # development, production 