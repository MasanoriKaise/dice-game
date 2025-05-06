from abc import ABC, abstractmethod
from typing import Dict, List, Union

class DiceService(ABC):
    """サイコロサービスのインターフェース"""
    
    @abstractmethod
    def roll(self) -> Dict[str, Union[int, List[str]]]:
        """サイコロを振る
        
        Returns:
            Dict[str, Union[int, List[str]]]: サイコロの面の情報
            {
                "number": int,  # サイコロの目（1-6）
                "pattern": List[str]  # サイコロの表示パターン
            }
        """
        pass
    
    @abstractmethod
    def get_current_face(self) -> Dict[str, Union[int, List[str]]]:
        """現在のサイコロの面を取得する
        
        Returns:
            Dict[str, Union[int, List[str]]]: サイコロの面の情報
            {
                "number": int,  # サイコロの目（1-6）
                "pattern": List[str]  # サイコロの表示パターン
            }
        """
        pass 