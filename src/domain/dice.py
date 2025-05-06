import random
from dataclasses import dataclass
from typing import List

@dataclass
class DiceFace:
    """サイコロの面を表す値オブジェクト"""
    number: int
    pattern: List[str]

    @classmethod
    def create(cls, number: int) -> 'DiceFace':
        """サイコロの面を作成する"""
        patterns = {
            1: [
                "┌─────┐",
                "│     │",
                "│  ●  │",
                "│     │",
                "└─────┘"
            ],
            2: [
                "┌─────┐",
                "│ ●   │",
                "│     │",
                "│   ● │",
                "└─────┘"
            ],
            3: [
                "┌─────┐",
                "│ ●   │",
                "│  ●  │",
                "│   ● │",
                "└─────┘"
            ],
            4: [
                "┌─────┐",
                "│ ● ● │",
                "│     │",
                "│ ● ● │",
                "└─────┘"
            ],
            5: [
                "┌─────┐",
                "│ ● ● │",
                "│  ●  │",
                "│ ● ● │",
                "└─────┘"
            ],
            6: [
                "┌─────┐",
                "│ ● ● │",
                "│ ● ● │",
                "│ ● ● │",
                "└─────┘"
            ]
        }
        return cls(number=number, pattern=patterns[number])

class Dice:
    """サイコロのドメインモデル"""
    def __init__(self):
        self._current_face: DiceFace = None

    def roll(self) -> DiceFace:
        """サイコロを振る"""
        number = random.randint(1, 6)
        self._current_face = DiceFace.create(number)
        return self._current_face

    @property
    def current_face(self) -> DiceFace:
        """現在の面を取得する"""
        if self._current_face is None:
            raise ValueError("サイコロはまだ振られていません")
        return self._current_face 