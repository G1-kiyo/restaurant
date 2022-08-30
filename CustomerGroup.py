#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pygame
import random
from Util import Util
from Image import Image


class CustomerGroup:
    WAIT_PREPARED_TIMER = {"status": False, "interval": 0, "last_time": 0, "flag": False,
                                "remove": False}
    WAIT_REGISTER_TIMER = {"status": False, "interval": 0, "last_time": 0, "flag": False,
                                "remove": False}
    WAIT_EAT_TIMER = {"status": False, "interval": 0, "last_time": 0, "flag": False, "remove": False}
    WAIT_FINISH_TIMER = {"status": False, "interval": 0, "last_time": 0, "flag": False, "remove": False}
    WAIT = False
    WELL_PREPARED = False
    NEED = False
    NEED_REGISTERED = False
    EATING = False
    FINISH = False
    TABLE = None
    WAIT_TIME = 0
    LEAVE = False
    total = 0
    WARN = False
    PAID = False
    util = Util()
    def __init__(self, customer_list):
        self.customer_list = customer_list

    # def is_selected(self):
    #     for customer in self.customer_list:
    #         if customer.rect.collidepoint(self.point_pos[0],self.point_pos[1]):
    #             self.WELL_PREPARED = True
    def set_timer(self,timer_info):
        if timer_info["status"]==False and timer_info["remove"]==False:
            timer_info["last_time"] = pygame.time.get_ticks()
            timer_info["status"] = True
            # print(self.WAIT_PREPARED_TIMER["status"])
        elif timer_info["status"]==True and timer_info["remove"]==False:
            current_time = pygame.time.get_ticks()
            # print(current_time,timer_info["last_time"])
            if current_time - timer_info["last_time"] >= timer_info["interval"] and current_time - timer_info["last_time"] < timer_info["interval"] + 1000:
                self.WARN = True
            elif current_time - timer_info["last_time"] >= timer_info["interval"]+1000 and current_time - timer_info["last_time"] < timer_info["interval"] + 1500:
                self.WARN = False
            elif current_time - timer_info["last_time"] >= timer_info["interval"] + 1500:
                if timer_info["flag"] == False:
                    self.LEAVE = True
                timer_info["status"] = False
    def remove_timer(self,timer_info):
        timer_info["remove"]=True
    def set_wait_prepared_timer(self,interval):
        self.WAIT_PREPARED_TIMER["interval"] = interval
        self.WAIT_PREPARED_TIMER["flag"] = self.WELL_PREPARED
        # self.WAIT_PREPARED_TIMER = {"status":False,"interval":interval,"last_time":0,"flag":self.WELL_PREPARED,"remove":False}
        self.set_timer(self.WAIT_PREPARED_TIMER)
    def set_wait_register_timer(self,interval):
        self.WAIT_REGISTER_TIMER["interval"] = interval
        self.WAIT_REGISTER_TIMER["flag"] = self.NEED_REGISTERED
        # self.WAIT_REGISTER_TIMER = {"status":False,"interval":interval,"last_time":0,"flag":self.NEED_REGISTERED,"remove":False}
        self.set_timer(self.WAIT_REGISTER_TIMER)
    def set_wait_eat_timer(self,interval):
        self.WAIT_EAT_TIMER["interval"] = interval
        self.WAIT_EAT_TIMER["flag"] = self.EATING
        # self.WAIT_EAT_TIMER = {"status": False, "interval": interval, "last_time": 0, "flag": self.EATING,"remove":False}
        self.set_timer(self.WAIT_EAT_TIMER)
    def set_wait_finish_timer(self,interval):
        self.WAIT_FINISH_TIMER["interval"] = interval
        self.WAIT_FINISH_TIMER["flag"] = self.FINISH
        # self.WAIT_FINISH_TIMER = {"status": False, "interval": interval, "last_time": 0, "flag": self.FINISH,"remove":False}
        self.set_timer(self.WAIT_FINISH_TIMER)
        if self.LEAVE==True:
            self.FINISH=True

    def food_list(self):
        food_list = []
        for customer in self.customer_list:
            food_list.append(customer.food)
        return food_list

    def leaving_path(self, customer, speed, i, surface, d, destination):
        customer.move(d, speed + i, [customer.rect.x, destination])
        customer.move(0, speed + i, [1000, customer.rect.y])
        self.util.cancel_image(surface, customer.rect.x, customer.rect.y, customer.rect.width, customer.rect.height)
        pygame.display.update()

    def leaving_path_wait(self, surface, d):
        if d == 2:
            for i in range(len(self.customer_list)):
                customer = self.customer_list[i]
                customer.move(d, 5 + i, [customer.rect.x, 750])
                customer[i].move(1, 5 + i, [0, 750])
                self.util.cancel_image(surface, customer.rect.x, customer.rect.y, customer.rect.width, customer.rect.height)
                pygame.display.update()

        elif d == 3:
            for i in range(len(self.customer_list)):
                customer = self.customer_list[i]
                customer.move(d, 5 + i, [customer.rect.x, 200])
                customer[i].move(1, 5 + i, [0, 200])
                self.util.cancel_image(surface, customer.rect.x, customer.rect.y, customer.rect.width, customer.rect.height)
                pygame.display.update()

    def check_food(self):
        num = 0
        for customer in self.customer_list:
            if customer.food is None:
                num = num+1
        if num == len(self.customer_list):
            return True
        else:
            return False
    def finish_eating(self):
        # pygame.time.delay(random.randrange(50, 100))
        # self.EATING = False
        # self.FINISH = True
        num = len(self.customer_list)
        # 计算总额
        self.total = num * 30

        # if need == True:
        #     pygame.time.delay(random.randrange(500, 1500))
        #     self.EATING = False
        #     self.FINISH = True
        #     num = len(self.customer_list)
        #     # 计算总额
        #     self.total = num * 30
        #
        #     # 生成金钱图片在餐桌上
        #     money_rect = self.util.blit_image(surface, Image.MONEY, destX=table.rect.centerx - 20,
        #                                  destY=table.rect.centery - 20)
        # else:
        #     self.FINISH = True

        # 离开画面
        i = 0
        # for customer in self.customer_list:
        #     if customer.rect.y < table.rect.centery and table.x <= 450:
        #         self.leaving_path(customer, speed, i, surface, 3, 200)
        #     elif customer.rect.y > table.rect.centery and table.x <= 450:
        #         self.leaving_path(customer, speed, i, surface, 2, 350)
        #     elif customer.rect.y < table.rect.centery and table.x > 450:
        #         self.leaving_path(customer, speed, i, surface, 3, 550)
        #     elif customer.rect.y > table.rect.centery and table.x > 450:
        #         self.leaving_path(customer, speed, i, surface, 2, 750)
        #     i = i + 1
