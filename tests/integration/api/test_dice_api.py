import pytest
from fastapi.testclient import TestClient
from src.infrastructure.api.main import app
from src.infrastructure.container import Container
from datetime import datetime

@pytest.fixture
def container():
    """コンテナのフィクスチャ"""
    return Container()

@pytest.fixture
def client():
    """テストクライアントのフィクスチャ"""
    return TestClient(app)

class TestDiceApiIntegration:
    """サイコロAPIの統合テストクラス"""
    
    def test_roll_and_get_sequence(self, client):
        """サイコロを振って取得する一連の流れのテスト"""
        # サイコロを振る
        roll_response = client.get("/api/roll")
        assert roll_response.status_code == 200
        roll_data = roll_response.json()
        
        # レスポンスの検証
        assert "number" in roll_data
        assert "pattern" in roll_data
        assert "timestamp" in roll_data
        assert 1 <= roll_data["number"] <= 6
        assert len(roll_data["pattern"]) == 5
        
        # タイムスタンプの検証
        timestamp = datetime.fromisoformat(roll_data["timestamp"])
        assert isinstance(timestamp, datetime)
        
        # 現在の面を取得
        current_response = client.get("/api/current")
        assert current_response.status_code == 200
        current_data = current_response.json()
        
        # 同じ面が返されることを確認
        assert roll_data["number"] == current_data["number"]
        assert roll_data["pattern"] == current_data["pattern"]
        assert roll_data["timestamp"] == current_data["timestamp"]
    
    def test_multiple_rolls(self, client):
        """複数回サイコロを振るテスト"""
        # 最初のサイコロを振る
        first_roll = client.get("/api/roll").json()
        first_timestamp = datetime.fromisoformat(first_roll["timestamp"])
        
        # 2回目のサイコロを振る
        second_roll = client.get("/api/roll").json()
        second_timestamp = datetime.fromisoformat(second_roll["timestamp"])
        
        # タイムスタンプの検証
        assert first_timestamp < second_timestamp
        
        # サイコロの目の検証
        assert isinstance(first_roll["number"], int)
        assert isinstance(second_roll["number"], int)
        assert 1 <= first_roll["number"] <= 6
        assert 1 <= second_roll["number"] <= 6 