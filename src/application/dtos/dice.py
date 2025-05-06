from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class DiceFaceDTO:
    """サイコロの面のDTO"""
    number: int
    pattern: List[str]

@dataclass
class DiceRolledDTO:
    """サイコロが振られた結果のDTO"""
    face: DiceFaceDTO
    timestamp: datetime
    error: Optional[str] = None 