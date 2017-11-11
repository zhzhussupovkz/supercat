# -*- coding: utf-8 -*-
import pygame

# Cat class
class Cat():
    def __init__(self, screen, x, y):
        self.image = pygame.image.load("./images/cat.png")
        self.x, self.y = x, y
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, [self.x, self.y])

    def move_left(self):
        self.x -= 0.4
        if self.x <= 32:
            self.x = 32

    def move_right(self):
        self.x += 0.4
        if self.x >= 732:
            self.x = 732

    def walk(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.move_right()
        elif key[pygame.K_LEFT]:
            self.move_left()