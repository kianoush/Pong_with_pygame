
import pygame


class Padd:
    def __init__(self, height, width, speed):
        self.height = height
        self.width = width
        self.speed = speed
        self.padd_a = pygame.image.load("img/01.jpeg")
        self.padd_a = pygame.transform.scale(self.padd_a, (self.height, self.width))
        self.padd_b = pygame.image.load("img/02.jpeg")
        self.padd_b = pygame.transform.scale(self.padd_b, (self.height, self.width))


    def show_padd_a(self):
        self.padd_a = self.padd_a

        return self.padd_a

    def show_padd_b(self):
        self.padd_b = self.padd_b

        return self.padd_b