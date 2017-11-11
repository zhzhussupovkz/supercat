# -*- coding: utf-8 -*-
import pygame
import sys
from core.cat import *

class World():
    SIZE = (800, 600)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Super Cat')
        self.pygame = pygame
        self.screen = pygame.display.set_mode(self.SIZE)
        self.background_image = pygame.image.load("./images/background.png").convert()
        self.cat = Cat(self.screen, 48, 500)

    def draw(self):
        self.cat.draw()

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                sys.exit()
            self.screen.blit(self.background_image, [0, 0])
            self.draw()
            self.cat.walk()
            pygame.display.flip()
        pygame.quit()