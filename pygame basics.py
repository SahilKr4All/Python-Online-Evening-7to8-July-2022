import pygame

W=800
H=600
color = 255,255,255#rgb-red green blue-0-255
red=255,0,0
gameBoard = pygame.display.set_mode((W,H))
play=True
rect_x=0
rect_y=0
rect_w=100
rect_h=100
move_x=0
move_y=0
frogImg=pygame.image.load("frog.png")
frogImg=pygame.transform.scale(frogImg,(100,100))
while play ==True:
    gameBoard.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                move_x = -1
                move_y=0
            elif event.key==pygame.K_RIGHT:
                move_x = 1
                move_y=0
            elif event.key==pygame.K_UP:
                move_y =-1
                move_x=0
            elif event.key==pygame.K_DOWN:
                move_y=1
                move_x=0

    frog=pygame.draw.rect(gameBoard,red,[rect_x,rect_y,rect_w,rect_h])
    gameBoard.blit(frogImg,(rect_x,rect_y))
    
    rect_x+=move_x
    rect_y+=move_y

    if rect_x>W-rect_w:
        rect_x=0
    elif rect_x<0:
        rect_x = W-rect_w
    elif rect_y>H-rect_h:
        rect_y=0
    elif rect_y<0:
        rect_y=H-rect_h
    
    
    pygame.display.update()
    
