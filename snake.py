import pygame
import time
import random
import sys

pygame.init()
pygame.display.init()


#difficulty=15

screen_width=800
screen_height=600

display=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake")

fps=pygame.time.Clock()


font_style = pygame.font.SysFont(None, 30)
def message(msg,color):
    mesg=font_style.render(msg, True, color)
    display.blit(mesg, [screen_width/4, screen_height/2])



def gameOver(gameOver,gameExit):
    gameContinue=False
    message("You lost! Press 1 to play again or Esc to close",(255,0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameOver = True
                gameExit = False
                sys.exit()
            if event.key == pygame.K_1:
                gameLoop()


def showScore(score):
    score_font=pygame.font.SysFont("times new roman", 20)
    score_text=score_font.render('Score:' + str(score),True,(255,255,255))
    score_box=score_text.get_rect()
    score_box.midtop=(screen_width/20,10)
    display.blit(score_text, score_box)



def gameLoop():

    difficulty=15

    snake=[screen_height/2,screen_width/2]
    snake_body=[[screen_height/2, screen_width], [screen_height/2-10, screen_width/2], [screen_height/2-20, screen_width/2]]

    food = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
    food_spawn=True

    score=0
    initialScore=1

    direction = 'UP'
    change_direction = direction

    gameContinue=False
    gameExit=False

    while not gameContinue:
        while gameExit==True:
            gameOver(gameOver,gameExit)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_direction = 'UP'
                if event.key == pygame.K_DOWN:
                    change_direction = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_direction = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_direction = 'RIGHT'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        if change_direction == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_direction == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_direction == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_direction == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake[1] -= 10
        if direction == 'DOWN':
            snake[1] += 10
        if direction == 'LEFT':
            snake[0] -= 10
        if direction == 'RIGHT':
            snake[0] += 10

        snake_body.insert(0, list(snake))
        
        if snake[0]==food[0] and snake[1]==food[1]:
            score += 1
            if score==initialScore+10:
                difficulty=difficulty+5
                initialScore=score
            showScore(score)
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
        food_spawn = True     

        display.fill((0,0,0))

        for pos in snake_body:
            pygame.draw.rect(display, (83, 79, 5), pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.draw.rect(display, (255,0,0), pygame.Rect(food[0], food[1], 10, 10))

        if snake[0] < 0 or snake[0] > screen_width-10:
            gameExit=True
        if snake[1] < 0 or snake[1] > screen_height-10:
            gameExit=True
        

        for block in snake_body[1:]:
            if snake[0] == block[0] and snake[1] == block[1]:
                gameExit=True

        showScore(score)

        pygame.display.update()

        fps.tick(difficulty)

gameLoop()