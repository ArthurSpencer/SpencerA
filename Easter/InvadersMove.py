import pygame
import random
import math

table = []
    for i in range (11):
    table.append([1,1,1,1,1])
#Table with 11 columns and 5 values in each column corresponding to each alien in that column


BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

pygame.init()

# Screen
FPS = 60
size(640,640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moving")

screen.fill(BLACK)
pygame.display.flip()
# Screen

class invader(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 400)
        self.speed = speed
        
    def lookupdate(self):
        #Should change animation of the sprite (all sprite done together)

    def moveupdate(self):for i in range (11):
    table.append(
[1,1,1,1,1])
        #

class player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = (300, size[0] - height)
        self.speed = 0
        
    def playerupdate(self):

done = False
row1 = pygame.sprite.Group()
row2 = pygame.sprite.Group()
row3 = pygame.sprite.Group()
row4 = pygame.sprite.Group()
row5 = pygame.sprite.Group()
Invader_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

#row1
firstx = 53
for counter in range(11):
    invader = invader(White, 5, 5, 1)
    row1.add(invader)
    all_sprites_list.add(my_snow)
    firstx = firstx + 53


# 5 row - 11 in each row (make each row seperately - (added to different group)
