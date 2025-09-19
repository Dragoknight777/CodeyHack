import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


ball_img = pygame.image.load('./content/Soccerball.svg')  # Use a local soccer ball image
ball_rect = ball_img.get_rect()
angle = 0
x, y = 0, 300
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x += speed
    angle += 10
    if x > 800:
        x = -ball_rect.width

    screen.fill((34, 139, 34))  # Soccer field green
    rotated_ball = pygame.transform.rotate(ball_img, angle)
    ball_rect = rotated_ball.get_rect(center=(x, y))
    screen.blit(rotated_ball, ball_rect)
    pygame.display.flip()
    clock.tick(60)