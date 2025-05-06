import pytest
from unittest.mock import patch
from src.saikoro import roll_dice, get_dice_face

def test_roll_dice_range():
    """サイコロの目が1から6の範囲内であることをテスト"""
    for _ in range(100):  # 100回テスト
        result = roll_dice()
        assert 1 <= result <= 6

def test_dice_face_representation():
    """各サイコロの面が正しく表現されていることをテスト"""
    # 1の目のテスト
    face_1 = get_dice_face(1)
    assert len(face_1) == 5  # 5行のASCIIアート
    assert "●" in face_1[2]  # 中央に目がある
    assert face_1[2].count("●") == 1  # 目が1つ

    # 6の目のテスト
    face_6 = get_dice_face(6)
    assert len(face_6) == 5
    assert face_6[1].count("●") == 2  # 上段に2つの目
    assert face_6[2].count("●") == 2  # 中段に2つの目
    assert face_6[3].count("●") == 2  # 下段に2つの目

@pytest.mark.parametrize("dice_number", range(1, 7))
def test_all_dice_faces_exist(dice_number):
    """1から6までの全ての面が存在することをテスト"""
    face = get_dice_face(dice_number)
    assert len(face) == 5
    assert all(len(line) == 7 for line in face)  # 各行が7文字

def test_roll_dice_randomness():
    """サイコロのランダム性をテスト"""
    with patch('random.randint', return_value=4) as mock_randint:
        result = roll_dice()
        assert result == 4
        mock_randint.assert_called_once_with(1, 6) 