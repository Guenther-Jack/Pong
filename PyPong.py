# Hello! My name is Jack Guenther and this was one of my first projects using pygame. Here I practed creating basic shapes and graphics, basic pysics and AI.
# I am continuing to update this program to include more graphics overtime.

import pygame, sys, random

#Animations
def ball_animation ():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= Screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= Screen_width:
        ball_restart()
        
    if ball.colliderect(player_box) or ball.colliderect(opponent):
        ball_speed_x *= -1
        
def player_animation ():
    player_box.y += player_speed
    if player_box.top <=0:
        player_box.top = 0
    if player_box.bottom >= Screen_height:
        player_box.bottom = Screen_height
        
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <=0:
        opponent.top = 0
    if opponent.bottom >= Screen_height:
        opponent.bottom = Screen_height   
        
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (Screen_height/2, Screen_width/2)
    ball_speed_y *= random.choice((-1,1))
    ball_speed_x *= random.choice((-1,1))

    
#set up
pygame.init()
clock = pygame.time.Clock()

#Main Window
Screen_width = 1080
Screen_height = 760
Screen = pygame.display.set_mode((Screen_width,Screen_height))
pygame.display.set_caption('Python Pong')

#Game Rectangles
ball = pygame.Rect(Screen_width/2-15,Screen_height/2-15,30,30)
player_box = pygame.Rect(Screen_width-20,Screen_height/2-70,10,140)
opponent = pygame.Rect(10,Screen_height/2-70,10,140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((-1,1))
ball_speed_y = 7 * random.choice((-1,1))
player_speed = 0
opponent_speed = 7

#Input
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_DOWN:
                player_speed += 7
            if event.key ==pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_DOWN:
                player_speed -= 7
            if event.key ==pygame.K_UP:
                player_speed += 7
 
    ball_animation()
    player_animation()
    opponent_ai()
              
    #Visuals
    Screen.fill(bg_color)
    pygame.draw.rect(Screen,light_grey,player_box)
    pygame.draw.rect(Screen,light_grey,opponent)
    pygame.draw.ellipse(Screen,light_grey,ball)
    pygame.draw.aaline(Screen, light_grey, (Screen_width/2,0), (Screen_width/2,Screen_height))
        
    pygame.display.flip()
    clock.tick(60)