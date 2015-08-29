import config
import pygame
import model
import render
from generator import Generator
import time
import logging
from player import Player
from computer import Computer
import menu

if __name__ == "__main__":

    logging.basicConfig(filename='rats.log', level=logging.INFO)

    if config.enable_menu:
        menu.show_menu()

    pygame.init()
    player = Player()
    generator = Generator(player)
    game = model.Model(generator)
    view = render.View(game.map.size)

    running = True
    while running:
        game.step()
        view.render(game)
        time.sleep(config.speed_value[config.speed])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                player.process_click(pos)