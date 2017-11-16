# -*- coding: utf-8 -*-
import pygame
import sys
import random
from core.cat import *
from core.fish import *
from core.brick import *

class World():
    SIZE = (800, 600)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Super Cat')
        self.pygame = pygame
        self.screen = pygame.display.set_mode(self.SIZE)
        self.background_image = pygame.image.load("./images/background.png").convert()
        self.cat = Cat(self.screen, 48, 500)
        self.bricks = []
        self.fishes = []
        self.gen_bricks()

    def draw(self):
        for brick in self.bricks:
            brick.draw()
        for fish in self.fishes:
            fish.draw()
        self.cat.draw()

    def gen_bricks(self):
        i = 128
        while i <= 720:
            coord = random.randint(256, 460)
            self.bricks.append(Brick(self.screen, i, coord))
            self.fishes.append(Fish(self.screen, i+16, coord-48))
            i += 128

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