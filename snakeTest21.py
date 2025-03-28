# importing libraries
import pygame
import time
import random

snake_speed = 10

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
orange = pygame.Color(165, 100, 0)
yellow = pygame.Color(255, 255, 150)

print('orange: ', orange)
gray = pygame.Color(100, 120, 100)

color_arr =[white, green, red, orange]

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('SnakeTest 2.1')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50, white]

# defining first 4 blocks of snake body
snake_body = [[100, 50, green],
              [90, 50, green],
              [80, 50, green],
              [70, 50, white],
              [60, 50, white],
              [50, 50, white]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0
fruit_color = color_arr[random.randrange(2,4)]

# displaying Score function
def show_score(choice, color, font, size):
  
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    game_window.blit(score_surface, score_rect)

# game over function
def game_over():
  
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # after 2 seconds we will quit the program
    time.sleep(2)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()


# Main Function
while True:
    
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two 
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    
    l1 = len(snake_body)-1
    snake_position[2] = snake_body[l1][2]

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    # snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        snake_position[2] = fruit_color
        fruit_spawn = False
        fruit_color = color_arr[random.randrange(0,4)]
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        
    fruit_spawn = True
    game_window.fill(black)

    # print('snake_body:')
    # print(snake_body)
    # inpt = input()
    lenSnake = len(snake_body)
    # for i in range(0,lenSnake-1):
    #     snake_body[i][2]=snake_body[i+1][2]

    snake_body[lenSnake-1][2] = gray

    j=0
    for pos in snake_body:
        if j%2==0:
            pygame.draw.rect(game_window, yellow, pygame.Rect(pos[0], pos[1], 10, 10)) 
        else:
            pygame.draw.rect(game_window, gray, pygame.Rect(pos[0], pos[1], 10, 10)) 
        j = j + 1 
        # if pos[2]==gray:
        #     pygame.draw.rect(game_window, pos[2],
        #                  pygame.Rect(pos[0], pos[1], 10, 10))
        # else:
        #     pygame.draw.rect(game_window, pos[2],
        #                  pygame.Rect(pos[0], pos[1], 15, 15))

        if not (pos[2]==gray or pos[2]==yellow):
            pygame.draw.rect(game_window, pos[2], pygame.Rect(pos[0], pos[1], 15, 15))           
        
    pygame.draw.rect(game_window, fruit_color, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
    
    snake_body.insert(0, list(snake_position))
    # l1 = len(snake_body)-1
    # l1 = 0
    # snake_position[2] = snake_body[l1][2]

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
