from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class DiceFace:
    """サイコロの面を表す値オブジェクト"""
    number: int
    pattern: List[str]

    def __post_init__(self):
        """値の検証"""
        if not 1 <= self.number <= 6:
            raise ValueError("サイコロの目は1から6の間である必要があります")
        if len(self.pattern) != 5:
            raise ValueError("パターンは5行である必要があります")

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