from typing import Dict, List, Union
from src.domain.dice import Dice
from src.application.interfaces.dice import DiceService
from src.application.dtos.dice import DiceFaceDTO, DiceRolledDTO

class DiceServiceImpl(DiceService):
    """サイコロサービスの実装"""
    
    def __init__(self, dice: Dice):
        self._dice = dice
    
    def roll(self) -> Dict[str, Union[int, List[str], str]]:
        """サイコロを振る"""
        face = self._dice.roll()
        event = self._dice.last_event
        return self._to_dict(DiceRolledDTO(
            face=DiceFaceDTO(number=face.number, pattern=face.pattern),
            timestamp=event.timestamp
        ))
    
    def get_current_face(self) -> Dict[str, Union[int, List[str], str]]:
        """現在のサイコロの面を取得する"""
        try:
            face = self._dice.current_face
            event = self._dice.last_event
            return self._to_dict(DiceRolledDTO(
                face=DiceFaceDTO(number=face.number, pattern=face.pattern),
                timestamp=event.timestamp
            ))
        except (ValueError, AttributeError) as e:
            return {"error": str(e)}
    
    def _to_dict(self, dto: DiceRolledDTO) -> Dict[str, Union[int, List[str], str]]:
        """DTOを辞書に変換する"""
        if dto.error:
            return {"error": dto.error}
        return {
            "number": dto.face.number,
            "pattern": dto.face.pattern,
            "timestamp": dto.timestamp.isoformat()
        } 