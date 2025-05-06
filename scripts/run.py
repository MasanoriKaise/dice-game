"""アプリケーション起動スクリプト"""
import uvicorn
from src.infrastructure.api.main import app
from config.api import API_HOST, API_PORT

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=API_HOST,
        port=API_PORT,
        reload=True  # 開発環境での自動リロード
    ) 