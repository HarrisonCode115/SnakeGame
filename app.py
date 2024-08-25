import pygame
import time
import random

pygame.init()
sWidth = 500
sHeight = 500
snakeSize = int(sWidth/20)
dis=pygame.display.set_mode((sWidth,sHeight))
pygame.display.update()
pygame.display.set_caption('Snake game')

red = (255,0,0)
blue = (0,0,255)
background = (20,20,20)
black = (0,0,0)
green = (0,255,0)
white = (255,255,255)
cyan = (50,50,255)

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [sWidth/3, sHeight/2])



def drawSnake(snakeBody):
    for x in range(len(snakeBody)):
        if(x == len(snakeBody)-1):
            pygame.draw.rect(dis,cyan,[snakeBody[x][0],snakeBody[x][1],snakeSize,snakeSize])
        else:
            pygame.draw.rect(dis,blue,[snakeBody[x][0],snakeBody[x][1],snakeSize,snakeSize])
            



def gameLoop():
    x1 = int(sWidth/2)
    y1 = int(sHeight/2)

   
    
    snakeSpeed = 5
    snakeBody = []
    snakeLength = 1

    xDelta = 0
    yDelta = 0

    game_over=False
    quitStatus = False

    foodX = round(random.randrange(0,sWidth-snakeSize)/snakeSize)*snakeSize
    foodY = round(random.randrange(0,sHeight-snakeSize)/snakeSize)*snakeSize

    while not quitStatus:
        while not game_over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quitStatus = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        xDelta = -snakeSize
                        yDelta = 0
                    elif event.key == pygame.K_d:
                        xDelta = snakeSize
                        yDelta = 0
                    elif event.key == pygame.K_w:
                        yDelta = -snakeSize
                        xDelta = 0
                    elif event.key == pygame.K_s:
                        yDelta = snakeSize
                        xDelta = 0
            x1 += xDelta
            y1 += yDelta

            if(x1 >= sWidth or x1 <= 0 or y1 <= 0 or y1 >= sHeight):
                game_over = True
            
            if(x1 == foodX and y1 == foodY):
                foodX = round(random.randrange(0,sWidth-snakeSize)/snakeSize)*snakeSize
                foodY = round(random.randrange(0,sHeight-snakeSize)/snakeSize)*snakeSize
                snakeLength += 1
                snakeSpeed +=1


            snakeHead = [x1,y1]
            snakeBody.append(snakeHead)
            if(len(snakeBody) > snakeLength):
                del snakeBody[0]

            for body in snakeBody[:-1]:
                if body == snakeHead:
                    game_over = True

            dis.fill(background)
            drawSnake(snakeBody)
            pygame.draw.rect(dis,green,[foodX,foodY,snakeSize,snakeSize])

            #Shows the score
            score = "Score: "+ str(snakeLength-1)
            msg = font_style.render(score, True, white)
            dis.blit(msg,[0,0])
            pygame.display.update()
            clock.tick(snakeSpeed)


        dis.fill(black)
        message("You lost!",red)
        msg = font_style.render("Press enter to play again!", True, white)
        dis.blit(msg,[sWidth/10,sHeight/1.5])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    
                    x1 = int(sWidth/2)
                    y1 = int(sHeight/2)
                    snakeSpeed = 5
                    snakeBody = []
                    snakeLength = 1
                    xDelta = 0
                    yDelta = 0
                    game_over=False
                    quitStatus = False
                    foodX = round(random.randrange(0,sWidth-snakeSize)/snakeSize)*snakeSize
                    foodY = round(random.randrange(0,sHeight-snakeSize)/snakeSize)*snakeSize
                elif event.key == pygame.K_ESCAPE:
                    quitStatus = True
            elif event.type == pygame.QUIT:
                quitStatus = True



    pygame.display.update()
    pygame.quit()
    quit()

gameLoop()


