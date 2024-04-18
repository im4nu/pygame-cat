import pygame
import sys
from pygame.locals import *

pygame.init()

WIDTH = 800
HEIGHT = 800

DISPLAYSURFACE = pygame.display.set_mode((800,600))
FPS = 60
fpsClock = pygame.time.Clock()

SPEED = 4.0
direction = [0,0]

WHITE = pygame.Color(255,255,255)
pygame.display.set_caption('Rect')
# rect= pygame.Rect(200,100,50,50)

box = pygame.image.load("box.png")
box = pygame.transform.scale(box, (150, 150))
box_rect = box.get_rect()

box_rect.center = (400,300)

cat_sprite = pygame.image.load("cat_sprite.jpg")

class Cat(pygame.sprite.Sprite):

    def __init__(self) :
        super().__init__()
        self.sprites = []
        self.index = 0
        self.direction = 2
        self.animation = False
        for i in range (7):
            sprite_row = []
            for j in range (8):
                img = cat_sprite.subsurface(
                 (j * 32, i * 32),
                    (32,32)
                )
                sprite_row.append(img)
            self.sprites.append(sprite_row)
        self.image = self.sprites[0][0]
        self.rect = self.image.get_rect()

    def update(self):
        if self.animation:
            self.index += 0.11
            if self.index >= 8 :
                self.index = 0
        else:
            self.index = 0
        self.image = self.sprites[self.direction][int(self.index)]
        self.image = pygame.transform.scale(self.image,(32,32))

cat_sprites = pygame.sprite.Group()

cat = Cat()

cat_sprites.add(cat)

while True:
    DISPLAYSURFACE.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            cat.animation = True
            if event.key == K_UP:
               # rect.move_ip(0,-1 )
               direction[1] = SPEED * -1 
               cat.direction = 3
            if event.key == K_DOWN:
                #rect.move_ip(0,1 )
                direction[1] = SPEED * 1
                cat.direction = 0 
            if event.key == K_LEFT:
                #rect.move_ip(-1,0)
                direction[0] = SPEED * -1 
                cat.direction = 1
            if event.key == K_RIGHT:
                #rect.move_ip(1,0 )
                direction[0] = SPEED * 1 
                cat.direction = 2
                
        if event.type == KEYUP:
            cat.animation = False
            if event.key == K_UP:
               # rect.move_ip(0,-1 )
               direction[1] = 0
            if event.key == K_DOWN:
                #rect.move_ip(0,1 )
                direction[1] = 0
            if event.key == K_LEFT:
                #rect.move_ip(-1,0)
                direction[0] = 0
            if event.key == K_RIGHT:
                #rect.move_ip(1,0 )
                direction[0] = 0

    cat.rect.move_ip(direction[0],direction[1])

    # pygame.draw.rect(DISPLAYSURFACE,(255,100,0),rect , 1)
    # pygame.draw.rect(DISPLAYSURFACE,(255,100,0),rect , 1)
    
    cat_sprites.update()
    cat_sprites.draw(DISPLAYSURFACE)

    if cat.rect.colliderect(box_rect):
        if direction[0] > 0: 
            cat.rect.right = box_rect.left
        elif direction[0] < 0: 
            cat.rect.left = box_rect.right
        elif direction[1] > 0: 
            cat.rect.bottom = box_rect.top
        elif direction[1] < 0:
            cat.rect.top = box_rect.bottom
            
    # if cat.rect.colliderect(rect):
    #     if direction[0] > 0: 
    #         cat.rect.right = rect.left
    #     elif direction[0] < 0:  
    #         cat.rect.left = rect.right
    #     elif direction[1] > 0: 
    #         cat.rect.bottom = rect.top
    #     elif direction[1] < 0:  
    #         cat.rect.top = rect.bottom

    DISPLAYSURFACE.blit(box,box_rect)

    pygame.display.update()
    fpsClock.tick(FPS)
