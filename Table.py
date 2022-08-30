#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Util import Util
import pygame
class Table:
    NAME = ""
    INDEX = None
    USED = False
    ISUSING = False
    util = Util()
    pos = ()
    def __init__(self,surface,path,imgWidth,imgHeight,destX,destY):
        self.rect = self.util.blit_image(surface,path,imgWidth,imgHeight,destX,destY)
        # pygame.draw.rect(surface,(255,255,0),(self.rect.x,self.rect.y,self.rect.w,self.rect.h))
        # pygame.draw.rect(surface,(0,0,0),(self.rect.x-1,self.rect.y-1,self.rect.w-2,self.rect.h-2))
        self.seat = {1: {"pos": [self.rect.centerx-20,self.rect.centery-20],"status":False},
                     2: {"pos": [self.rect.centerx-20,self.rect.centery+20],"status":False},
                     3: {"pos": [self.rect.centerx+20,self.rect.centery-20],"status":False},
                     4: {"pos": [self.rect.centerx+20,self.rect.centery+20],"status":False}}
        # self.dest = {"1号桌":[375,300],
        #              "2号桌":[375,350],
        #              "3号桌":[425,325],
        #              "4号桌":[600,300],
        #              "5号桌":[600,350]}


