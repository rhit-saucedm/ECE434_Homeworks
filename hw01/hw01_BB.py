#!/usr/bin/env python3

import pygame
import sys

from pygame.locals import *

pygame.init()

#Screen Sizing
screenLength = 600 #cast into integer
screenWidth = 600
screen = pygame.display.set_mode((screenLength,screenWidth))

x = screenLength/2
y = screenWidth/2

clock = pygame.time.Clock()
screen.fill((255,255,255))


# additionalSettings = input('Do you want additional pen settings? (Y/N): ').upper()
# if additionalSettings == 'Y':
#     penSize = int(input('What size pen? (2 is normal): '))
#     penColor = input('What color pen?: ').upper()

while 1:
    clock.tick(60)
    # if additionalSettings == 'Y': pygame.draw.circle(screen,pygame.Color(penColor),(x,y),penSize)
    # elif additionalSettings == 'N': pygame.draw.circle(screen,(0,0,0),(x,y),2)
    pygame.draw.circle(screen,(0,0,0),(x,y),2)
    pygame.display.update()
    
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]: 
        x += 1
    if key[pygame.K_LEFT]: 
        x -= 1
    if key[pygame.K_UP]: 
        y -= 1
    if key[pygame.K_DOWN]: 
        y += 1
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            screen.fill((255,255,255))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
