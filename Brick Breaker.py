import pygame
import random
H=500
W=1000
gameBoard = pygame.display.set_mode((W,H))
white = 255,255,255


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

     
    gameBoard.fill(white)
    for i in range(0,10):
        for j in range(0,5):
            color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
            pygame.draw.rect(gameBoard,color,(i*110,j*60,100,50))
            
    
    pygame.display.update()
