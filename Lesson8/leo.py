import pygame
pygame.init()

WIDTH = 700
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Sprites")

background = pygame.image.load("background.png")
class Player(pygame.sprite.Sprite):
    def __init__(self, pic):
        super().__init__() #importing constructor of the super class (all properties)
        self.image = pygame.image.load(pic)
        self.rect = self.image.get_rect()

    def update(self, keys, w):
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -w)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-w, 0)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, w)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(w, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT



group1 = pygame.sprite.Group()
pic = "rat.png"
rat = Player(pic)
group1.add(rat)

#rocket = Player("C5 Sprites/rocket.png")
#group1.add(rocket)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    rat.update(keys, 1)
    #rocket.update(keys, 0.2)
    screen.blit(background, (0, 0))
    group1.draw(screen)
    pygame.display.update()