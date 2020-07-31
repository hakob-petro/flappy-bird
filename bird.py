#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import pyganim
from pygame import *

SPEED = 0
JUMP = 10
GRAVITY = 1
COLOR = (0, 0, 0)
ANIMATION_DELAY = 1
ANIMATION = ["bird/skeleton-animation_00.png",
             "bird/skeleton-animation_01.png",
             "bird/skeleton-animation_02.png",
             "bird/skeleton-animation_03.png",
             "bird/skeleton-animation_04.png",
             "bird/skeleton-animation_05.png",
             "bird/skeleton-animation_06.png",
             "bird/skeleton-animation_07.png",
             "bird/skeleton-animation_08.png",
             "bird/skeleton-animation_09.png",
             "bird/skeleton-animation_10.png"]

class Bird(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = xpos
        self.y = ypos
        self.yvel = 0
        self.up = False
        self.wasup = False
        self.end = False
        self.score = 0
        self.image = Surface((53, 30))
        #self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        
        self.image.set_colorkey(COLOR)
        animations = []
        for anim in  ANIMATION:
            animations.append((anim, ANIMATION_DELAY))
        self.anim = pyganim.PygAnimation(animations)
        self.anim.play()
        

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        timer = pygame.time.Clock()
        self.image.fill(COLOR)
        self.anim.blit(self.image, (0, 0))
        
        if self.up:
            self.yvel = -JUMP
            self.up = False
            self.wasup = True
        elif not self.wasup:
            self.yvel += GRAVITY
        else:
            self.wasup = False
        #pygame.time.delay(30)
        self.y += self.yvel
        self.rect.y = self.y
        self.x += SPEED
        self.rect.x = self.x
        if (self.y < 0):
            self.y = 0
        if self.y >= 400:
            self.end = True
