
"""
define the ball and move it
"""

import pygame



class Ball:
    def __init__(self, size, height, width):
        self.size = size
        self.move = [3, 3]
        self.height = height
        self.width = width
        self.x = 40
        self.y = 40
        self.img = pygame.image.load("img/Ball_2.jpg")
        self.img = pygame.transform.scale(self.img, (self.size))
        self.pos = [20, 20]

    def show_ball(self):
        self.img = self.img
        return self.img















