#importing libraries crucial to running of the game
import pygame 
import random
import time
#game window

#snak default speed 
snake_speed = 20


#game screen size 
screen_height=480
screen_width=720

#assigning colours with pygame, making it easier to assign colours within the game
black= (0,0,255)
white= (255,255,255)
red= (255,0,0)
green= (0,255,0)
blue= (0,0,255)

#initialising pygame and 
pygame.init()

#opening game window
pygame.display.set_caption ('Snake Game Xtreme')
game_screen=pygame.display.set_mode((screen_width,screen_height))

#frames per second controller
fps=pygame.time.Clock()


#assigning default snake position
snake_start_position= [100,50]


#assigning the first 3 blocks of the snake
#body
snake_main_body=[[100,50],
                    [90,50],
                    [80,50]]

#food position 
#creating a randomiser for the position of the food 
food_position= [random.randrange(1,(screen_width//10))*10,
                random.randrange(1,(screen_height//10))*10]
#food will spawn 
food_spawn=True
#set default spawn direction of snake to right so player has time to react as it spawns on left side of screen
#directio is right facing
direction= 'RIGHT'
change_to = direction


#scoring system 
#starting score 
score=0
#displaying score function
def show_score(choice,color,font,size):
    #create font object 
    score_font=pygame.font.SysFont(font,size)

    #creating display object
    #score layer
    score_layer=score_font.render('Score : '+ str(score),True,color)

    #creating a rectangle for the text 
    score_rectangle= score_layer.get_rect()

    #displaying the text
    game_screen.blit(score_layer, score_rectangle)



#game over function
def game_over():
    #creating object for font 
    my_font=pygame.font.SysFont('gothic', 50)
    
    #creating the layer which the text will show
    game_over_layer= my_font.render('Your score is : '+str(score),True,red)

    #creating rectangle layer for the font and the text
    game_over_rectangle=game_over_layer.get_rect()

    #positioning of the text
    game_over_rectangle.midtop=(screen_height/2, screen_width/4)

    #blit draws text on the screen
    game_screen.blit(game_over_layer,game_over_rectangle)
    pygame.display.flip()

    #after 5 seconds program will close
    time.sleep(5)

    #deactivating the pygame library, for cleanliness purposes
    pygame.quit

    #quitting the program altogether
    quit()

#Movement function that persists throughout the game, will also be able to adjust for double pressing keys, for example if the player is holding down a key and presses another
#the most recent keypress is taken to avoid movement issues within the game

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key ==pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to='RIGHT'
        
    #addressing the simultaneous keypress issue here, stops snake trying to go two different ways at the same time
    if change_to=='UP' and direction != 'DOWN':
        direction='UP'
    if change_to=='DOWN' and direction != 'UP' :
        direction='DOWN'
    if change_to=='LEFT' and direction != 'RIGHT':
        direction= 'LEFT'
    if change_to=='RIGHT'and direction != 'LEFT':
        direction = 'RIGHT'

    #snake movement 
    if direction == 'UP':
        snake_start_position[1]-=10
    if direction == 'DOWN':
        snake_start_position[1]+=10
    if direction == 'LEFT':
        snake_start_position[0]-=10
    if direction =='RIGHT':
        snake_start_position[0]+=10

    
    #food system and growing of the snake, making sure that when snake collides with food a point is achieved, increments of 1 point using .pop to eliminate the element when it collides
    snake_main_body.insert(0,list(snake_start_position))
    if snake_start_position[0]==food_position[0] and snake_start_position[1]== food_position[1]:
        score +=1
        food_spawn= False   
    else: 
        snake_main_body.pop()
    
    if not food_spawn:
        food_position = [random.randrange(1,(screen_height//10))*10,
                     random.randrange(1,(screen_width//10))*10]
    
    food_spawn = True
    game_screen.fill (black)
    
    for pos in snake_main_body:
        pygame.draw.rect(game_screen,green,
                         pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(game_screen, white, pygame.Rect(
        food_position[0], food_position[1],10,10))
    


    #game ending conditions 
    if snake_start_position[0]<0 or snake_start_position[0]>screen_width-10:
        game_over()
    if snake_start_position[1]<0 or snake_start_position[1]>screen_height-10:
        game_over()

    #touching the snakes own body to cause game over condition
    for block in snake_main_body[1:]:
        if snake_start_position[0]==block[0] and snake_start_position[1]== block[1]:
            game_over()

    #showing the score all the time for the player to see
    show_score(1,white,'gothic',20)

    #refreshing the game screen in line with the frames per second to ensure the game is smooth as possible.
    pygame.display.update()

    #frame per second /refresh rate
    fps.tick(snake_speed)



#Bonus features added here







