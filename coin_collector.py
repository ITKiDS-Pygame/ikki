import pygame
import random

SCREEN_X = 640
SCREEN_Y = 480
SCREEN = (SCREEN_X, SCREEN_Y)
FPS = 60
BG = (0,0,0)
CLOCK = pygame.time.Clock()
SURFACE = pygame.display.set_mode(SCREEN)

PLAYER_COLOR = (0,0,255)
COIN_COLOR = (255,255,0)
coinList = []

class Player:
    def __init__(self, startx, starty):
        self.surface = SURFACE
        self.color = PLAYER_COLOR
        self.size = 30
        self.speed = 5
        self.rect = pygame.Rect(startx, starty, self.size, self.size)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.x >= SCREEN_X - 30:
            self.rect.x = SCREEN_X - 30
        if self.rect.y >= SCREEN_Y - 30:
            self.rect.y = SCREEN_Y - 30

    def update(self):
        self.move()

    def draw(self):
        pygame.draw.rect(self.surface,self.color,self.rect) 

class Coin:
    def __init__(self, posX, posY):
        self.surface = SURFACE
        self.size = 5
        self.color = COIN_COLOR
        self.rect = pygame.Rect(posX, posY, self.size, self.size)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
    
def get_coins():
    global coinList
    for i in range(25):
        coinList.append(Coin(random.randrange(0, SCREEN_X - 5),random.randrange(0, SCREEN_Y - 5)))






player = Player(SCREEN_X / 2, SCREEN_Y / 2)

def draw():
    player.draw()
    if len(coinList) > 0:
        for coin in coinList:
            coin.draw()


def update():
    CLOCK.tick(FPS)
    if len(coinList) == 0:
        get_coins()
        
    draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(1)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        exit(1)
    
    for coin in coinList:
        if coin.rect.colliderect(player.rect):
            coinList.remove(coin)


    player.update()
    pygame.display.update()
    SURFACE.fill(BG)

def run():
    while True:
        update()


if  __name__ == "__main__":
    run()