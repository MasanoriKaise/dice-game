import pytest
import dataclasses
from src.domain.value_objects.dice_face import DiceFace

class TestDiceFace:
    """DiceFaceのテストクラス"""
    
    def test_create_valid_face(self):
        """有効な面の作成テスト"""
        face = DiceFace.create(1)
        assert face.number == 1
        assert len(face.pattern) == 5
        assert face.pattern[0] == "┌─────┐"
        assert face.pattern[2] == "│  ●  │"
    
    def test_create_invalid_number(self):
        """無効な数字での面の作成テスト"""
        with pytest.raises(ValueError, match="サイコロの目は1から6の間である必要があります"):
            DiceFace(number=7, pattern=[""] * 5)
    
    def test_create_invalid_pattern(self):
        """無効なパターンでの面の作成テスト"""
        with pytest.raises(ValueError, match="パターンは5行である必要があります"):
            DiceFace(number=1, pattern=[""] * 4)
    
    def test_immutability(self):
        """値オブジェクトの不変性テスト"""
        face = DiceFace.create(1)
        with pytest.raises(dataclasses.FrozenInstanceError):
            face.number = 2 