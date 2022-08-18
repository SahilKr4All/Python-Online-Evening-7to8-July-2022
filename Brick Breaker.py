import pygame
import random
H=500
W=1000
gameBoard = pygame.display.set_mode((W,H))
white = 255,255,255
black = 0,0,0
blue = 0,0,255
brick_w = 80
brick_h=25
player_w=150
player_h=15
player_x=W/2 - player_w/2
player_y=H-player_h-10
ball_r=10
ball_x=player_x+player_w/2+ball_r/2
ball_y=H-player_h

move_x=0
move_y=0
brick_list=[]

for i in range(0,12):
    for j in range(0,10):
        brick_list.append(pygame.rect(i*100,j*30,brick_w,brick_h))
        
while True:
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x=-10
            elif event.key == pygame.K_RIGHT:
                move_x=10
            elif event.key == pygame.K_SPACE:
                move_y = -10
            

     
    gameBoard.fill(white)

          
    for i in range(len(brick_list)):
            color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
            pygame.draw(gameBoard,color,brick_list[i])
            
    rect = pygame.draw.rect(gameBoard,black,(player_x,player_y,player_w,player_h))
    ball = pygame.draw.circle(gameBoard,blue,(ball_x,ball_y-player_h),ball_r)

    for i in range(len(brick_list)):
        if pygame.rect(brick_list[i]).collide_rect(ball):
            print("Collision")
    

    player_x+=move_x
    ball_x+=move_x

    ball_y+=move_y

    if player_x > W-player_w:
        move_x=-1
    elif player_x<0:
        move_x=1
    pygame.display.update()
