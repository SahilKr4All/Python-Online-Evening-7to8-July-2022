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
bar_w=150
bar_h=15
bar_x=W/2 - bar_w/2
bar_y=H-bar_h-10
ball_r=10
ball_x=bar_x+bar_w/2+ball_r/2
ball_y=H-bar_h

move_x=0

move_ball_x=0
move_ball_y=0
brick_list=[]

rows = 5
cols = W//brick_w

for i in range(rows):
    for j in range(cols):
        rect = pygame.Rect(j*(brick_w+5),i*(brick_h+5),brick_w,brick_h)
        brick_list.append(rect)

while True:
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x=-1
            elif event.key == pygame.K_RIGHT:
                move_x=1
            elif event.key == pygame.K_SPACE:
                move_ball_y = -1
        else:
            move_x=0


     
    gameBoard.fill(white)

          
    for i in range(len(brick_list)):
            color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
            pygame.draw.rect(gameBoard,color,brick_list[i])
            
    rect = pygame.draw.rect(gameBoard,black,(bar_x,bar_y,bar_w,bar_h))
    ball=pygame.draw.circle(gameBoard,blue,(ball_x,ball_y-bar_h),ball_r)
            
    for i in range(len(brick_list)):
        if brick_list[i].colliderect(ball):
            del brick_list[i]
            move_ball_y=1
            break

    bar_x+=move_x
    ball_x+=move_x

    ball_y+=move_ball_y

    

    if bar_x > W-bar_w:
        move_x=-1
    elif bar_x<0:
        move_x=1

    if rect.colliderect(ball):
        move_ball_y=-1
    elif ball_y<0:
        move_ball_y=1
    elif ball_y>H+ball_r:
        ball_x=bar_x+bar_w/2+ball_r/2
        ball_y=H-bar_h
    
    pygame.display.update()