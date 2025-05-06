import pytest
from fastapi.testclient import TestClient
from datetime import datetime
from src.infrastructure.api.main import app, container
from src.domain.dice import Dice

@pytest.fixture(autouse=True)
def reset_container():
    """各テストの前にコンテナをリセットするフィクスチャ"""
    container.reset_singletons()
    yield
    container.reset_singletons()

@pytest.fixture
def client():
    """テストクライアントのフィクスチャ"""
    return TestClient(app)

class TestDiceEndpoints:
    """サイコロAPIエンドポイントのテストクラス"""
    
    def test_roll_dice(self, client):
        """サイコロを振るエンドポイントのテスト"""
        # テスト実行
        response = client.get("/api/roll")
        
        # 検証
        assert response.status_code == 200
        data = response.json()
        
        # レスポンスの構造の検証
        assert "number" in data
        assert "pattern" in data
        assert "timestamp" in data
        
        # 値の検証
        assert isinstance(data["number"], int)
        assert isinstance(data["pattern"], list)
        assert 1 <= data["number"] <= 6
        assert len(data["pattern"]) == 5
        
        # タイムスタンプの検証
        timestamp = datetime.fromisoformat(data["timestamp"])
        assert isinstance(timestamp, datetime)
        assert timestamp <= datetime.now()
    
    def test_get_current_face_after_roll(self, client):
        """サイコロを振った後に現在の面を取得するテスト"""
        # サイコロを振る
        roll_response = client.get("/api/roll")
        roll_data = roll_response.json()
        
        # 現在の面を取得
        response = client.get("/api/current")
        
        # 検証
        assert response.status_code == 200
        data = response.json()
        
        # レスポンスの構造の検証
        assert "number" in data
        assert "pattern" in data
        assert "timestamp" in data
        
        # 値の検証
        assert isinstance(data["number"], int)
        assert isinstance(data["pattern"], list)
        assert 1 <= data["number"] <= 6
        assert len(data["pattern"]) == 5
        
        # タイムスタンプの検証
        timestamp = datetime.fromisoformat(data["timestamp"])
        assert isinstance(timestamp, datetime)
        assert timestamp == datetime.fromisoformat(roll_data["timestamp"])
    
    def test_get_current_face_before_roll(self, client):
        """サイコロを振る前に現在の面を取得するテスト"""
        # 現在の面を取得
        response = client.get("/api/current")
        
        # 検証
        assert response.status_code == 200
        data = response.json()
        assert "error" in data
    
    def test_cors_headers(self, client):
        """CORSヘッダーのテスト"""
        response = client.options("/api/roll")
        assert response.status_code == 200
        assert "access-control-allow-origin" in response.headers
    
    def test_error_handling(self, client):
        """エラーハンドリングのテスト"""
        # 存在しないエンドポイントへのリクエスト
        response = client.get("/api/nonexistent")
        assert response.status_code == 404 