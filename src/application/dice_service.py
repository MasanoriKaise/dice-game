from typing import List
from src.domain.dice import Dice, DiceFace

class DiceService:
    """サイコロのアプリケーションサービス"""
    def __init__(self):
        self._dice = Dice()

    def roll_dice(self) -> DiceFace:
        """サイコロを振る"""
        return self._dice.roll()

    def get_current_face(self) -> DiceFace:
        """現在の面を取得する"""
        return self._dice.current_face

    def get_rotation_messages(self) -> List[str]:
        """回転メッセージを取得する"""
        return ["サイコロが転がっています...", "コロコロ...", "ゴロゴロ...", "コロン..."] 