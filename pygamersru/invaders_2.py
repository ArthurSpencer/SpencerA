import pygame
import random
import math


# - - Global Constants

# - - Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# - - Initialise PyGame
pygame.init()

# - - Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# - - Title of new window/screen
pygame.display.set_caption("Snow")

## -- Classes
## -- Define the class snow which is a sprite
class invader(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height, speed):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(-25, 400)
        self.speed = speed
    #End Procedure
    # Class update function - runs for each pass through the game loop

    def update(self):
        self.rect.y = self.rect.y + self.speed
    
    # Set speed of the sprite
#End Class

class player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed, lives):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = (300, size[0] - height)
        self.speed = 0
        self.lives = 5
        self.bullet_count = 60
        self.score = 0
        
    def update(self):
        self.rect.y = self.rect.y + self.speed


class bullet(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed, lives):
        super().__init__()
        self.image = pygame.Surface([2,2])
        self.image.fill(color)
        self.rect = (player)
        self.speed = 2

    def update(self):
        self.rect.y = self.rect.y + self.speed


# - - Exit game flag set to false
done = False
# Create a list of the snow blocks

Invader_list = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_list = pygame.sprite.Group()

# Create the snowflakes
number_of_flakes = 10 # we are creating 50 snowflakes
for x in range(number_of_flakes):
    my_invader = invader(WHITE, 10, 10, 1) # snowflakes are white with size 5 by 5 px
    invader_list.add(my_Invader) # adds the new snowflake to the group of snowflakes
    all_sprites_list.add(my_Invader) # adds it to the group of all Sprites
#Next x

for x in range(bullet_group):
    bullet_hit_group = 

my_player = player(Yellow, 10, 10, 1)
    all_sprites_list.add(my_player)

# - - Manages how fast screen refreshes
clock = pygame.time.Clock()

### - - Game Loop

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

    

    
        #End If
    #Next event
    # - - Game logic goes after this comment
    all_sprites_list.update()
    # -- when invader hits the player add 5 to score.
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
    for foo in player_hit_group:
        player.lives = player.lives - 1


    
    

    
    # - - Screen background is BLACK
    screen.fill (BLACK)
    # - - Draw here
    all_sprites_list.draw (screen)
    # - - flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit() 
