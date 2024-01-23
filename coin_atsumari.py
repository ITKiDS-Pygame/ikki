import pygame

SCREEN_W = 640
SCREEN_H = 480
SURFACE = pygame.display.set_mode((SCREEN_W, SCREEN_H))
CLOCK = pygame.time.Clock()
FPS = 60
BG = (0, 0, 0)

class Coin:
    pass

class Player:
    def __init__(self):
        self.speed = 3
        self.color = (0, 255, 0)
        self.rect = pygame.Rect(SCREEN_W / 2, SCREEN_H / 2, 25, 25)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LSHIFT]:
            self.speed = 5
        else:
            self.speed = 3

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.x >= SCREEN_W - 25:
            self.rect.x = SCREEN_W - 25
        if self.rect.y >= SCREEN_H - 25:
            self.rect.y = SCREEN_H - 25

    def draw(self):
        pygame.draw.rect(SURFACE, self.color, self.rect)


def get_coins(amount):
    pass


player = Player()

def draw():
    player.draw()

def update():
    CLOCK.tick(FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            exit(1)

    

    draw()
    player.draw()
    pygame.display.update()
    SURFACE.fill(BG)

def run():
    while True:
        update()

if __name__ == "__main__":
    run()