#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from Util import Util
from Image import Image
import pygame
import random


class Kitchen:
    all_food_rect = []
    prepare_list = []
    util = Util()
    def __init__(self, surface, path, imgWidth, imgHeight, destX, destY):
        self.surface = surface
        self.destX = destX
        self.destY = destY
        # self.rect = self.surface.blit(pygame.transform.rotate(pygame.image.load(path),90),(destX,destY))
        self.rect = self.util.blit_image(surface, path, imgWidth, imgHeight, destX, destY)

    def record_food(self, food_list):
        for food in food_list:
            self.prepare_list.append(food)

    def provide_food(self):
        pygame.time.delay(random.randrange(2000, 5000))
        for i in range(6):
            food_rect = self.util.blit_image(self.surface, Image.FOOD.get(self.prepare_list[i]), destX=self.destX,
                                        destY=self.destY + i * 50)
            self.all_food_rect[food_rect] = self.prepare_list[i]
            pygame.time.delay(random.randrange(500, 2000))
            if i + 1 > len(self.prepare_list):
                break

    def cancel_kitchen_food(self, food_rect):
        self.util.cancel_image(self.surface, food_rect.x, food_rect.y, food_rect.width, food_rect.height)
