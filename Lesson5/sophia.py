import pygame
import time
pygame.init()

rocket = pygame.image.load('rocket.png')
sky = pygame.image.load('bg.png')
screen = pygame.display.set_mode([800,600])

x = 400
y = 300

keys = [False,False,False,False]

running = True
while running:
    screen.blit(sky,(0,0))
    screen.blit(rocket,(x,y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_UP:
                keys[0] = True
            elif event.key ==  pygame.K_DOWN: 
                keys[1] = True
            elif event.key ==  pygame.K_LEFT:
                keys[2] = True
            elif event.key ==  pygame.K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key ==  pygame.K_UP:
                keys[0] = False
            elif event.key ==  pygame.K_DOWN: 
                keys[1] = False
            elif event.key ==  pygame.K_LEFT:
                keys[2] = False
            elif event.key ==  pygame.K_RIGHT:
                keys[3] = False
                
    if keys[0] == True:
        y -= 5
    elif keys[1] == True:
        y += 5
    elif keys[2] == True:
        x -= 5
    elif keys[3] == True:
        x += 5
    #pygame.display.update()


        



