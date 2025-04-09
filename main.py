import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong")

ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20)
paddle1 = pygame.Rect(30, HEIGHT // 2 - 70, 10, 140)
paddle2 = pygame.Rect(WIDTH - 40, HEIGHT // 2 - 70, 10, 140)

#start settings

BALL_SPEED_X, BALL_SPEED_Y = 5, 5
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y
PADDLE_SPEED = 10

#main loop
while True:
    #quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #upravlenie

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y = paddle1.y - PADDLE_SPEED
    if keys[pygame.K_w] and paddle1.bottom < HEIGHT:
        paddle1.y = paddle1.y + PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y = paddle2.y - PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y = paddle2.y + PADDLE_SPEED
