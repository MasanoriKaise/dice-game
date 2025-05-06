import pytest
from unittest.mock import patch, MagicMock
from src.infrastructure.console_ui import ConsoleUI
from src.application.dice_service import DiceService

def test_clear_screen():
    """画面クリアのテスト"""
    with patch('os.system') as mock_system:
        ui = ConsoleUI()
        ui.clear_screen()
        mock_system.assert_called_once()

def test_show_rolling_animation():
    """アニメーション表示のテスト"""
    with patch('os.system'), \
         patch('time.sleep'), \
         patch('builtins.print') as mock_print:
        
        # モックの設定
        mock_service = MagicMock(spec=DiceService)
        mock_face = MagicMock()
        mock_face.pattern = ["line1", "line2"]
        mock_service.roll_dice.return_value = mock_face
        mock_service.get_rotation_messages.return_value = ["msg1", "msg2"]
        
        # テスト実行
        ui = ConsoleUI()
        ui._dice_service = mock_service  # プライベート属性を直接設定
        ui.show_rolling_animation()
        
        # 検証
        assert mock_service.roll_dice.call_count > 0
        assert mock_print.call_count > 0 