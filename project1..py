import random
import time

def dice():
    roll = random.randrange(1,7)
    return roll

dice_rool = dice()
print(dice_rool)

print(f"I rolled a {dice()}")
print(f"Your enemy rolled at {dice()}")
      
player_life = 0
enemy_life = 0

def init():
    global player_life, enemy_life
    player_life = 100
    enemy_life = 100

def init():
    global player_life, enemy_life
    player_life, enemy_life = 100, 100

def run():
    global player_life, enemy_life

init()

while True:
    print( )
