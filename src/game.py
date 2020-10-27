import pygame
import random
from src.sprites_game import Player

WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# game_folder = os.path.dirname(__file__)
# image_folder = os.path.join(game_folder, 'img')
# player_img = pygame.image.load(os.path.join(image_folder, 'p1_jump.png'))
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Цикл игры
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLUE)
    all_sprites.draw(screen)

    pygame.display.flip()
pygame.quit()
