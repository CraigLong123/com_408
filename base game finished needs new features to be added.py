import pygame 
import random
import time

# Initialize pygame
pygame.init()

# Game window settings
screen_height = 480
screen_width = 720
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game Xtreme')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Snake main body and setting start position and direction
snake_speed = 15
snake_block = 10
snake_start_position = [100, 50]
snake_main_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction

# Food settings, where the food spawns and when 
food_position = [random.randrange(1, (screen_width // 10)) * 10,
                 random.randrange(1, (screen_height // 10)) * 10]
food_spawn = True

# Score keeps score at 0 on start of the game
score = 0

# Frame controller
fps = pygame.time.Clock()

# Displaying score function, scoreboard that displays the score and ensures that it is visible and correct 
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_screen.blit(score_surface, score_rect)

# Game over function, making sure that when the game ends that it will pause to let the player see their score and make sure that it will auto reset after some time
def game_over():
    my_font = pygame.font.SysFont('gothic', 50)
    game_over_surface = my_font.render('Your score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width / 2, screen_height / 4)
    game_screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

# Main logic, direction of the snake and ensuring that you cannot flip back on yourself for example you cannot go up then down immediately.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
    
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    if direction == 'UP':
        snake_start_position[1] -= snake_block
    if direction == 'DOWN':
        snake_start_position[1] += snake_block
    if direction == 'LEFT':
        snake_start_position[0] -= snake_block
    if direction == 'RIGHT':
        snake_start_position[0] += snake_block
    
    snake_main_body.insert(0, list(snake_start_position))
    if snake_start_position[0] == food_position[0] and snake_start_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_main_body.pop()
    
    if not food_spawn:
        food_position = [random.randrange(1, (screen_width // 10)) * 10,
                         random.randrange(1, (screen_height // 10)) * 10]
    food_spawn = True

    game_screen.fill(black)

    for pos in snake_main_body:
        pygame.draw.rect(game_screen, green, pygame.Rect(pos[0], pos[1], snake_block, snake_block))
    pygame.draw.rect(game_screen, white, pygame.Rect(food_position[0], food_position[1], snake_block, snake_block))

    if snake_start_position[0] < 0 or snake_start_position[0] > screen_width - snake_block:
        game_over()
    if snake_start_position[1] < 0 or snake_start_position[1] > screen_height - snake_block:
        game_over()

    for block in snake_main_body[1:]:
        if snake_start_position[0] == block[0] and snake_start_position[1] == block[1]:
            game_over()

    show_score(white, 'gothic', 20)
    pygame.display.update()
    fps.tick(snake_speed)

    # base game completed above new features should be added below, new aim features time limit and speed change