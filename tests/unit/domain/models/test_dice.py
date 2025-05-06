import pytest
from src.domain.models.dice import Dice
from src.domain.value_objects.dice_face import DiceFace
from src.domain.events.dice_rolled import DiceRolled

class TestDice:
    """Diceのテストクラス"""
    
    @pytest.fixture
    def dice(self):
        """Diceのインスタンスを作成するフィクスチャ"""
        return Dice()
    
    def test_roll(self, dice):
        """サイコロを振るテスト"""
        face = dice.roll()
        
        assert isinstance(face, DiceFace)
        assert 1 <= face.number <= 6
        assert len(face.pattern) == 5
    
    def test_get_current_face_before_roll(self, dice):
        """サイコロを振る前に現在の面を取得するテスト"""
        with pytest.raises(ValueError, match="サイコロはまだ振られていません"):
            _ = dice.current_face
    
    def test_get_current_face_after_roll(self, dice):
        """サイコロを振った後に現在の面を取得するテスト"""
        face = dice.roll()
        current_face = dice.current_face
        assert current_face == face
    
    def test_last_event(self, dice):
        """最後のイベントを取得するテスト"""
        face = dice.roll()
        event = dice.last_event
        
        assert isinstance(event, DiceRolled)
        assert event.face == face
        assert event.timestamp is not None 