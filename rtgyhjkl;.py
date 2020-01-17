from os import path
import sys
import pygame
from main import main_game


def load_image(name):
    fullname = path.join('textures', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


pygame.init()
player = None
size = width, height = 1200, 600
screen = pygame.display.set_mode(size)

fps = 30
clock = pygame.time.Clock()


def start_screen():
    font = pygame.font.Font(None, 30)
    text_coord = 50
    intro_text = ['Приветствуем Вас в нашей игре.',
                  "Играя за доброго синего слизня",
                  "в ней Вам предстоит добежать",
                  "до портала, избегая",
                  "препятствия в виде лиловых кустов",
                  "и летающих противников.",
                  "Пополняйте здоровье при помощи",
                  "Голубых цветков",
                  "W - прыжок; A/D - назад/вперёд",
                  'Нажмите Enter для начала игры.',
                  "Желаем удачи!"]
    screen.fill((152, 217, 234))
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('mediumblue'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 800
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    fon_image = load_image('player.png')
    fon_image = pygame.transform.scale(fon_image, (800, 800))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_game()
                    return
        text_cord = [0, 0]
        rect = fon_image.get_rect()
        rect.x = text_cord[0]
        rect.y = text_cord[1]
        screen.blit(fon_image, rect)
        clock.tick(fps)
        pygame.display.flip()


def end_screen():
    font = pygame.font.Font(None, 30)
    text_coord = 50
    intro_text = ["Мы снова встретились!",
                  'Вы проиграли или победили,',
                  "вспомните сами!",
                  "Счёт:",
                  "Рекорд при победе:",
                  'Для начала новой игры нажмите Enter.',
                  "Желаем удачи и новых рекордов!"]
    screen.fill((152, 217, 234))
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('mediumblue'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 800
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    fon_image = load_image('player.png')
    fon_image = pygame.transform.scale(fon_image, (800, 800))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_screen()
                    return
        text_cord = [0, 0]
        rect = fon_image.get_rect()
        rect.x = text_cord[0]
        rect.y = text_cord[1]
        screen.blit(fon_image, rect)
        clock.tick(fps)
        pygame.display.flip()


def terminate():
    pygame.quit()
    sys.exit()


    # your code


start_screen()
end_screen()
main_game()
terminate()
