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
size = (640,640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moving")

screen.fill(BLACK)
pygame.display.flip()
# Screen

class invader(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed, x, y, number):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.number = number
        
    def lookupdate(self):
        #Should change animation of the sprite (all sprite done together)
        pass
    def moveupdate(self, movetype):
        for i in range (11):
            table.append([1,1,1,1,1])
        if movetype == "down":
            pass
        elif movetype == "right":
            self.rect.x = self.rect.x + 10

        elif movetype == "left":
            pass
        #

class player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = (300, size[0] - height)
        self.speed = 0
        
    def playerupdate(self):
        pass

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
firsty = 300
number = 1 
for counter in range(11):
    myinvader = invader(WHITE, 5, 5, 1, firstx, firsty, number)
    #print(myinvader)
    row1.add(myinvader)
    all_sprites_list.add(myinvader)
    firstx = firstx + 10
    number = number + 1

#row2
firstx = 53
firsty = 290
for counter in range(11):
    myinvader = invader(WHITE, 5, 5, 1, firstx, firsty, number)
    row2.add(myinvader)
    all_sprites_list.add(myinvader)
    firstx = firstx + 10
    number = number + 1
#row3
firstx = 53
firsty = 280
for counter in range(11):
    myinvader = invader(WHITE, 5, 5, 1, firstx, firsty, number)
    row3.add(myinvader)
    all_sprites_list.add(myinvader)
    firstx = firstx + 10
    number = number + 1
#row4
firstx = 53
firsty = 270
for counter in range(11):
    myinvader = invader(WHITE, 5, 5, 1, firstx, firsty, number)
    row4.add(myinvader)
    all_sprites_list.add(myinvader)
    firstx = firstx + 10
    number = number + 1
#row5
firstx = 53
firsty = 260
for counter in range(11):
    myinvader = invader(WHITE, 5, 5, 1, firstx, firsty, number)
    row5.add(myinvader)
    all_sprites_list.add(myinvader)
    firstx = firstx + 10
    number = number + 1 
# 5 row - 11 in each row (make each row seperately - (added to different group)
# without pygame working i cant see how the sprites are named



clock = pygame.time.Clock()
#game loop


moveright = True
row1moves = 30
row2moves = 30
row3moves = 30
row4moves = 30
row5moves = 30

while not done:

    if moveright == True:
        if row1moves > 0: 
            row1moves = row1moves - 1
            invader.moveupdate("right")
        
    
    screen.fill (BLACK)
    all_sprites_list.draw (screen)
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()

