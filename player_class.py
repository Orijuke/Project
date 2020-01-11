import pygame
import random

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

    #hit_sound = load_sound('hit.ogg')
    #monster_death_sound = load_sound('monster_death.wav')

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

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                #Enemy.hit_sound.play()
                self.get_click(event.pos)

    def get_click(self, pos):
        if self.rect.collidepoint(pos):
            self.health -= 50
            player.score *= 1.02
            print(self.health)
            if self.health <= 0:
                #Enemy.monster_death_sound.play()
                player.score *= 1.80
                self.kill()

player = Player(width // cell_size // 2, 0)
body_sprites = pygame.sprite.Group()
body_sprites.add(player)
enemy_sprites = pygame.sprite.Group()
for n in range(20):
    enemy = Enemy(random.randrange(width // cell_size, level_length - width // cell_size), 0)
    enemy_sprites.add(enemy)
