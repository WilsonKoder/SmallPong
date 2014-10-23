#Created by Wilson Koder under the GPL-3 license, https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)
#:-) one minor modification to the license though, you don't need to credit me! It would be nice if you did though :-)
#a link to my GitHub would be cool as well :-)

__author__ = 'WilsonKoder'

#imports
import pygame
import pygame.mixer
import random
import sys

#defining some basic colors
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
blue = 0, 255, 0
green = 0, 0, 255

#initialize some modules
pygame.init()
pygame.mixer.init()

#window setup
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pong - Wilson Koder - Started 21/10/14 - wilson@wilsonkoder.com")


#text setup
rallyText = pygame.font.SysFont("Arial", 36)
rally = 0
rallyRender = rallyText.render(str(rally), 1, black, white)

#image loading
paddle1 = pygame.image.load("Images/paddle.png")
paddle2 = pygame.image.load("Images/paddle.png")
ball = pygame.image.load("Images/ball.png")
bg = pygame.image.load("Images/bg.png")

#game variables
running = True

#score variables
score1 = 0
score2 = 0

#position/physics variables
x1 = 5
y1 = 260
x2 = 780
y2 = 260
ball_pos = pygame.math.Vector2(385, 285)
ball_velocity = pygame.math.Vector2(random.randint(-10, 11), random.randint(-10, 11))

#movement variables
paddle1_up = False
paddle1_down = False
paddle2_up = False
paddle2_down = False

#clock...
clock = pygame.time.Clock()

while running:
    #FPS
    clock.tick(60)
    #move ball
    ball_pos += ball_velocity

    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                score1 = 0
                score2 = 0
                ball_velocity = pygame.math.Vector2(random.randint(-10, 11), random.randint(-10, 11))
                ball_pos = pygame.math.Vector2(385, 285)
            if event.key == pygame.K_f:
                ball_velocity = (ball_velocity * 2)
            if event.key == pygame.K_w:
                paddle1_up = True
            if event.key == pygame.K_s:
                paddle1_down = True
            if event.key == pygame.K_UP:
                paddle2_up = True
            if event.key == pygame.K_DOWN:
                paddle2_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                paddle1_up = False
            if event.key == pygame.K_s:
                paddle1_down = False
            if event.key == pygame.K_UP:
                paddle2_up = False
            if event.key == pygame.K_DOWN:
                paddle2_down = False

    # check input bool's
    if paddle1_up:
        y1 -= 10
    if paddle1_down:
        y1 += 10
    if paddle2_up:
        y2 -= 10
    if paddle2_down:
        y2 += 10

    #Audio
    #Collision with top and bottom walls
    if ball_pos[1] > window_size[1] - 30:
        pygame.mixer.music.load("Audio/collision.wav")
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
        ball_velocity[1] = (ball_velocity[1] * -1)

    elif ball_pos[1] < 0:
        pygame.mixer.music.load("Audio/collision.wav")
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
        ball_velocity[1] = (ball_velocity[1] * -1)

    if ball_pos[0] > window_size[0]:
        score2 += 1
        rally = 0
        pygame.mixer.music.load("Audio/endgame.wav")
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
        ball_velocity = pygame.math.Vector2(random.randint(-10, 11), random.randint(-10, 11))
        ball_pos = pygame.math.Vector2(385, 285)

    if ball_pos[0] < 0:
        score1 += 1
        rally = 0
        pygame.mixer.music.load("Audio/endgame.wav")
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
        ball_velocity = pygame.math.Vector2(random.randint(-10, 11), random.randint(-10, 11))
        ball_pos = pygame.math.Vector2(385, 285)


    #Collision Checking - Still glitchy, but we're getting there
    #New Collision Detection from /u/edbluetooth

    if (0 < int(ball_pos[0]) <=30) and (y1 - 45 < int(ball_pos[1]) <= y1 + 45):
        rally += 1
        pygame.mixer.music.load("Audio/hit.wav")
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
        ball_velocity = (ball_velocity * -1)
        ball_velocity[0] = random.randint(1, 11)
        ball_velocity[1] = random.randint(-10, 11)

    if (750 < int(ball_pos[0]) <= 800 - 30) and (y2 - 45 < int(ball_pos[1]) <= y2 + 45):
        rally += 1
        pygame.mixer.music.load("Audio/hit.wav")
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
        ball_velocity = (ball_velocity * -1)
        ball_velocity[0] = random.randint(-11, -1)
        ball_velocity[1] = random.randint(-10, 11)

    #text
    rallyRender = rallyText.render(str(rally), 4, black)
    score1Render = rallyText.render(str(score1), 4, black)
    score2Render = rallyText.render(str(score2), 4, black)

    #clear the screen
    screen.fill(white)

    #draw everything again
    screen.blit(bg, (0, 0))
    screen.blit(paddle1, (x1, y1))
    screen.blit(paddle2, (x2, y2))
    screen.blit(ball, ball_pos)
    screen.blit(rallyRender, (420, 550))
    screen.blit(score1Render, (420, 10))
    screen.blit(score2Render, (360, 10))

    #render it
    pygame.display.flip()
sys.exit()

#~190 LOC, gonna keep it that way ;-) - Feature List: Text for score and rally count, collisions, sound, reset key, and double speed key.