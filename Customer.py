#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pygame
from Util import Util
from Image import Image
import random
import math


class Customer:
    NEED = False
    food = None
    saved_food = None
    seat_key = None
    order = 0  # 保持同一姿势换个方向，全局变量
    MOVE = True
    LEAVED = False
    util = Util()

    def __init__(self,imgType, direction, imgWidth, imgHeight, centerX, centerY):
        self.x = centerX
        self.y = centerY
        self.position = [self.x, self.y]
        # self.screen = screen
        # self.bg = bg
        self.type = imgType
        self.d = direction
        self.w = imgWidth
        self.h = imgHeight


    def move(self, direction, speed, to):
        # print("move")
        self.d = direction
        if direction == 0:
            # 不知道为什么在主程序只调用了一次，却能调用类方法多次
            # 更新绘制，用screen，最后保留状态，用subwindow或bg
            if self.x < to[0]:
                self.x = self.x + speed[0]
                self.change_img()
                pygame.time.delay(10)

        elif direction == 1:
            if self.x > to[0]:
                self.x = self.x - speed[0]
                self.change_img()
                pygame.time.delay(10)
        elif direction == 2:
            if self.y < to[1]:
                self.y = self.y + speed[1]
                self.change_img()
                pygame.time.delay(10)
        else:
            if self.y > to[1]:
                self.y = self.y - speed[1]
                self.change_img()
                pygame.time.delay(10)

    def change_img(self):
        end = len(Image.CUSTOMER.get(self.type).get(self.d))
        if self.order == end - 1:
            self.order = 0
        else:
            self.order = self.order + 1

    # def draw_img(self):
    #     # print(self.x, self.y)
    #     self.screen.blit(self.bg, (0, 0))
    #     self.rect = self.util.blit_image(self.screen, Image.CUSTOMER.get(self.type).get(self.d)[self.order], self.w,
    #                                      self.h,
    #                                      self.x, self.y)
    #     # pygame.display.update()

    # def path_to_transfer(self, queue_len, i):
    #     # print(33)
    #     if queue_len == 0:
    #         self.move(0, [i + 5, i + 5], (150, 325 + i * 10))
    #         # self.move(2, [i+5, i+5], (150, 325 + i * 10))
    #     else:
    #         self.move(0, [i + 5, i + 5], (150 - queue_len * 30, 325 + i * 10))
    #         # self.move(2, [i + 5, i + 5], (150 - queue_len * 30, 325 + i * 10))

    # def path(self,speed,to):
    #     #当刚好y坐标相等
    #     if self.y==to[1]:
    #         if to[0]>=self.x:
    #             self.move(0,speed,to)
    #         else:
    #             self.move(1,speed,to)
    #     #当刚好x坐标相等
    #     elif self.x==to[0]:
    #         if to[1]>=self.y:
    #             self.move(2,speed,to)
    #         else:
    #             self.move(3,speed,to)
    #     #当x，y坐标都不相等
    #     elif self.x!=to[0] and self.y!=to[1]:

    # 方向0：东 1：西 2：南 3：北
    # def move(self, direction, speed, to):
    #     if direction == 0 or direction == 1:
    #         order = 0
    #         time = pygame.time.get_ticks()
    #         while self.x != to[0]:
    #             order = order + 1
    #             self.rect = Util.blit_image(self.surface, Image.CUSTOMER.get(type).get(self.d)[order], self.w, self.h, self.x, self.y)
    #             current = pygame.time.get_ticks()
    #             if current - time == speed:
    #                 self.x = self.x + 5
    #                 time = current
    # 仅一条直线上的运动

    def ask_for_food(self):
        food_size = len(Image.FOOD)
        food_order = random.randint(1, food_size)
        if self.food is not None:
            pass
        else:
            self.food = food_order

    # def cancel_order(self):
    #     self.util.cancel_image(self.surface, self.bubble_rect.x, self.bubble_rect.y, self.bubble_rect.width,
    #                            self.bubble_rect.height)
    #     self.util.cancel_image(self.surface, self.food_rect.x, self.food_rect.y, self.food_rect.width,
    #                            self.food_rect.height)
    #     self.bubble_rect = None
    #     self.food_rect = None
    #     pygame.display.update()
    def find_seat(self,i,screen):
        if i == 0:
            self.seat_pos = (self.x - 15, self.y - 25)
            self.util.blit_image(screen,
                                 Image.CUSTOMER.get(self.type).get(0)[
                                     3], 30,
                                 50, self.x - 15, self.y - 25)
        elif i == 1:
            self.seat_pos = (self.x - 15, self.y - 25)
            self.util.blit_image(screen,
                                 Image.CUSTOMER.get(self.type).get(3)[
                                     3], 30,
                                 50, self.x - 15, self.y - 25)
        elif i == 2:
            self.seat_pos = (self.x - 15, self.y - 25)
            self.util.blit_image(screen,
                                 Image.CUSTOMER.get(self.type).get(1)[
                                     3], 30,
                                 50, self.x - 15, self.y - 25)
        elif i == 3:
            self.seat_pos = (self.x - 15, self.y - 25)
            self.util.blit_image(screen,
                                 Image.CUSTOMER.get(self.type).get(3)[
                                     3], 30,
                                 50, self.x - 15, self.y - 25)
    def check_seat(self):
        for key, val in self.table.seat.items():
            if self.table.seat.get(key).get("status") == False:
                self.seat_key = key
                return self.table.seat.get(key).get("pos")

    def find_path(self, speed, table):
        self.table = table
        table_name = table.NAME
        if table_name == "1号桌":
            self.move(0, speed, [375, self.y])
            self.move(3, speed, [self.x, 400])
            self.seat_pos = self.check_seat()
            self.move(3, speed, self.seat_pos)
            # self.draw_img()
        elif table_name == "2号桌":
            self.move(0, speed, [375, self.y])
            self.move(2, speed, [self.x, 325])
            self.seat_pos = self.check_seat()
            self.move(2, speed, self.seat_pos)
            self.MOVE = False
            # self.draw_img()
        elif table_name == "3号桌":
            self.move(0, speed, [425, self.y])
            self.seat_pos = self.check_seat()
            self.move(0, speed, self.seat_pos)
            self.MOVE = False
            # self.draw_img()
        elif table_name == "4号桌":
            self.move(0, speed, [375, self.y])
            self.move(3, speed, [self.x, 400])
            self.move(0, speed, [600, self.y])
            self.seat_pos = self.check_seat()
            self.move(3, speed, self.seat_pos)
            self.MOVE = False
            # self.draw_img()
        elif table_name == "5号桌":
            self.move(0, speed, [375, self.y])
            self.move(2, speed, [self.x, 325])
            self.move(0, speed, [600, self.y])
            self.seat_pos = self.check_seat()
            self.move(2, speed, self.seat_pos)
            self.MOVE = False
            # self.draw_img()

    # def change_img(self, type):
    #         end = len(Image.CUSTOMER.get(type).get(0))
    #         order = 0
    #         if order == end - 1:
    #             order = 0
    #         else:
    #             order = order + 1
    #         return order
    #
    # def draw_img(self, direction, order, type, w, h, x, y):
    #         # print(self.x,self.y)
    #
    #         self.rect = self.util.blit_image(self.screen, Image.CUSTOMER.get(type).get(direction)[order], w,
    #                                          h,
    #                                          x, y)
    #
    # def move(self, direction, speed, to, customer):
    #         # print("move")
    #         self.d = direction
    #         if direction == 0:
    #             # 不知道为什么在主程序只调用了一次，却能调用类方法多次
    #             # 更新绘制，用screen，最后保留状态，用subwindow或bg
    #             if customer.x != to[0]:
    #                 self.screen.blit(self.subWindow, (0, 0))
    #                 # self.screen.fill((255,255,255))
    #                 # pygame.display.update()
    #                 customer.x = customer.x + speed[0]
    #                 order = self.change_img(customer.type)
    #                 self.draw_img(direction, order, customer.type, customer.w, customer.h, customer.x, customer.y)
    #                 pygame.time.delay(100)
    #             else:
    #                 self.util.blit_image(self.subWindow, Image.CUSTOMER.get(customer.type).get(0)[0], 50, 100,
    #                                      destX=customer.x,
    #                                      destY=customer.y)
    #         elif direction == 1:
    #             if self.x != to[0]:
    #                 self.screen.blit(self.subWindow, (0, 0))
    #                 # self.screen.fill((255,255,255))
    #                 # pygame.display.update()
    #                 self.x = self.x - speed[0]
    #                 self.change_img()
    #                 self.draw_img()
    #                 pygame.time.delay(100)
    #             if self.x == to[0] and self.y == to[1]:
    #                 self.util.blit_image(self.subWindow, Image.CUSTOMER.get(customer.type).get(1)[0], 50, 100,
    #                                      destX=self.x,
    #                                      destY=self.y)
    #
    #         elif direction == 2:
    #             if self.y != to[1]:
    #                 self.screen.blit(self.subWindow, (0, 0))
    #                 # self.screen.fill((255,255,255))
    #                 # pygame.display.update()
    #                 self.y = self.y + speed[1]
    #                 self.change_img()
    #                 self.draw_img()
    #                 pygame.time.delay(100)
    #             if self.x == to[0] and self.y == to[1]:
    #                 self.util.blit_image(self.subWindow, Image.CUSTOMER.get(customer.type).get(2)[0], 50, 100,
    #                                      destX=self.x,
    #                                      destY=self.y)
    #         else:
    #             if self.y != to[1]:
    #                 self.screen.blit(self.subWindow, (0, 0))
    #                 # self.screen.fill((255,255,255))
    #                 # pygame.display.update()
    #                 self.y = self.y - speed[1]
    #                 self.change_img()
    #                 self.draw_img()
    #                 pygame.time.delay(100)
    #             if self.x == to[0] and self.y == to[1]:
    #                 self.util.blit_image(self.subWindow, Image.CUSTOMER.get(customer.type).get(3)[0], 50, 100,
    #                                      destX=self.x,
    #                                      destY=self.y)
