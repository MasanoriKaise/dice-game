import pytest
from unittest.mock import Mock
from datetime import datetime
from src.domain.models.dice import Dice
from src.domain.value_objects.dice_face import DiceFace
from src.domain.events.dice_rolled import DiceRolled
from src.application.services.dice import DiceServiceImpl

class TestDiceServiceImpl:
    """DiceServiceImplのテストクラス"""
    
    @pytest.fixture
    def mock_dice(self):
        """Diceのモックを作成するフィクスチャ"""
        return Mock(spec=Dice)
    
    @pytest.fixture
    def dice_service(self, mock_dice):
        """DiceServiceImplのインスタンスを作成するフィクスチャ"""
        return DiceServiceImpl(dice=mock_dice)
    
    def test_roll_dice(self, mock_dice, dice_service):
        """サイコロを振るテスト"""
        # モックの設定
        mock_face = DiceFace.create(3)
        mock_event = DiceRolled(face=mock_face)
        mock_dice.roll.return_value = mock_face
        mock_dice.last_event = mock_event
        
        # テスト実行
        result = dice_service.roll()
        
        # 検証
        assert result["number"] == 3
        assert result["pattern"] == mock_face.pattern
        assert "timestamp" in result
        mock_dice.roll.assert_called_once()
    
    def test_get_current_face(self, mock_dice, dice_service):
        """現在のサイコロの面を取得するテスト"""
        # モックの設定
        mock_face = DiceFace.create(4)
        mock_event = DiceRolled(face=mock_face)
        mock_dice.current_face = mock_face
        mock_dice.last_event = mock_event
        
        # テスト実行
        result = dice_service.get_current_face()
        
        # 検証
        assert result["number"] == 4
        assert result["pattern"] == mock_face.pattern
        assert "timestamp" in result
    
    def test_get_current_face_error(self, mock_dice, dice_service):
        """サイコロが振られていない場合のエラーテスト"""
        # モックの設定
        mock_dice.current_face = None
        
        # テスト実行
        result = dice_service.get_current_face()
        
        # 検証
        assert "error" in result
        assert result["error"] == "サイコロはまだ振られていません" 