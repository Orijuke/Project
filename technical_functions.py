from camera import camera
from level_generator import block_sprites, portal_sprites, kit_sprites, spike_sprites
from player_class import enemy_sprites, body_sprites


def camera_apply():
    for sprite in block_sprites:
        camera.apply(sprite)
    for sprite in spike_sprites:
        camera.apply(sprite)
    for sprite in kit_sprites:
        camera.apply(sprite)
    for sprite in portal_sprites:
        camera.apply(sprite)
    for sprite in enemy_sprites:
        camera.apply(sprite)


def sprites_update(event):
    block_sprites.update(event)
    spike_sprites.update(event)
    kit_sprites.update(event)
    portal_sprites.update(event)
    body_sprites.update(event)
    enemy_sprites.update(event)


def sprites_draw(screen):
    block_sprites.draw(screen)
    spike_sprites.draw(screen)
    kit_sprites.draw(screen)
    portal_sprites.draw(screen)
    body_sprites.draw(screen)
    enemy_sprites.draw(screen)