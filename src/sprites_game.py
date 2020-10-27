import pygame
import os


class Player(pygame.sprite.Sprite):
    WIDTH = 480
    HEIGHT = 600

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    speedx = 0

    game_folder = os.path.dirname(__file__)
    image_folder = os.path.join(game_folder, 'img')
    player_img = pygame.image.load(os.path.join(image_folder, 'Player/p1_jump.png'))

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(self.GREEN)
        # self.image = self.player_img
        self.rect = self.image.get_rect()
        # self.rect.center = (self.WIDTH / 2, self.HEIGHT / 2)
        self.rect.centerx = self.WIDTH / 2
        self.rect.bottom = self.HEIGHT - 10
        #self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -4
        if keystate[pygame.K_RIGHT]:
            self.speedx = 4
        self.rect.x += self.speedx
        if self.rect.right > self.WIDTH:
            self.rect.right = self.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
