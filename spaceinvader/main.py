import pygame
import random
import math
from pygame import mixer

# init the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("C:\\Users\\tussh\\PycharmProjects\\spaceinvader\\spaceback.jpg")

# background sound
mixer.music.load("C:\\Users\\tussh\\PycharmProjects\\spaceinvader\\background.wav")
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("C:\\Users\\tussh\\PycharmProjects\\spaceinvader\\ufo.png")
pygame.display.set_icon(icon)

# payer
playerImg = pygame.image.load("C:\\Users\\tussh\\PycharmProjects\\spaceinvader\\player.png")
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemy = 5

for i in range(number_of_enemy):
    enemyImg.append(pygame.image.load("C:\\Users\\tussh\\PycharmProjects\\spaceinvader\\enimy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1.5)
    enemyY_change.append(40)


def enemy(x, y,i):
    screen.blit(enemyImg[i], (x, y))


# bullet

# ready - you cant see the bullet on the screen
# fier - the bullet is currently moving

bulletImg = pygame.image.load("C:\\Users\\tussh\\PycharmProjects\\spaceinvader\\ammo.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2)
                         + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

#score
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)

textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))

#Game over text
over_font = pygame.font.Font("freesansbold.ttf",64)

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text,(200,250))


# game loop
running = True
while running:
    # red green blue
    screen.fill((156, 156, 10))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check wheather its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound("C:\\Users\\tussh\\PycharmProjects\\spaceinvader\\laser.wav")
                    bullet_Sound.play()
                    # get the current x coordinate of the bullet
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # change in player position
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736



    #emey movement
    for i in range(number_of_enemy):

        #Game over
        if enemyY[i] > 420:
            for j in range(number_of_enemy):
                enemyY[j] = 2000
            game_over_text()
            break;

        # change in enemy position
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1.5
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound("C:\\Users\\tussh\\PycharmProjects\\spaceinvader\\explosion.wav")
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    # show_score(textX,textY)
    pygame.display.update()
