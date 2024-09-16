import pygame
import math

pygame.init()

root = pygame.display.set_mode((700, 700))
pygame.display.set_caption('CLICK_BOOM')

BLACK = (0, 0, 0)
RED = (225, 0, 50)

l_ps = None
ball_radius = 20
ball_pos = None
ball_speed = 1
ball_direction = (0, 0)
square_size = 40
is_ball = True

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                l_ps = event.pos
                ball_pos = list(l_ps)
                angle = math.radians(-90)
                ball_direction = (math.cos(angle), math.sin(angle))

    if ball_pos:
        ball_pos[0] += ball_direction[0] * ball_speed
        ball_pos[1] += ball_direction[1] * ball_speed

        if (ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > 700 or
                ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > 700):
            is_ball = False
            ball_pos = [min(max(ball_pos[0], square_size // 2), 700 - square_size // 2),
                        min(max(ball_pos[1], square_size // 2), 700 - square_size // 2)]

    root.fill(BLACK)

    if ball_pos:
        if is_ball:
            pygame.draw.circle(root, RED, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
        else:
            pygame.draw.rect(root, RED, pygame.Rect(ball_pos[0] - square_size // 2,
                                                    ball_pos[1] - square_size // 2,
                                                    square_size, square_size))

    pygame.display.update()

pygame.quit()
