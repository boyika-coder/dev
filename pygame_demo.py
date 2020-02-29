# -*- coding: utf-8 -*-

import pygame
import sys

size = (800,600)
white = (255,255,255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("pygame demo")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(white)
    pygame.display.update()
