from os import path
import pygame
from load_image_function import load_image, cell_size

class Block(pygame.sprite.Sprite):

    grass_image = load_image("grass.png")
    dirt_image = load_image("dirt.png")

    def __init__(self, x, y, grassed):
        super().__init__()
        if grassed:
            self.image = Block.grass_image
        else:
            self.image = Block.dirt_image
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size

    def set_pos(self, x, y):
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
