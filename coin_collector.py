import pygame

SCREEN_X = 640
SCREEN_Y = 480
SCREEN = (SCREEN_X, SCREEN_Y)
FPS = 60
BG = (0,0,0)
CLOCK = pygame.time.Clock()
SURFACE = pygame.display.set_mode(SCREEN)

PLAYER_COLOR = (0,0,255)
COIN_COLOR = (255,255,0)

def draw():
    pass

def update():
    CLOCK.tick(FPS)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(1)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        exit(1)

    pygame.display.update()
    SURFACE.fill(BG)

def run():
    while True:
        update()

if  __name__ == "__ main__":
    run()



