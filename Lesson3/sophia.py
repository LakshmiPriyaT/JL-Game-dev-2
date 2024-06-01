import pygame
import random
pygame.init()

screen = pygame.display.set_mode([500,500])
screen.fill('powderblue')
pygame.display.update()
class My_circle():
    def __init__ (self,pos,radius,color):
        self.screen = screen
        self.pos = pos
        self.radius = radius
        self.color =color

    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius)
    
    def shrink(self,r):
       self.radius = self.radius - r
       pygame.draw.circle(self.screen,self.color,self.pos,self.radius)

    def grow(self,radius):
       self.radius = self.radius + radius
       pygame.draw.circle(self.screen,self.color,self.pos,self.radius)
circle1 = My_circle((150,100),30,'red')




running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:

        circle1.draw()
        pygame.display.update()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            screen.fill('powderblue')
            circle1.grow(5)
            pygame.display.update()

        elif event.key == pygame.K_DOWN:
            screen.fill('powderblue')
            circle1.shrink(10)
            pygame.display.update()