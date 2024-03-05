import pygame

screen_w = 640
screen_h = 480
screen = (640,1080)
BG = (0,0,0)

surface = pygame.display.set_mode(screen)
pygame.display.set_caption("My first Window")

def update():
    global BG
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(1)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        exit(1)

    if keys[pygame.K_SPACE]:
        BG=(255,0,0)
    
    elif keys[pygame.K_x]:
        BG=(0,255,0)

    elif keys[pygame.K_UP]:
        BG=(0,0,255)
    else:
        BG=(255,255,0)

    pygame.display.update()
    surface.fill(BG)

while True:
    update()







