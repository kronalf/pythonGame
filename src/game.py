import pygame
from src.sprites_game import Player, Mob

WIDTH = 480
HEIGHT = 600
FPS = 60

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
mods = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mods.add(m)

# Цикл игры
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(all_sprites, bullets)
    # Обновление
    all_sprites.update()

    #Проверка попадания пули
    hits = pygame.sprite.groupcollide(mods, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mods.add(m)

    #Проверка столкновения
    hits = pygame.sprite.spritecollide(player, mods, False)
    if hits:
        running = False

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
pygame.quit()
