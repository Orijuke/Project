import math

import pygame
import random

from camera import camera
from level_generator import level_height, level_length
from load_image_function import load_image, cell_size, width, height, load_sound

pygame.mixer.init()


class Player(pygame.sprite.Sprite):
    player_image = load_image("player.png")

    def __init__(self, x, y):
        super().__init__()
        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
        self.health = 2000
        self.score = 1
        self.x = x
        self.y = y


class Enemy(pygame.sprite.Sprite):
    hit_sound = load_sound('hit.ogg')
    monster_death_sound = load_sound('m_death.ogg')

    enemy_image = load_image("enemy.png")

    def __init__(self, x, y):
        super().__init__()
        self.image = Enemy.enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
        self.health = 2000
        self.x = x
        self.y = y
        self.cr = True

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                Enemy.hit_sound.play()
                self.get_click(event.pos)

    def get_click(self, pos):
        if self.rect.collidepoint(pos):
            self.health -= 400
            player.score += 0.2
            if self.health <= 0:
                Enemy.monster_death_sound.play()
                player.score += 1.80
                self.kill()

    def make_step(self):
        dx = (self.rect.x - player.rect.x) / cell_size
        dy = (self.rect.y - player.rect.y) / cell_size
        c = math.sqrt(dx ** 2 + dy ** 2)
        player_dx = player.x - width / cell_size / 2
        if c < width / cell_size / 2 and c != 0:
            #print('B', self.x, self.rect.x / cell_size)
            ky = dy / c
            kx = dx / c
            self.rect.x -= 2 * kx
            self.rect.y -= 2 * ky
            print(player.x, player.rect.x)
            self.x = self.rect.x / cell_size + player_dx
            self.y = self.rect.y / cell_size
            #print('A', self.x, self.rect.x / cell_size)



player = Player(width // cell_size // 2, 0)
body_sprites = pygame.sprite.Group()
body_sprites.add(player)
enemy_sprites = pygame.sprite.Group()
for n in range(20):
    enemy = Enemy(random.randrange(width // cell_size, level_length - width // cell_size), random.randrange(0, 5))
    enemy_sprites.add(enemy)
