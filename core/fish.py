# -*- coding: utf-8 -*-
import pygame

# Fish
class Fish():
    def __init__(self, screen, x, y):
        self.image = pygame.image.load("./images/fish.png")
        self.x, self.y = x, y
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, [self.x, self.y])
