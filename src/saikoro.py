import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_dice_face(number):
    dice_faces = {
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
    return dice_faces[number]

def roll_dice():
    return random.randint(1, 6)

def show_rolling_animation():
    # サイコロが転がるアニメーション
    for i in range(15):
        clear_screen()
        temp_result = roll_dice()
        
        # 回転効果のための空白行
        print("\n" * 2)
        
        # サイコロの面を表示
        dice_face = get_dice_face(temp_result)
        for line in dice_face:
            print(" " * 5 + line)
        
        # 回転効果のためのメッセージ
        rotation_messages = ["サイコロが転がっています...", "コロコロ...", "ゴロゴロ...", "コロン..."]
        print("\n" + " " * 5 + rotation_messages[i % len(rotation_messages)])
        
        # アニメーションの速度を徐々に遅くする
        time.sleep(0.1 + (i * 0.02))
    
    # 最終結果を表示
    clear_screen()
    final_result = roll_dice()
    print("\n" * 2)
    dice_face = get_dice_face(final_result)
    for line in dice_face:
        print(" " * 5 + line)
    print("\n" + " " * 5 + "サイコロが止まりました！")

if __name__ == "__main__":
    show_rolling_animation()
