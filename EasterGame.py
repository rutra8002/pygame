import pygame
import random
import sys
from pygame.locals import *

pygame.init()

width = 1200
height = 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

speed = 0.5

MAX_EGGS = 2

f = open("options.txt", "r")

GAMEMODE = f.readline()
GAMEMODE = GAMEMODE.strip()
MAX_EGGS = int(f.readline())
POINTS = 0
POINTS1 = 0

COLLECTED_EGGS = [0] * 16

obstacles = []
obstacles2 = []

max_obstacles = 10
current_obstacles = 0
current_obstacles2 = 0


class Egg:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.Visible = True
        self.egg_img = pygame.image.load("./img/egg.png")
        self.egg_img = pygame.transform.scale(self.egg_img, (100, 100))

    def draw(self):
        screen.blit(self.egg_img, (self.x, self.y))
        if GAMEMODE == "EASY":
            num = 0
            if self.num == 'F':
                num = 15
            elif self.num == 'E':
                num = 14
            elif self.num == 'D':
                num = 13
            elif self.num == 'C':
                num = 12
            elif self.num == 'B':
                num = 11
            elif self.num == 'A':
                num = 10
            else:
                num = int(self.num)

            if num % 2 == 0:
                number = EggFont.render(self.num, True, blue)
            else:
                number = EggFont.render(self.num, True, (255, 0, 0))
        else:
            number = EggFont.render(self.num, True, (255, 255, 255))
        screen.blit(number, (self.x + 28, self.y + 15))


class Player:
    def __init__(self, playerID, x, y):
        if GAMEMODE != "IMPOSSIBLE" and playerID == 1:
            self.player_img = pygame.image.load("./img/bunny.png")
        elif GAMEMODE != "IMPOSSIBLE" and playerID != 1:
            self.player_img = pygame.image.load("./img/bunny1.png")
        else:
            self.player_img = pygame.image.load("./img/bunny2.png")

        self.player = self.player_img.get_rect()
        self.player_img = pygame.transform.scale(self.player_img, (100, 100))
        self.playerID = playerID
        self.xSpeed = 0
        self.ySpeed = 0
        self.x = x
        self.y = y

    def draw(self, x, y):
        self.player = self.player_img.get_rect()
        screen.blit(self.player_img, (x, y))





class Square():
    def __init__(self, x, y, l):
        self.x = x
        self.y = y
        self.l = l

    def center(self):
        return (self.x + self.l / 2, self.y + self.l / 2)

    def isIntersecting(self, square):
        if ((abs(abs(self.center()[0]) - abs(square.center()[0])) < self.l / 2 + square.l / 2) and abs(
                abs(self.center()[1]) - abs(square.center()[1])) < self.l / 2 + square.l / 2):
            return True
        return False

    def IntersectList(self, squareList):
        counter = 0
        for item in squareList:
            for item2 in squareList:
                if not (item.isIntersecting(item2)):
                    counter += 1
        return counter


class obstacle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, 40, 40)

    def draw(self):
        if GAMEMODE == "IMPOSSIBLE":
            pygame.draw.rect(screen, (255, 255, 255), self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

def show_menu():
    global MAX_EGGS  # we need to use the global variable MAX_EGGS
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((89, 179, 66))
        title = bigFont.render("Game Menu", True, (0, 0, 0))
        title_rect = title.get_rect(center=(width/2, 200))
        screen.blit(title, title_rect)

        # render the current value of MAX_EGGS
        max_eggs_text = font.render(f"Eggs: {MAX_EGGS}", True, (0, 0, 0))
        max_eggs_rect = max_eggs_text.get_rect(center=(width/2, 300))
        screen.blit(max_eggs_text, max_eggs_rect)

        easy = font.render("Easy", True, (0, 0, 0))
        easy_rect = easy.get_rect(center=(width/2, 400))
        screen.blit(easy, easy_rect)

        medium = font.render("Medium", True, (0, 0, 0))
        medium_rect = medium.get_rect(center=(width/2, 500))
        screen.blit(medium, medium_rect)

        hard = font.render("Hard", True, (0, 0, 0))
        hard_rect = hard.get_rect(center=(width/2, 600))
        screen.blit(hard, hard_rect)

        impossible = font.render("Impossible", True, (0, 0, 0))
        impossible_rect = impossible.get_rect(center=(width/2, 700))
        screen.blit(impossible, impossible_rect)

        # check for mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Check if left mouse button is clicked
                pos = pygame.mouse.get_pos()

                if easy_rect.collidepoint(pos):
                    global GAMEMODE
                    GAMEMODE = "EASY"
                    return

                if medium_rect.collidepoint(pos):
                    GAMEMODE = "MEDIUM"
                    return

                if hard_rect.collidepoint(pos):
                    GAMEMODE = "HARD"
                    return

                if impossible_rect.collidepoint(pos):
                    GAMEMODE = "IMPOSSIBLE"
                    return

                # if the user clicks on the "Max Eggs" text, allow them to change the value
                if max_eggs_rect.collidepoint(pos):
                    MAX_EGGS += 1  # increase the value of MAX_EGGS by 1
                    if MAX_EGGS > 16:
                        MAX_EGGS = 2  # if MAX_EGGS is greater than 16, reset it to 2

        pygame.display.update()

running = True

displayedEggs = 0
Eggs = []
prevNums = []

gameActive = True

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
yellow = (245, 236, 66)
X = 1950
Y = 100
X1 = 400
Y1 = 100

font = pygame.font.Font('./fonts/Font.ttf', 64)
bigFont = pygame.font.Font('./fonts/Font.ttf', 120)
EggFont = pygame.font.Font('./fonts/Font.ttf', 80)

text = font.render('Points: ' + str(POINTS), True, (0, 0, 255))
text2 = font.render('Points: ' + str(POINTS1), True, (255, 0, 0))

textRect = text.get_rect()
text2Rect = text2.get_rect()

textRect.center = (X // 2, Y // 2)
text2Rect.center = (X1 // 2, Y1 // 2)

subtitle1 = font.render('EVEN', True, (0, 0, 255))
subtitle2 = font.render('ODD ', True, (255, 0, 0))
show_menu()
player1 = Player(1, 300, 400)
player2 = Player(2, 800, 800)
while running:

    if GAMEMODE == "IMPOSSIBLE":
        text = font.render('Points: ' + str(POINTS), True, (255, 255, 255))
        text2 = font.render('Points: ' + str(POINTS1), True, (255, 255, 255))
        screen.fill((0, 0, 0))  # RGB
    else:
        text = font.render('Points: ' + str(POINTS), True, (0, 0, 255))
        text2 = font.render('Points: ' + str(POINTS1), True, (255, 0, 0))
        screen.fill((89, 179, 66))  # RGB

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if gameActive:
                if event.key == K_LEFT:
                    player1.xSpeed = -speed
                if event.key == K_RIGHT:
                    player1.xSpeed = speed
                if event.key == K_UP:
                    player1.ySpeed = -speed
                if event.key == K_DOWN:
                    player1.ySpeed = speed
                if event.key == K_p and current_obstacles < max_obstacles:
                    obstacles.append(obstacle(player1.x, player1.y, (255, 0, 0)))
                    current_obstacles += 1
                if event.key == K_a:
                    player2.xSpeed = -speed
                if event.key == K_d:
                    player2.xSpeed = speed
                if event.key == K_w:
                    player2.ySpeed = -speed
                if event.key == K_s:
                    player2.ySpeed = speed
                if event.key == pygame.K_e and current_obstacles2 < max_obstacles:
                    obstacles2.append(obstacle(player2.x, player2.y, (0, 0, 255)))
                    current_obstacles2 += 1
            #### RESTART ####
            if event.key == K_r and gameActive == False:
                player1.x = 300
                player1.y = 400
                player2.y = 800
                player2.x = 800
                POINTS = 0
                POINTS1 = 0
                speed = 0.5
                obstacles.clear()
                obstacles2.clear()
                current_obstacles2 = 0
                current_obstacles = 0
                displayedEggs = 0
                Eggs.clear()
                prevNums.clear()
                COLLECTED_EGGS = [0] * 16
                gameActive = True

        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player1.xSpeed = 0
            if event.key == K_UP or event.key == K_DOWN:
                player1.ySpeed = 0
            if event.key == K_a or event.key == K_d:
                player2.xSpeed = 0
            if event.key == K_w or event.key == K_s:
                player2.ySpeed = 0
    # if current_obstacles != max_obstacles:
    player1.draw(player1.x + player1.xSpeed, player1.y + player1.ySpeed)
    player1.x += player1.xSpeed
    player1.y += player1.ySpeed
    if player1.x < -100:
        player1.x = width + 100
    if player1.x > width + 100:
        player1.x = -100
    if player1.y < -100:
        player1.y = height + 100
    if player1.y > height + 100:
        player1.y = -100

    player2Square = Square(player2.x, player2.y, 100)
    player1Square = Square(player1.x, player1.y, 100)
    for item in obstacles:
        item.draw()
        itemSquare = Square(item.x, item.y, 40)
        if player2Square.isIntersecting(itemSquare) or gameActive == False:
            gameActive = False
            gameOver = bigFont.render('GAME OVER', True, (255, 255, 255))
            endPoints = font.render('Points: ' + str(POINTS), True, (0, 0, 255))
            endPoints2 = font.render('Points: ' + str(POINTS1), True, (255, 0, 0))
            restart = font.render('Press R to restart', True, (255, 255, 255))
            screen.blit(endPoints, (250, 550))
            screen.blit(endPoints2, (650, 550))
            screen.blit(gameOver, (300, 400))
            screen.blit(restart, (360, 650))
        else:
            screen.blit(text, textRect)
            screen.blit(text2, text2Rect)
            if GAMEMODE != "HARD" and GAMEMODE != "IMPOSSIBLE":
                screen.blit(subtitle1, ((X - 150) // 2, (Y + 100) // 2))
                screen.blit(subtitle2, ((X1 - 170) // 2, (Y1 + 100) // 2))

    if len(obstacles) == 0 and gameActive == True:
        screen.blit(text, textRect)
        screen.blit(text2, text2Rect)
        if GAMEMODE != "HARD" and GAMEMODE != "IMPOSSIBLE":
            screen.blit(subtitle1, ((X - 150) // 2, (Y + 100) // 2))
            screen.blit(subtitle2, ((X1 - 170) // 2, (Y1 + 100) // 2))
    for item in obstacles2:
        item.draw()
        itemSquare = Square(item.x, item.y, 40)
        if player1Square.isIntersecting(itemSquare) or gameActive == False:
            gameActive = False
            gameOver = bigFont.render('GAME OVER', True, (255, 255, 255))
            EggDisplay = font.render('Eggs: 0 1 2 3 4 5 6 7 8 9 A B C D E F', True, yellow)
            CollectedEggDisplay = font.render(
                'Collected: ' + str(COLLECTED_EGGS[0]) + " " + str(COLLECTED_EGGS[1]) + " " + str(
                    COLLECTED_EGGS[2]) + " " + str(COLLECTED_EGGS[3]) + " " + str(COLLECTED_EGGS[4]) + " " + str(
                    COLLECTED_EGGS[5]) + " " + str(COLLECTED_EGGS[6]) + " " + str(COLLECTED_EGGS[7]) + " " + str(
                    COLLECTED_EGGS[8]) + " " + str(COLLECTED_EGGS[9]) + " " + str(COLLECTED_EGGS[10]) + " " + str(
                    COLLECTED_EGGS[11]) + " " + str(COLLECTED_EGGS[12]) + " " + str(COLLECTED_EGGS[13]) + " " + str(
                    COLLECTED_EGGS[14]) + " " + str(COLLECTED_EGGS[15]), True, (255, 255, 255))
            endPoints = font.render('Points: ' + str(POINTS), True, (0, 0, 255))
            endPoints2 = font.render('Points: ' + str(POINTS1), True, (255, 0, 0))
            restart = font.render('Press R to restart', True, (255, 255, 255))
            screen.blit(endPoints, (250, 550))
            screen.blit(endPoints2, (650, 550))
            screen.blit(EggDisplay, (150, 125))
            screen.blit(CollectedEggDisplay, (32, 200))
            screen.blit(gameOver, (300, 400))
            screen.blit(restart, (360, 650))
        else:
            screen.blit(text, textRect)
            screen.blit(text2, text2Rect)

    player2.draw(player2.x + player2.xSpeed, player2.y + player2.ySpeed)
    if current_obstacles == max_obstacles and current_obstacles2 == max_obstacles and gameActive:
        if displayedEggs == 0:
            Eggs.clear()
            prevNums.clear()

            while (len(Eggs) < MAX_EGGS):
                generate = True

                while generate:

                    num = random.randint(0, 15)
                    prevNums.append(num)
                    if num == 15:
                        num = 'F'
                    elif num == 14:
                        num = 'E'
                    elif num == 13:
                        num = 'D'
                    elif num == 12:
                        num = 'C'
                    elif num == 11:
                        num = 'B'
                    elif num == 10:
                        num = 'A'
                    else:
                        num = str(num)

                    endPoints = font.render(num, True, (255, 255, 255))

                    randomX = random.randint(0, width - 100)
                    randomY = random.randint(0, height - 100)
                    EggSquare = Square(randomX, randomY, 100)
                    ok = True
                    for item in obstacles:
                        itemSquare = Square(item.x, item.y, 40)
                        if EggSquare.isIntersecting(itemSquare):
                            ok = False

                    even = 0
                    odd = 0
                    for number in prevNums:
                        if number % 2 == 0:
                            even += 1
                        else:
                            odd += 1
                    if (even == 0 or odd == 0) and len(prevNums) > 1 and (even + odd == len(prevNums)):
                        ok = False

                    if ok and EggSquare.isIntersecting(player1Square) is False and EggSquare.isIntersecting(
                            player2Square) is False:
                        generate = False
                        Eggs.append(Egg(randomX, randomY, num))
                    elif len(prevNums) > 0 and ok is False:
                        prevNums.pop()

            displayedEggs = MAX_EGGS

        for item in Eggs:
            itemSquare = Square(item.x, item.y, 100)

            if item.Visible:
                item.draw()

                num = 0

                if item.num == 'F':
                    num = 15
                elif item.num == 'E':
                    num = 14
                elif item.num == 'D':
                    num = 13
                elif item.num == 'C':
                    num = 12
                elif item.num == 'B':
                    num = 11
                elif item.num == 'A':
                    num = 10
                else:
                    num = int(item.num)

                if player2Square.isIntersecting(itemSquare) and num % 2 == 0:
                    item.Visible = False
                    displayedEggs -= 1
                    POINTS += 10
                    speed += 0.05
                    COLLECTED_EGGS[num] += 1

                if player1Square.isIntersecting(itemSquare) and num % 2 != 0:
                    item.Visible = False
                    displayedEggs -= 1
                    POINTS1 += 10
                    speed += 0.05
                    COLLECTED_EGGS[num] += 1

    player2.x += player2.xSpeed
    player2.y += player2.ySpeed
    if player2.x < -100:
        player2.x = width + 100
    if player2.x > width + 100:
        player2.x = -100
    if player2.y < -100:
        player2.y = height + 100
    if player2.y > height + 100:
        player2.y = -100

    pygame.display.update()

pygame.quit()
