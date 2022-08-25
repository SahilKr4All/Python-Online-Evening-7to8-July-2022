import pygame

H=500
W=1000
gameBoard = pygame.display.set_mode((W,H))
white = 255,255,255
color = 17,100,200
rect_w=25
rect_h=25
rect_x=0
rect_y=0
move_x=0
move_y=0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x = -1
                move_y = 0
            elif event.key == pygame.K_RIGHT:
                move_x=1
                move_y=0
            elif event.key == pygame.K_UP:
                move_y=-1
                move_x=0
            elif event.key == pygame.K_DOWN:
                move_y=1
                move_x=0
                
    gameBoard.fill(white)
    pygame.draw.rect(gameBoard,color,(rect_x,rect_y,rect_w,rect_h))
    rect_x+=move_x
    rect_y+=move_y

    if rect_x > W-rect_w:
        rect_x=0
    elif rect_x < 0 :
        rect_x = W-rect_w
    if rect_y > H-rect_h:
        rect_y=0
    elif rect_y < 0 :
        rect_y = H-rect_h
    
    pygame.display.update()
