import pygame
import os


class Player(pygame.sprite.Sprite):
    WIDTH = 360
    HEIGHT = 480

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    game_folder = os.path.dirname(__file__)
    image_folder = os.path.join(game_folder, 'img')
    player_img = pygame.image.load(os.path.join(image_folder, 'Player/p1_jump.png'))

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.player_img
        self.rect = self.image.get_rect()
        self.rect.center = (self.WIDTH / 2, self.HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > self.WIDTH:
            self.rect.right = 0
