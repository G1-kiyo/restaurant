#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Util import Util
import pygame
class Score:
    score = 0
    util = Util()
    def __init__(self, surface, path, imgWidth, imgHeight, destX, destY):
        # self.rect = Util.blit_image(surface, path, imgWidth, imgHeight, destX, destY)
        self.surface = surface
        self.path = path
        self.w = imgWidth
        self.h = imgHeight
        self.destX = destX
        self.destY = destY
        # 积分框rect
        self.score_rect = self.util.blit_image(surface, path, imgWidth, imgHeight, destX, destY)
        self.util.draw_text(self.surface,"./font/score.ttf",22,"￥"+str(self.score),"#7FFF00","#FF7F50",self.destX,self.destY,imgWidth,imgHeight)



    def update(self,score):
        self.score = self.score+score
        self.util.draw_text(self.surface, "./font/score.ttf", 22, "￥" + str(self.score), "#7FFF00", "#FF7F50", self.destX,
                       self.destY,self.w,self.h)




