import pygame
import random

pygame.init()

#Настройки окна
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dino by Parad1st") #Название

#Штука снизу
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

#Настройки игры
ground_height = 650 
dino_width = 80
dino_height = 80
dino_x = 50
dino_y = ground_height - dino_height
jump_height = 23
gravity = 1
game_speed = 10

#Кактус
cactus_image = pygame.image.load('cactus.jpg')
cactus_width = 160
cactus_height = 160
cactus_image = pygame.transform.scale(cactus_image, (cactus_width, cactus_height))
cactus_x = screen_width
cactus_y = ground_height - cactus_height

#Дино
dino_image = pygame.image.load('dino.png')
dino_image = pygame.transform.scale(dino_image, (dino_width, dino_height))

dino_y_change = 0
is_jumping = False
score = 1

running = True
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

#Счет
def display_score(score):
    text = font.render(f"Score: {score}", True, black)
    screen.blit(text, [10, 10])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN):
            if not is_jumping:
                is_jumping = True
                dino_y_change = -jump_height

    if is_jumping:
        dino_y += dino_y_change
        dino_y_change += gravity
        if dino_y >= ground_height - dino_height:
            dino_y = ground_height - dino_height
            is_jumping = False
            dino_y_change = 0

    cactus_x -= game_speed
    if cactus_x < -cactus_width:
        cactus_x = screen_width
        score += 1

    if dino_x + dino_width > cactus_x and dino_x < cactus_x + cactus_width:
        if dino_y + dino_height > cactus_y:
            running = False

    screen.fill(white)
    pygame.draw.rect(screen, gray, [0, ground_height, screen_width, screen_height - ground_height])
    screen.blit(dino_image, (dino_x, dino_y))
    screen.blit(cactus_image, (cactus_x, cactus_y))
    display_score(score)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
