import pygame
import sys
import pygame_menu
import pygame_menu.events
import pygame_menu.themes

pygame.init()

WIDTH, HEIGHT = 800, 600
white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong")

ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20)
paddle1 = pygame.Rect(30, HEIGHT // 2 - 70, 10, 100)
paddle2 = pygame.Rect(WIDTH - 40, HEIGHT // 2 - 70, 10, 100)
center_line = pygame.Rect(WIDTH // 2, 0, 1, HEIGHT)
font_style = pygame.font.SysFont(None, 25)
def text_vyvod(text, color, x, y):
    text = str(text)
    txxt = font_style.render(text, True, color)
    screen.blit(txxt, (x,y))

#start settings

BALL_SPEED_X, BALL_SPEED_Y = 10, 10
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y
PADDLE_SPEED = 10

#main loop
def start_the_game(player1_name, player2_name):
    global ball_speed_y, ball_speed_x
    ball.center = (WIDTH // 2, HEIGHT // 2)
    paddle1.centery = HEIGHT // 2
    paddle2.centery = HEIGHT // 2

    score1 = 0
    score2 = 0

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
        if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
            paddle1.y = paddle1.y + PADDLE_SPEED
        if keys[pygame.K_UP] and paddle2.top > 0:
            paddle2.y = paddle2.y - PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
            paddle2.y = paddle2.y + PADDLE_SPEED

        #gBu}|{eHue M94a

        ball.x = ball.x + ball_speed_x
        ball.y = ball.y + ball_speed_y

        #oTckok M94a oT cTeH

        if ball.top < 0 or ball.bottom > HEIGHT:
            ball_speed_y = -ball_speed_y
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_speed_x = -ball_speed_x

        #TTpoBepka Bblxoga 3a TTpegeJIbl 3kpaHa

        # if ball.left <= 0 or ball.right >= WIDTH:
        #     ball.x = WIDTH // 2
        #     ball.y = HEIGHT // 2
        #     ball_speed_x = BALL_SPEED_X * (-1 if ball.left >= 0 else 1)

        if ball.left <= 0:
            score2 += 1
            ball.x = WIDTH // 2
            ball.y = HEIGHT // 2
            ball_speed_x = -BALL_SPEED_X

        if ball.right >= WIDTH:
            score1 += 1
            ball.x = WIDTH // 2
            ball.y = HEIGHT // 2
            ball_speed_x = BALL_SPEED_X

        #OTpucoBka

        screen.fill(black)
        pygame.draw.ellipse(screen, (255, 255, 255), ball)
        pygame.draw.rect(screen, (255, 255, 255), paddle1)
        pygame.draw.rect(screen, (255, 255, 255), paddle2)
        pygame.draw.rect(screen, (white), center_line)

        #text

        text_vyvod(f"{player1_name}: {score1}", (255,255,255), 20, 20)
        text_vyvod(f"{player2_name}: {score2}", (255,255,255), WIDTH - 150, 20)

        pygame.display.flip()
        pygame.time.delay(60)

menu = pygame_menu.Menu(
    height=HEIGHT,
    theme=pygame_menu.themes.THEME_DARK,
    title='POSHUMIM',
    width=WIDTH
)

p1_input = menu.add.text_input('Name :', default='MC Sleva')
p2_input = menu.add.text_input('Name :', default='MC Sprava')

menu.add.button('Play', lambda: start_the_game(p1_input.get_value(), p2_input.get_value()))
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)

pygame.quit()
sys.exit()

