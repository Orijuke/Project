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

class Spike(pygame.sprite.Sprite):

    spike_image = load_image("spike.png")

    def __init__(self, x, y):
        super().__init__()
        self.image = Spike.spike_image
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size

    def set_pos(self, x, y):
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size

class Kit(pygame.sprite.Sprite):

    kit_image = load_image("kit.png")

    def __init__(self, x, y):
        super().__init__()
        self.image = Kit.kit_image
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size

    def set_pos(self, x, y):
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size

class Portal(pygame.sprite.Sprite):

    top_image = load_image("portal_top.png")
    down_image = load_image("portal_down.png")

    def __init__(self, x, y, top):
        super().__init__()
        if top:
            self.image = Portal.top_image
        else:
            self.image = Portal.down_image
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size

    def set_pos(self, x, y):
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size