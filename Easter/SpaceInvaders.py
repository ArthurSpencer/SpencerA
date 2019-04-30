import pygame
import random
import math

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

pygame.init()

size = (480,640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Invaders")

class invader(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed, ex, ey):
        super().__init__()
        self.width = 3
        self.height = 3
        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        #setting position
        self.rect = self.image.get_rect()
        # - Each consecutive invader in loop should have x + 10 - then
        # have a dedicatedy value for that row of invaders
        self.rect.x = (ex)
        self.rect.y = (ey)
        self.speed = speed
    def update(self):
        #Moving the x and y coordinate
        #Maybe have a boundary x coordinate that is constantly changed - when
        #gotten to certain x coordinate - put y coordinate so it goes down and reverse
        #the x coordinate count direction
        #(

invadetype1_list = pygame.sprite.Group()

invaders_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

#Making the first type of invader
ex = 5
ey = 10
for x in range (6):
    
    my_invadertype1 = invader(GREEN, 10, 5, 1, ex, ey)
    invadertype1_list.add(my_invadertype1)
    invaders_list.add(my_invadertype1)
    all_sprites_list.add(my_invadertype1)


while not done:
    # - - User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # -- User inputs here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: # - a key is down
            if event.key == pygame.K_LEFT:# - if the left key pressed
                
                player.player_set_speed(-3) # speed set to -3
            elif event.key == pygame.K_RIGHT: # - if the right key pressed
                player.player_set_speed(3) # speed set to 3
            elif event.type == pygame.K_UP:
                player.bullet_count = player.bullet_count - 1
                my_player = player(Red, 2, 2, 1)
                all_sprites_list.add(my_player)
        if event.key == pygame.K_LEFT or 
    elif event.type == pygame.KEYUP: # - a key released
        event.key == pygame.K_RIGHT:
            player.player_set_speed(0) # speed set to 0

    screen.fill (BLACK)
    # - - Draw here
    all_sprites_list.draw (screen)
    # - - flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()

