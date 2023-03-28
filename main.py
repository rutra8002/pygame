import pygame
import random

from pygame import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, KEYUP

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
class Player:
    def __init__(self, playerID, x, y):
        self.player_img = pygame.image.load("egg.png")
        self.player = self.player_img.get_rect()
        #self.player_img = pygame.transform.scale(self.player_img, (100, 100))
        self.playerID = playerID
        self.xSpeed = 0
        self.ySpeed = 0
        self.x = x
        self.y = y

    def draw(self, x, y):
        self.player = self.player_img.get_rect()
        screen.blit(self.player_img, (x, y))

player2 = Player(1, 300, 400)



running = True
while running:
    screen.fill((89, 179, 66)) #RGB

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player2.xSpeed = -1
            if event.key == K_RIGHT:
                player2.xSpeed = 1
            if event.key == K_UP:
                player2.ySpeed = -1
            if event.key == K_DOWN:
                player2.ySpeed = 1
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player2.xSpeed = 0
            if event.key == K_UP or event.key == K_DOWN:
                player2.ySpeed = 0

    player2.draw(player2.x + player2.xSpeed, player2.y + player2.ySpeed)
    player2.x += player2.xSpeed
    player2.y += player2.ySpeed
    pygame.display.update()

pygame.quit()
