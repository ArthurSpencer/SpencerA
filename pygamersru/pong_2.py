import pygame
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
pygame.display.set_caption("Pong")
# - - Exit game flag set to false
done = False
# - - Manages how fast screen refreshes
clock = pygame.time.Clock()

x_direction = 1
y_direction = 1
x_val = 150
y_val = 200
ball_width = 20
x_padd = 0
y_padd = 20
padd_length = 15
padd_width = 60

### - - Game Loop

while not done:
    # - - User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # - write logic that happens on key press here
                y_padd = y_padd - 5
            elif event.key == pygame.K_DOWN:
                # - write logic that happens on key press here
                y_padd = y_padd + 5
            #End If
        #End If
#Next event
    # - - Game logic goes after this comment

    
        #End If
        
    
    if x_val == 640:
        x_direction = x_direction * -1
        y_direction = y_direction
    if x_val == 0: 
        x_direction = x_direction * -1
        y_direction = y_direction
    if y_val == 480:
        x_direction = x_direction
        y_direction = y_direction * -1
    if y_val == 0: 
        x_direction = x_direction
        y_direction = y_direction * -1

    
        
    x_val = x_val + x_direction
    y_val = y_val + y_direction
    
    # - - Screen background is BLACK
    screen.fill (BLACK)

    pygame.draw.rect(screen, WHITE, (x_padd,y_padd,padd_length,padd_width))
    
    # - - Draw here

   

    pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width))
    
    # - - flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit() 
