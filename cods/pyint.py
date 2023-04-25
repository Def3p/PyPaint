import pygame        # pygame
from pygame import * # все модули из pygame
from base import whiler # соседний файл

WIDTH, HEIGHT = 650, 650 # разрешение

init() # инициализация
screen = pygame.display.set_mode((WIDTH, HEIGHT), NOFRAME) # дисплей

whiler(screen) # игровой цикл