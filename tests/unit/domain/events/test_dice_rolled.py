import pytest
import dataclasses
from datetime import datetime
from src.domain.value_objects.dice_face import DiceFace
from src.domain.events.dice_rolled import DiceRolled

class TestDiceRolled:
    """DiceRolledのテストクラス"""
    
    def test_create_event(self):
        """イベントの作成テスト"""
        face = DiceFace.create(1)
        event = DiceRolled(face=face)
        
        assert event.face == face
        assert isinstance(event.timestamp, datetime)
    
    def test_immutability(self):
        """イベントの不変性テスト"""
        face = DiceFace.create(1)
        event = DiceRolled(face=face)
        
        with pytest.raises(dataclasses.FrozenInstanceError):
            event.face = DiceFace.create(2) 