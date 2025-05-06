import random
from typing import Optional
from src.domain.value_objects.dice_face import DiceFace
from src.domain.events.dice_rolled import DiceRolled

class Dice:
    """サイコロのドメインモデル"""
    def __init__(self):
        self._current_face: Optional[DiceFace] = None
        self._last_event: Optional[DiceRolled] = None

    def roll(self) -> DiceFace:
        """サイコロを振る"""
        number = random.randint(1, 6)
        self._current_face = DiceFace.create(number)
        self._last_event = DiceRolled(face=self._current_face)
        return self._current_face

    @property
    def current_face(self) -> DiceFace:
        """現在の面を取得する"""
        if self._current_face is None:
            raise ValueError("サイコロはまだ振られていません")
        return self._current_face

    @property
    def last_event(self) -> Optional[DiceRolled]:
        """最後のイベントを取得する"""
        return self._last_event 