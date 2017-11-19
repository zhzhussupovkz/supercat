# -*- coding: utf-8 -*-
import pygame

# Cat class
class Cat():
    def __init__(self, screen, x, y):
        self.image = pygame.image.load("./images/cat_right.png")
        self.heart = pygame.image.load('./images/heart.png')
        self.x, self.y = x, y
        self.screen = screen
        self.lives = 3

    def draw(self):
        self.screen.blit(self.image, [self.x, self.y])
        for i in range(0, self.lives):
            self.screen.blit(self.heart, [16+i*36, 16])

    def move_left(self):
        self.image = pygame.image.load("./images/cat.png")
        self.x -= 0.4
        if self.x <= 32:
            self.x = 32

    def move_right(self):
        self.image = pygame.image.load("./images/cat_right.png")
        self.x += 0.4
        if self.x >= 732:
            self.x = 732

    def move_down(self):
        if self.y <= 500:
            self.y += 1

    def jump(self):
        if self.y >= 240:
            self.y -= 2

    def walk(self):
        self.move_down()
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.move_right()
        elif key[pygame.K_LEFT]:
            self.move_left()
        if key[pygame.K_SPACE]:
            self.jump()
