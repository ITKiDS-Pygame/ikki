import random
import time

def dice():
    roll = random.randrange(1,7)
    if roll < 6:
        return roll
    else:
        return roll *5

dice_rool = dice()
print(dice_rool)

print(f"I rolled a {dice()}")
print(f"Your enemy rolled at {dice()}")
      
player_life = 0
enemy_life = 0

def init():
    global player_life, enemy_life
    player_life, enemy_life = 100, 100

def run():
    global player_life, enemy_life

init()

while True:
    print("敵が現れた!")
    time.sleep(1)
    print("バトルの準備をしましょう!")
    time.sleep(1)
    choice = input("[A]戦う [R]逃げる: ").lower()
    time.sleep(1)
    if choice == "r":
        print("逃げてみる...")
        if dice() > 4:
            print("逃げた!GAME OVER! ")
            exit(1)
    else:
        print("逃げられなかった!")
        damage = dice()
        player_life -= damage
        print(f"ダメージ: {damage}")
        print(f"HP: {player_life}")
        time.sleep(1)
        print("敵はあなたにアタック!")
        if dice() > dice():
            print("敵のアタックが成功")
            damage = dice()

                  

        


        
