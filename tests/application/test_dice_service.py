from src.application.dice_service import DiceService
from src.domain.dice import DiceFace

def test_roll_dice():
    """サイコロを振るテスト"""
    service = DiceService()
    face = service.roll_dice()
    assert isinstance(face, DiceFace)
    assert 1 <= face.number <= 6

def test_get_current_face():
    """現在の面を取得するテスト"""
    service = DiceService()
    service.roll_dice()
    face = service.get_current_face()
    assert isinstance(face, DiceFace)
    assert 1 <= face.number <= 6

def test_get_rotation_messages():
    """回転メッセージを取得するテスト"""
    service = DiceService()
    messages = service.get_rotation_messages()
    assert len(messages) == 4
    assert "サイコロが転がっています..." in messages
    assert "コロコロ..." in messages
    assert "ゴロゴロ..." in messages
    assert "コロン..." in messages 