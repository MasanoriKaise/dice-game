import pytest
from src.domain.dice import Dice, DiceFace

def test_dice_face_creation():
    """DiceFaceの作成をテスト"""
    face = DiceFace.create(1)
    assert face.number == 1
    assert len(face.pattern) == 5
    assert face.pattern[0] == "┌─────┐"
    assert face.pattern[2] == "│  ●  │"

def test_dice_face_invalid_number():
    """無効な数字でのDiceFace作成をテスト"""
    with pytest.raises(KeyError):
        DiceFace.create(7)

def test_dice_roll():
    """サイコロを振るテスト"""
    dice = Dice()
    face = dice.roll()
    assert isinstance(face, DiceFace)
    assert 1 <= face.number <= 6

def test_dice_current_face_before_roll():
    """サイコロを振る前のcurrent_faceをテスト"""
    dice = Dice()
    with pytest.raises(ValueError):
        _ = dice.current_face

def test_dice_current_face_after_roll():
    """サイコロを振った後のcurrent_faceをテスト"""
    dice = Dice()
    face = dice.roll()
    assert dice.current_face == face 