import pygame
import random
from pygame.locals import *

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

# player_img = pygame.image.load("face.png")
# player = player_img.get_rect()
# player.x = 400
# player.y = 300
# player_points = 0

# font = pygame.font.Font('RubikWetPaint-Regular.ttf', 32)
# text_img = font.render('0', False, (255, 0, 0) )
# text = text_img.get_rect()
# text.x = 100
# text.y = 550

running = True
while running:
    screen.fill((89, 179, 66)) #RGB

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                print("left")
            if event.key == K_RIGHT:
                print("right")

    pygame.display.update()

pygame.quit()
