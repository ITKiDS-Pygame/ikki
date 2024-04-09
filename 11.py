import pygame

SCREEN_X = 640
SCREEN_Y = 480
SCREEN = (SCREEN_X, SCREEN_Y)
BG = (0,0,0)
FPS = 60
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
YELLOW = (255,255,0)
current_color = BLUE
speed = 5

surface = pygame.display.set_mode(SCREEN)
pygame.display.set_caption("しかく練習")
CLOCK = pygame.time.Clock()


center_x = SCREEN_X / 2
center_y = SCREEN_Y / 2
center = (center_x, center_y)
sides = 50
start_x = center_x - sides / 2
start_y = center_y - sides / 2
myRect = pygame.Rect(start_x, start_y, sides, sides)

def draw():
    pygame.draw.rect(surface, current_color, myRect)
    

def update():
    global current_color
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(1)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        exit(1)
    if keys[pygame.K_r]:
        current_color = RED
    if keys[pygame.K_y]:
        current_color = YELLOW
    if keys[pygame.K_b]:
        current_color = BLUE
    if keys[pygame.K_w]:
        current_color = WHITE
    if keys[pygame.K_g]:
        current_color = GREEN
    if keys[pygame.K_RIGHT]:
        myRect.x += speed
    if keys[pygame.K_LEFT]:
        myRect.x -= speed
    if keys[pygame.K_UP]:
        myRect.y -= speed
    if keys[pygame.K_DOWN]:
        myRect.y += speed

    if myRect.x <= 0:
        myRect.x = 0
    if myRect.y <= 0:
        myRect.y = 0
    if myRect.x >= SCREEN_X - myRect.width:
        myRect.x = SCREEN_X - myRect.width
    if myRect.y >= SCREEN_Y - myRect.height:
        myRect.y = SCREEN_Y - myRect.height


    draw()

    pygame.display.update()
    surface.fill(BG)

def run():
    while True:
        update()

if __name__=='__main__':
    run()
