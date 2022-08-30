#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Util import Util
import pygame
from Image import Image
import math


class Waiter:
    STATUS = ""
    LEFT_HAND = False
    RIGHT_HAND = False
    X_GO = True
    Y_GO = False
    order = 0  # 保持同一姿势换个方向，全局变量
    MOVE = False
    util = Util()
    kitchen = None
    food = {"left":None,"right":None}
    register = {"table":None,"group":None}
    send = {"table":None,"group":None}
    profit = {"table": None, "group": None}
    def __init__(self,screen,subWindow,direction, imgWidth, imgHeight, centerX, centerY):
        self.x = centerX
        self.y = centerY
        self.position = [self.x, self.y]
        self.screen = screen
        self.subWindow = subWindow
        self.d = direction
        self.w = imgWidth
        self.h = imgHeight
        # self.waiter_surface = pygame.Surface(size=(imgWidth, imgHeight))
        # self.waiter_rect = self.util.blit_image(self.subWindow, Image.WAITER.get(direction)[self.order], imgWidth,
        #                                    imgHeight, centerX-25, centerY-50)
        # self.waiter_surface_rect = self.util.blit_image(self.surface, self.waiter_surface, destX=destX, destY=destY)
        # self.waiter_surface_rect = self.surface.blit(self.waiter_surface,(destX,destY))

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
    def find_path(self,speed,origin,destination):
        destination_list = {"1号桌":[300,250],
                            "2号桌":[300,350],
                            "3号桌":[450,300],
                            "4号桌":[600,250],
                            "5号桌":[600,350]}
        # dest_pos = destination_list.get(destination)
        direction,final_dest = self.find_closest_pos(origin,destination)
        if final_dest[0]==origin[0] and final_dest[1]==origin[1]:
            self.set_final_direction(direction)
            self.draw_img()
            self.MOVE = False
        elif final_dest[0]==origin[0] and final_dest[1]!=origin[1]:
            if final_dest[1]>origin[1]:
                self.move(2,speed,final_dest)
            else:
                self.move(3,speed,final_dest)
        elif final_dest[1]==origin[1] and final_dest[0]!=origin[0]:
            if final_dest[0]>origin[0]:
                self.move(0,speed,final_dest)
            else:
                self.move(1,speed,final_dest)
        else:
            if final_dest[1]<origin[1]:
                self.move(3,speed,final_dest)
            elif final_dest[1]>origin[1]:
                self.move(2,speed,final_dest)

    def set_final_direction(self,direction):
        if direction==0:
            self.d = 1
        elif direction==1:
            self.d = 0
        elif direction==2:
            self.d = 3
        else:
            self.d = 2
    def find_closest_pos(self,origin,dest_pos):
        seat = [(dest_pos[0]+30,dest_pos[1]),(dest_pos[0]-30,dest_pos[1]),(dest_pos[0],dest_pos[1]+30),(dest_pos[0],dest_pos[1]-30)]
        dis = list(map(lambda x:(x[0]-origin[0])**2+(x[1]-origin[1])**2,seat))
        min_val = min(dis)
        direction = dis.index(min_val)
        return (direction,seat[direction])

    # def find_path(self, speed, origin, destination):
    #     destination_list = {1: [150, 450],
    #                         "1号桌": [300, 250],
    #                         "4号桌": [600, 250],
    #                         "2号桌": [300, 350],
    #                         "5号桌": [600, 350],
    #                         "3号桌": [450, 300],
    #                         "stand": [800, 300]}
    #     transfer = [650, 375]
    #     # 假设某个坐标轴是相同的
    #     if origin[0] == destination_list.get(destination)[0] and origin[1] != destination_list.get(destination)[1]:
    #         if origin[1] >= destination_list.get(destination)[1]:
    #             self.move(3, speed, destination_list.get(destination))
    #         else:
    #             self.move(2, speed, destination_list.get(destination))
    #     elif origin[1] == destination_list.get(destination)[1] and origin[0] != destination_list.get(destination)[0]:
    #         if origin[0] >= destination_list.get(destination)[0]:
    #             self.move(1, speed, destination_list.get(destination))
    #         else:
    #             self.move(0, speed, destination_list.get(destination))
    #     elif origin[1] == destination_list.get(destination)[1] and origin[0] == destination_list.get(destination)[0]:
    #         self.draw_img()
    #     else:
    #         if origin[0] >= destination_list.get(destination)[0] and origin[1] != destination_list.get(destination)[1]:
    #             self.move(1, speed, transfer)
    #             self.find_path(speed, [self.x, self.y], destination_list.get(destination))
    #
    #         elif origin[0] <= destination_list.get(destination)[0] and origin[1] != destination_list.get(destination)[
    #             1]:
    #             self.move(0, speed, transfer)
    #             self.move(2, speed, transfer)
    #             self.find_path(speed, [self.x, self.y], destination_list.get(destination))

    def change_img(self):
        end = len(Image.WAITER.get(self.d))
        if self.order == end - 1:
            self.order = 0
        else:
            self.order = self.order + 1


    def draw_img(self):
        #
        self.rect = self.util.blit_image(self.screen, Image.WAITER.get(self.d)[0], self.w, self.h,
                                         0, 0)
        # if self.MOVE == False:
        #
        #     self.waiter_surface_rect = self.util.blit_image(self.surface, self.waiter_surface, destX=self.x, destY=self.y)
        # else:
        #     self.rect = self.util.blit_image(self.waiter_surface, Image.WAITER.get(self.d)[self.order], self.w, self.h,
        #                                 0, 0)
        #     self.waiter_surface_rect = self.util.blit_image(self.surface, self.waiter_surface, destX=self.x, destY=self.y)
        # pygame.display.update()

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

    # def find_path(self,speed,table):
    #     self.table = table
    #     table_name = table.NAME
    #     if table_name=="1号桌":
    #         self.move(0,speed,[250,self.y])
    #         self.move(3,speed,[self.x,350])
    #     elif table_name=="2号桌":
    #         self.move(0, speed, [250, self.y])
    #         self.move(2, speed, [self.x, 550])
    #     elif table_name=="3号桌":
    #         self.move(0,speed,[350,self.y])
    #     elif table_name=="4号桌":
    #         self.move(0, speed, [250, self.y])
    #         self.move(3, speed, [self.x, 350])
    #         self.move(0,speed,[450,self.y])
    #     elif table_name=="5号桌":
    #         self.move(0, speed, [250, self.y])
    #         self.move(2, speed, [self.x, 550])
    #         self.move(0, speed, [450, self.y])
    def send_food(self, hand):
        if hand == "LEFT_HAND":
            self.screen.blit(self.bg,(0,0))
            # self.util.cancel_image(self.screen, self.left_rect.x, self.left_rect.y, self.left_rect.width,
            #                   self.left_rect.height)
            self.left_rect = None
        elif hand == "RIGHT_HAND":
            self.screen.blit(self.bg, (0, 0))
            # self.util.cancel_image(self.waiter_surface, self.right_rect.x, self.right_rect.y, self.right_rect.width,
            #                   self.right_rect.height)
            self.right_rect = None
        pygame.display.update()

    def pick_food(self, food_order,hand):
        if hand=="left":
            if self.d == 0:
                self.left_rect = self.util.blit_image(self.screen, Image.FOOD.get(food_order),10,10,
                                                      destX=self.rect.centerx + 2,
                                                      destY=self.rect.centery - 10)
            elif self.d == 1:
                self.left_rect = self.util.blit_image(self.screen, Image.FOOD.get(food_order),10,10,
                                                      destX=self.rect.centerx - 2, destY=self.rect.centery)
            elif self.d == 2:
                self.left_rect = self.util.blit_image(self.screen, Image.FOOD.get(food_order),10,10,
                                                      destX=self.rect.centerx + 2, destY=self.rect.centery)
            elif self.d == 3:
                self.left_rect = self.util.blit_image(self.screen, Image.FOOD.get(food_order),10,10,
                                                      destX=self.rect.centerx - 2, destY=self.rect.centery)
        elif hand=="right":
            if self.d == 0:
                self.right_rect = self.util.blit_image(self.screen, Image.FOOD.get(food_order), 10,10,destX=self.rect.centerx + 2,
                                                  destY=self.rect.centery)
            elif self.d == 1:
                self.right_rect = self.util.blit_image(self.screen, Image.FOOD.get(food_order),10,10,
                                                  destX=self.rect.centerx - 2, destY=self.rect.centery - 10)
            elif self.d == 2:
                self.right_rect = self.util.blit_image(self.screen, Image.FOOD.get(food_order),10,10,
                                                  destX=self.rect.centerx - 2, destY=self.rect.centery)
            elif self.d == 3:
                self.right_rect = self.util.blit_image(self.screen, Image.FOOD.get(food_order),10,10,
                                                  destX=self.rect.centerx + 2, destY=self.rect.centery)

        # if self.LEFT_HAND == False:
        #
        #     if self.d == 0:
        #         self.left_rect = self.util.blit_image(self.screen, food_rect, destX=self.rect.centerx + 10,
        #                                          destY=self.rect.centery - 10)
        #     elif self.d == 1:
        #         self.left_rect = self.util.blit_image(self.screen, food_rect,
        #                                          destX=self.rect.centerx - 10, destY=self.rect.centery + 10)
        #     elif self.d == 2:
        #         self.left_rect = self.util.blit_image(self.screen, food_rect,
        #                                          destX=self.rect.centerx + 10, destY=self.rect.centery + 10)
        #     elif self.d == 3:
        #         self.left_rect = self.util.blit_image(self.screen, food_rect,
        #                                          destX=self.rect.centerx - 10, destY=self.rect.centery - 10)
        #     self.LEFT_FOOD = food_order
        #
        # elif self.LEFT_HAND == True and self.RIGHT_HAND == False:
        #     if self.d == 0:
        #         self.right_rect = self.util.blit_image(self.screen, food_rect, destX=self.rect.centerx + 10,
        #                                           destY=self.rect.centery + 10)
        #     elif self.d == 1:
        #         self.right_rect = self.util.blit_image(self.screen, food_rect,
        #                                           destX=self.rect.centerx - 10, destY=self.rect.centery - 10)
        #     elif self.d == 2:
        #         self.right_rect = self.util.blit_image(self.screen, food_rect,
        #                                           destX=self.rect.centerx - 10, destY=self.rect.centery + 10)
        #     elif self.d == 3:
        #         self.right_rect = self.util.blit_image(self.screen, food_rect,
        #                                           destX=self.rect.centerx + 10, destY=self.rect.centery - 10)
        #     self.RIGHT_FOOD = food_order

        # pygame.display.update()
