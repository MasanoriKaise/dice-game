from dataclasses import dataclass
from datetime import datetime
from src.domain.value_objects.dice_face import DiceFace

@dataclass(frozen=True)
class DiceRolled:
    """サイコロが振られたことを表すドメインイベント"""
    face: DiceFace
    timestamp: datetime = None

    def __post_init__(self):
        """イベント作成時にタイムスタンプを設定する"""
        if self.timestamp is None:
            object.__setattr__(self, 'timestamp', datetime.now()) 