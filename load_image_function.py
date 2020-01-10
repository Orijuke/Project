from os import path
import pygame

pygame.mixer.init()

size = width, height = 1200, 600
cell_size = 20
screen = pygame.display.set_mode(size)

def load_image(name):
    fullname = path.join('textures', name)
    image = pygame.image.load(fullname).convert_alpha()
    image = pygame.transform.scale(image, (cell_size, cell_size))
    return image

def load_sound(name):
    fullname = path.join('sounds', name)
    sound = pygame.mixer.Sound(fullname)
    return sound
