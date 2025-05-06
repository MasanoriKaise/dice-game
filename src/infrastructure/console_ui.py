import os
import time
from src.application.services.dice import DiceServiceImpl
from src.domain.dice import Dice

class ConsoleUI:
    """コンソールUIの実装"""
    def __init__(self):
        dice = Dice()
        self._dice_service = DiceServiceImpl(dice)

    def clear_screen(self):
        """画面をクリアする"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_rolling_animation(self):
        """サイコロが転がるアニメーションを表示する"""
        # サイコロが転がるアニメーション
        for i in range(15):
            self.clear_screen()
            temp_result = self._dice_service.roll()
            
            # 回転効果のための空白行
            print("\n" * 2)
            
            # サイコロの面を表示
            for line in temp_result["pattern"]:
                print(" " * 5 + line)
            
            # 回転効果のためのメッセージ
            rotation_messages = ["回転中...", "転がっています...", "まだ回っています..."]
            print("\n" + " " * 5 + rotation_messages[i % len(rotation_messages)])
            
            # アニメーションの速度を徐々に遅くする
            time.sleep(0.1 + (i * 0.02))
        
        # 最終結果を表示
        self.clear_screen()
        final_result = self._dice_service.roll()
        print("\n" * 2)
        for line in final_result["pattern"]:
            print(" " * 5 + line)
        print("\n" + " " * 5 + "サイコロが止まりました！")

def show_rolling_animation():
    """サイコロのアニメーションを表示する（エントリーポイント）"""
    ui = ConsoleUI()
    ui.show_rolling_animation() 