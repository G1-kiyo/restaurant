#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pygame
from Image import Image
from Music import Music
from Util import Util
from Table import Table
from Waiter import Waiter
from Kitchen import Kitchen
from Score import Score
from Customer import Customer
import random
from CustomerGroup import CustomerGroup
from pygame.locals import *
from threading import Thread
import sys


class MainEntry:
    WAIT_WARN = True
    ORDER_WARN = True
    DISH_WARN = True
    GAME_SWITCH = False
    GAME_OVER = False
    START_GAME = False
    PAUSE = False
    SETTING = False
    MUSIC_STATUS = 0
    CLOCK = 0
    util = Util()
    dest_table = ()

    # 初始化窗口
    def init_window(self):
        # 使用pygame之前必须初始化
        # pygame.init()
        # 设置主屏窗口
        self.width = 1000
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))

        # 设置窗口的标题，即游戏名称
        pygame.display.set_caption('林间主题餐厅')
        # 绘制背景
        self.load_mainWindow()

        # pygame.display.update()
    def load_mainWindow(self):

        self.background_rect = self.util.blit_image(self.screen, Image.MAIN_SCREEN, self.width, self.height, 0, 0)
        # 开始按钮
        self.start_button_rect = self.util.blit_image(self.screen, Image.START_BUTTON, 200, 50, self.width / 2 - 100,
                                                      self.height / 2 - 25)
        self.temp = self.screen
        # 音乐控制按钮
        self.music_set_button = self.util.blit_image(self.screen, Image.MUSIC_SET_PLAY, 50, 50, self.width - 60,
                                                     self.height - 100)
    def init_subWindow(self):
        self.subWindow = pygame.Surface(size=(self.width, self.height))
        # 背景
        self.dinner_room_rect = self.util.blit_image(self.subWindow, Image.SUB_SCREEN, self.width, self.height, 0, 0)

        # 餐桌
        rowx = [300, 300, 450, 600, 600]
        coly = [280, 380, 340, 280, 380]
        pos_list = [(410, 330), (410, 430), (580, 350), (590, 330), (650, 380)]
        self.table_rect_list = []
        index = 1
        for i, j in zip(rowx, coly):
            table = Table(self.subWindow, Image.TABLE, 80, 80, i, j)
            table.pos = (table.rect.centerx,table.rect.centery)
            table.NAME = str(index) + "号桌"
            table.INDEX = index
            index = index + 1
            self.table_rect_list.append(table.rect)
            self.table_list[table.NAME] = table
            # self.table_list.append(table)

        # 服务员
        self.waiter = Waiter(self.screen, self.subWindow, 1, 25, 50, self.width - 250, self.height / 2)

        # 后厨
        self.kitchen = Kitchen(self.subWindow, Image.KITCHEN, 200, 100, self.width - 200, 250)

        # 积分
        self.score = Score(self.subWindow, Image.SCORE, 80, 40, self.width - 80, 50)

        # 时间
        self.clock = self.util.blit_image(self.subWindow, Image.CLOCK[self.CLOCK], 50, 50, 20, 20)

        # 垃圾桶
        self.cabin = self.util.blit_image(self.subWindow, Image.CABIN, 100, 80, self.width - 100, 350)

        # 设置按钮
        self.setting = self.util.blit_image(self.subWindow, Image.SETTING, 50, 50, self.width - 50, self.height - 50)

        # self.subWindow_surface_rect = self.util.blit_image(self.screen, self.subWindow, destX=0, destY=0)

        self.subWindow_surface_rect = self.screen.blit(self.subWindow, (0, 0))

    def load_setting(self):
        self.setting_surface = pygame.Surface(size=(self.width, self.height))
        self.setting_bg = self.util.blit_image(self.setting_surface, Image.COVER, self.width, self.height, 0, 0)

        self.screen.blit(self.setting_surface,(0,0))
        # pygame.display.update()
    def load_setting_detail(self):
        self.setting_detail = self.util.blit_image(self.setting_surface, Image.SETTING_BOARD, 300, 300,
                                                   self.width / 2 - 150,
                                                   self.height / 2 - 150)
        self.close_button_rect = self.util.blit_image(self.setting_surface, Image.CLOSE, 30, 30, self.width / 2 + 160,
                                                      self.height / 2 - 150)
        self.pause_game_rect = self.util.draw_text(self.setting_surface, "./font/pause_game.ttf", 20, "暂停游戏", "#000000",
                                                   None, self.setting_detail.x, self.setting_detail.y, 300,
                                                   100)
        self.close_music_rect = self.util.draw_text(self.setting_surface, "./font/close_music.ttf", 20, "关闭音乐",
                                                    "#000000",
                                                    None,
                                                    self.setting_detail.x, self.setting_detail.y, 300,
                                                    200)
        self.close_game_rect = self.util.draw_text(self.setting_surface, "./font/close_game.ttf", 20, "关闭游戏", "#000000",
                                                   None,
                                                   self.setting_detail.x, self.setting_detail.y, 300,
                                                   300)
        self.return_main_window = self.util.draw_text(self.setting_surface, "./font/return_main_window.ttf", 20,
                                                      "返回主菜单",
                                                      "#000000", None,
                                                      self.setting_detail.x, self.setting_detail.y, 300,
                                                      400)
        self.screen.blit(self.setting_surface, (0, 0))
    def load_score(self):
        self.subWindow = pygame.Surface(size=(self.width, self.height))
        # 背景
        self.dinner_room_rect = self.util.blit_image(self.subWindow, Image.SUB_SCREEN, self.width, self.height, 0, 0)

        score_board = self.util.blit_image(self.subWindow,Image.FINAL_SCORE,400, 300,
                                                   self.width / 2 - 200,
                                                   self.height / 2 - 150)
        self.util.draw_text(self.subWindow,"./font/final_score.ttf", 20,
                                                      "最高积分",
                                                      "#000000", None,
                                                      score_board.x, score_board.y, 200,
                                                      300)
        self.util.draw_text(self.subWindow, "./font/final_score.ttf", 20,
                            str(self.highest_score),
                            "#000000", None,
                            score_board.x, score_board.y, 400,
                            300)

        self.util.draw_text(self.subWindow, "./font/final_score.ttf", 20,
                            "当前积分",
                            "#000000", None,
                            score_board.x, score_board.y, 200,
                            400)
        self.util.draw_text(self.subWindow, "./font/final_score.ttf", 20,
                            str(self.score.score),
                            "#000000", None,
                            score_board.x, score_board.y, 400,
                            400)
        self.subWindow_surface_rect = self.screen.blit(self.subWindow, (0, 0))
    def load_pause_button(self):
        # self.close_button_rect = None
        # self.close_music_rect = None
        # self.close_game_rect = None
        # self.return_main_window = None
        self.pause_game_rect = self.util.blit_image(self.setting_surface, Image.PAUSE, 50, 50,
                             self.width / 2 - 25,
                             self.height / 2 - 25)
        self.screen.blit(self.setting_surface, (0, 0))

    def save_score(self):
        score = 0
        new_score = self.score.score
        with open('highest_score.txt','r')as f:
            score = int(f.readline())
        if score<new_score:
            with open('highest_score.txt','w')as file:
                self.highest_score = new_score
                file.write(str(new_score))
        else:
            self.highest_score = score
    def load_customer(self):
        num = random.randint(1, 4)
        current_customer = []
        for i in range(num):
            type = random.randint(1, 5)
            customer = Customer(type, 0, 30, 50, centerX=0, centerY=325 + i * 10)
            current_customer.append(customer)
        customer_group = CustomerGroup(current_customer)
        self.waiting_queue.append(customer_group)

    # 音频设置
    def music_set(self, path, volume, play, loop):
        pygame.mixer.init()  # 初始化混音器模块（pygame库的通用做法，每一个模块在使用时都要初始化pygame.init()为初始化所有的pygame模块，可以使用它也可以单初始化这一个模块）
        pygame.mixer.music.load(path)  # 加载音乐
        pygame.mixer.music.set_volume(volume)  # 设置音量大小0~1的浮点数
        # 0代表正在播放 1代表暂停 2代表从暂停中恢复（保持原来的音乐进度）3代表停止
        if play == "play":
            pygame.mixer.music.play(loops=loop)  # 播放音频
            self.MUSIC_STATUS = 0
        elif play == "pause":
            pygame.mixer.music.pause()
            self.MUSIC_STATUS = 1
        elif play == "resume":
            pygame.mixer.music.unpause()
            self.MUSIC_STATUS = 2
        else:
            pygame.mixer.music.stop()
            self.MUSIC_STATUS = 3

    # 确定食物图片在餐桌上的位置
    def food_table_pos(self, customer):
        # print(customer.seat_key)
        if customer.seat_key!=0:
            if customer.seat_key == 1:
                food_rect = self.util.blit_image(self.screen, Image.FOOD.get(customer.saved_food),
                                                 destX=customer.seat_pos[0] + 10,
                                                 destY=customer.seat_pos[1] + 10)
            elif customer.seat_key == 2:
                food_rect = self.util.blit_image(self.screen,
                                                 Image.FOOD.get(customer.saved_food),
                                                 destX=customer.seat_pos[0] + 10,
                                                 destY=customer.seat_pos[1] - 10)
            elif customer.seat_key == 3:
                food_rect = self.util.blit_image(self.screen,
                                                 Image.FOOD.get(customer.saved_food),
                                                 destX=customer.seat_pos[0] - 10,
                                                 destY=customer.seat_pos[1] + 10)
            elif customer.seat_key == 4:
                food_rect = self.util.blit_image(self.screen,
                                                 Image.FOOD.get(customer.saved_food),
                                                 destX=customer.seat_pos[0] + 10,
                                                 destY=customer.seat_pos[1] - 10)

    # 提示文字的显示控制
    def warning_text_control(self, text):
        self.util.blit_image(self.screen, Image.WARNING, 500, 100, self.width / 2 - 250,
                             self.height / 2 - 50)
        self.util.draw_text(self.screen, "./font/warn.ttf", 30, text,
                            "#000000", None, self.width / 2 - 250, self.height / 2 - 50, 500, 100)
        # pygame.time.delay(200)
        # self.util.cancel_image(self.subWindow, self.width / 2 - 100,
        #                        self.height / 2 - 50, 200, 100)
    def waiter_move(self,dest,rect_list):
        if self.waiter.x == dest[0] and self.waiter.y == dest[1]:
            self.waiter.MOVE = False
            self.waiter.Y_GO = False
            self.waiter.X_GO = False
        if self.waiter.x <= dest[0] and self.waiter.X_GO == True:
            self.waiter.move(0, [5, 5], dest)
        elif self.waiter.x >= dest[0] and self.waiter.X_GO == True:
            self.waiter.move(1, [5, 5], dest)
        elif self.waiter.y >= dest[1] and self.waiter.Y_GO == True:
            self.waiter.move(3, [5, 5], dest)
        elif self.waiter.y <= dest[1] and self.waiter.Y_GO == True:
            self.waiter.move(2, [5, 5], dest)
        # elif self.waiter.x == dest[0] and self.waiter.y == dest[1]:
        #     self.waiter.MOVE = False

        if (self.waiter.d == 0 or self.waiter.d == 1) and self.waiter.rect.collidelist(rect_list) != -1:
            self.waiter.X_GO = False
            self.waiter.Y_GO = True
            
        elif (self.waiter.d == 2 or self.waiter.d == 3) and self.waiter.rect.collidelist(rect_list) != -1:
            self.waiter.Y_GO = False
            self.waiter.X_GO = True
        elif self.waiter.rect.collidelist(rect_list) == -1:
            self.waiter.Y_GO = True
            self.waiter.X_GO = True
    def refresh_waiting_queue(self):
        index = 0
        for customer_group in self.waiting_queue:
            # print(f'len1:{len(self.waiting_queue)}')
            if customer_group.LEAVE == False:
                for customer_order in range(len(customer_group.customer_list)):
                    # print("第"+str(group_order)+"组第"+str(customer_order)+"人在moving")
                    # 仅更新对象类的变量,绘图在主程序内绘制
                    customer = customer_group.customer_list[customer_order]
                    # print(f'len2:{len(self.waiting_queue)}')
                    customer.move(0, [5 - customer_order,
                                      5 - customer_order], (
                                      150 - index * 30,
                                      325 + customer_order * 10))

                    self.util.blit_image(self.screen,
                                         Image.CUSTOMER.get(customer.type).get(customer.d)[customer.order], 30,
                                         50,
                                         customer.x - 15, customer.y - 25)
            index = index+1
    def customer_leave(self,customer_group,queue):
        index = 0
        for customer in customer_group.customer_list:
            # print("this is"+str(customer.y)+","+str(customer.x))
            if customer.y < 480 and customer.y > 240:

                if customer.y >= 370:
                    customer.move(2, [5, 5], (0, 480))
                else:
                    customer.move(3, [5, 5], (0, 240))
                    # print(customer.d)
            elif (customer.y == 480 or customer.y == 240) and customer.x < 400:
                customer.move(0, [5 - index, 5 - index], (400, 0))
            elif customer.x >= 400:

                # print(111)
                customer.LEAVED = True

            if customer.LEAVED == True:
                if index == len(customer_group.customer_list) - 1:
                    queue.remove(customer_group)
                    # self.waiting_queue_change-= 1
                    # self.refresh_waiting_queue()
                    pass
            else:

                self.util.blit_image(self.screen,
                                     Image.CUSTOMER.get(customer.type).get(customer.d)[
                                         customer.order], 30, 50, customer.x - 15,
                                     customer.y - 25)
            index = index + 1

        # print(customer.y,customer.d)
    #
    def set_timer(self,timer_info):
        if timer_info["status"]==False:
            timer_info["last_time"] = pygame.time.get_ticks()
            timer_info["status"] = True
            timer_info["flag"]=False
        else:
            current_time = pygame.time.get_ticks()
            if current_time-timer_info["last_time"]>=timer_info["interval"]:
                timer_info["status"] = False
                timer_info["flag"] = True
    # 事件处理
    def event_handler(self):
        eventlist = pygame.event.get()

        for e in eventlist:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                x = e.pos[0]
                y = e.pos[1]
                # 左键1  按下滚轮2 上转滚轮为4 下转滚轮为5  右键 3
                if e.button == 1:
                    print(x, y)
                    if self.start_button_rect.collidepoint(x, y):
                        self.START_GAME = True
                    # 设置音乐按钮
                    if self.music_set_button.collidepoint(x, y):
                        if self.MUSIC_STATUS == 0:
                            self.music_set(Music.MAIN_MUSIC, 0.5, "stop", -1)
                            self.music_set_button = self.util.blit_image(self.screen, Image.MUSIC_SET_STOP, 50, 50,
                                                                         self.width - 60,
                                                                         self.height - 100)
                            pygame.display.update()
                            self.MUSIC_STATUS = 3
                        else:
                            self.music_set(Music.MAIN_MUSIC, 0.5, "play", -1)
                            self.music_set_button = self.util.blit_image(self.screen, Image.MUSIC_SET_PLAY, 50, 50,
                                                                         self.width - 60,
                                                                         self.height - 100)
                            pygame.display.update()
                            self.MUSIC_STATUS = 0

    def sub_event_handler(self):
        # 获取事件列表
        eventlist = pygame.event.get()

        for e in eventlist:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type==pygame.USEREVENT:
                self.text_control = False

            if e.type==self.clock_timer[0]:
                if self.CLOCK<5:
                    self.CLOCK = self.CLOCK+1


            if e.type == pygame.MOUSEBUTTONDOWN:
                x = e.pos[0]
                y = e.pos[1]
                # 左键1  按下滚轮2 上转滚轮为4 下转滚轮为5  右键 3
                if e.button == 1:
                    if len(self.waiting_queue) != 0:
                        # print(self.waiting_queue)
                        for customer in self.waiting_queue[0].customer_list:
                            rect = pygame.Rect((customer.x, customer.y, customer.w, customer.h))
                            if rect.collidepoint(x, y):
                                # self.customer_wait_group = CustomerGroup(self.waiting_queue[0])
                                self.waiting_queue[0].WELL_PREPARED = True
                                break
                    # 设置按钮相关操作
                    if self.setting is not None and self.setting.collidepoint(x, y):
                        self.SETTING = True
                    # 垃圾桶操作
                    if self.cabin is not None and self.cabin.collidepoint(x, y):
                        self.waiter.STATUS="discard_food"
                        # self.waiter.find_path(5, [self.waiter.rect.x, self.waiter.rect.y],
                        #                       [self.cabin.rect.x, self.cabin.rect.centery])
                        if self.waiter.food["left"] is not None:
                            self.waiter.food["left"] = None
                        if self.waiter.food["right"] is not None:
                            self.waiter.food["right"] = None
                    for key in self.table_list:
                        table = self.table_list[key]
                        if table.rect.collidepoint(x, y):
                            # 查看餐桌是否有人
                            if table.ISUSING == False and table.USED == False:
                                # 查看是否有点击等待的顾客
                                if len(self.waiting_queue) != 0 and self.waiting_queue[0].WELL_PREPARED == True:
                                    temp = self.waiting_queue[0]
                                    temp.TABLE = table
                                    temp.WAIT = False
                                    self.using_queue.append(temp)
                                    self.waiting_queue.pop(0)
                                    table.ISUSING = True

                                # 服务员到达指定桌子
                                else:
                                    self.waiter.MOVE = True
                                    self.dest_table = table
                                    self.waiter.STATUS = "none"
                            else:
                                self.waiter.MOVE = True
                                self.dest_table = table

                                # 判断餐桌是否有人使用，如果有，判断是那一组人在使用--1.已经就坐，但还没提出需求 2.提出需求，但还没登记 3.登记了还没送到 4.送到了在吃了
                                if table.ISUSING == True:
                                    for group in self.using_queue:
                                        # 如果当前组还没有就餐，且发起需求，厨房进行登记，并准备提供食物
                                        if group.TABLE.NAME == table.NAME:
                                            if group.NEED == True and group.NEED_REGISTERED == False:
                                                self.waiter.STATUS = "register"
                                                self.waiter.register["table"] = table
                                                self.waiter.register["group"] = group
                                                # self.kitchen.provide_food()
                                            elif group.NEED == True and group.NEED_REGISTERED == True and group.EATING == False:
                                                # group.WAIT = False
                                                self.waiter.STATUS = "send_food"
                                                self.waiter.send["table"] = table
                                                self.waiter.send["group"] = group

                                    for group in self.leaving_queue:
                                        if group.EATING==True and group.FINISH==True:
                                            self.waiter.STATUS = "profit"
                                            self.waiter.profit["table"] = table
                                            self.waiter.profit["group"] = group

                                                # self.score.update(group.total)

                    # 点击食物图片，服务员领取，厨房删除，与后续更新摆放的实物图片顺序有关
                    if self.kitchen is not None:
                        for food in self.kitchen.all_food_rect:
                            if food[0].collidepoint(x, y):
                                if self.waiter.food["left"] is None:
                                    self.waiter.food["left"] = food[1]
                                    self.kitchen.prepare_list.pop(food[2])
                                elif self.waiter.food["right"] is None:
                                    self.waiter.food["right"] = food[1]
                                    self.kitchen.prepare_list.pop(food[2])
                    #必须先点击
                    if self.kitchen is not None and self.kitchen.rect.collidepoint(x,y):
                        self.waiter.MOVE=True
                        self.waiter.STATUS = "pick_food"
                        self.waiter.kitchen = (self.kitchen.rect.x+25,self.kitchen.rect.y+100)



    def setting_event_handler(self):
        # 获取事件列表
        eventlist = pygame.event.get()

        for e in eventlist:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                x = e.pos[0]
                y = e.pos[1]
                # 左键1  按下滚轮2 上转滚轮为4 下转滚轮为5  右键 3
                if e.button == 1:
                    # 关闭设置窗口
                    if self.close_button_rect is not None and self.close_button_rect.collidepoint(x, y):
                        self.SETTING = False
                    # 暂停游戏
                    if self.pause_game_rect is not None and self.pause_game_rect.collidepoint(x, y):
                        if self.PAUSE:
                            self.SETTING = False

                        self.PAUSE = not self.PAUSE

                    # 关闭音乐
                    if self.close_music_rect is not None and self.close_music_rect.collidepoint(x, y):
                        self.music_set(Music.MAIN_MUSIC, 0.5, "stop", -1)
                        self.MUSIC_STATUS = 3
                    # 关闭游戏
                    if self.close_game_rect is not None and self.close_game_rect.collidepoint(x, y):
                        self.GAME_OVER = True
                    # 返回主菜单
                    if self.return_main_window is not None and self.return_main_window.collidepoint(x, y):
                        self.START_GAME = False
                        # self.load_mainWindow()
    def init_game(self):
        self.score = None
        self.kitchen = None
        self.waiter = None
        self.cabin = None
        self.table_list = {}
        self.waiting_queue = []
        self.using_queue = []
        self.leaving_queue = []
        self.customer_wait_group = None
        self.setting = None
        self.close_button_rect = None
        self.pause_game_rect = None
        self.close_game_rect = None
        self.close_music_rect = None
        self.return_main_window = None
        img = Image()
        img.create_food()

        self.init_window()
        self.music_set(Music.MAIN_MUSIC, 0.5, "play", -1)
        self.GAME_INIT = True

    def switch_game(self):
        self.util.cancel_image(self.screen, 0, 0, self.width, self.height)
        self.init_subWindow()
        self.music_set(Music.MAIN_MUSIC, 0.5, "play", -1)
        self.GAME_SWITCH = True

    def start_game(self):
        pygame.init()
        self.init_game()
        self.event_handler()
        pygame.display.update()
        TEXT_INTERVAL = USEREVENT
        random_load_customer = random.randrange(1500, 3000)
        CLOCK_TIMER = USEREVENT+1
        self.clock_timer = [CLOCK_TIMER,False]
        self.cutomer_load_timer = {"interval":0,"last_time":0,"status":False,"flag":False}
        timer2 = USEREVENT + 2
        timer3 = USEREVENT + 3
        self.text_control = True
        self.GAME_END = False
        # self.waiting_queue_change = 0
        # pygame.time.Clock().tick(30)
        while not self.GAME_OVER:
            # self.event_handler()
            self.event_handler()
            if not self.START_GAME and not self.GAME_INIT:
                self.init_game()
                self.GAME_INIT = True
                self.SETTING = False
                self.PAUSE = False
                self.GAME_SWITCH = False
            if not self.START_GAME and self.GAME_END:
                self.load_score()
            if self.SETTING and self.START_GAME:
                self.load_setting()
                if self.PAUSE:
                    self.load_pause_button()
                else:
                    self.load_setting_detail()
                self.setting_event_handler()
            if not self.GAME_OVER and not self.PAUSE and self.START_GAME and not self.SETTING:
                # self.GAME_INIT = False
                if not self.GAME_SWITCH:
                    self.switch_game()

                current_time = pygame.time.get_ticks()


                self.screen.blit(self.subWindow, (0, 0))
                # 计时，更换时钟图片
                if self.clock_timer[1]==False:
                    pygame.time.set_timer(self.clock_timer[0],10000)
                    self.clock_timer[1] = True
                if self.CLOCK==5:
                    self.save_score()
                    self.START_GAME = False
                    self.GAME_END = True



                self.clock = self.util.blit_image(self.subWindow, Image.CLOCK[self.CLOCK], 50, 50, 20, 20)
                # 计时，加载顾客
                if self.cutomer_load_timer["status"]==False:
                    self.cutomer_load_timer["interval"] = random.randrange(1500, 3000)
                self.set_timer(self.cutomer_load_timer)
                if self.cutomer_load_timer["flag"]==True:
                    if len(self.waiting_queue)<3:
                        self.load_customer()
                        # self.waiting_queue_change+=1
                # 检查顾客的状态 1.等待，且尚未入座 2.入座了但没有登记需求 3.登记需求了但菜还没送到
                if self.waiting_queue is not None and len(self.waiting_queue) != 0:
                    for customer_group in self.waiting_queue:
                        customer_group.set_wait_prepared_timer(10000)
                        if customer_group.WARN==True and customer_group.WELL_PREPARED==False:
                            self.warning_text_control("顾客快等不及啦")
                        if customer_group.LEAVE==True:
                            self.customer_leave(customer_group,self.waiting_queue)
                    self.refresh_waiting_queue()

                for customer_group in self.using_queue:
                    if customer_group.NEED==True:
                        customer_group.set_wait_register_timer(10000)
                    if customer_group.NEED_REGISTERED==True:
                        customer_group.remove_timer(customer_group.WAIT_REGISTER_TIMER)
                        customer_group.set_wait_eat_timer(100000)
                    if customer_group.EATING == True:
                        customer_group.remove_timer(customer_group.WAIT_EAT_TIMER)
                        customer_group.set_wait_finish_timer(10000)
                    if customer_group.FINISH==True:
                        customer_group.remove_timer(customer_group.WAIT_FINISH_TIMER)
                        customer_group.finish_eating()
                        if customer_group.total !=0:
                            for customer in customer_group.customer_list:
                                # 统统设置为0，不渲染
                                customer.seat_key = 0
                                self.food_table_pos(customer)


                    if customer_group.WARN==True:
                        if customer_group.NEED == True and customer_group.NEED_REGISTERED == False:
                            self.warning_text_control("第" + customer_group.TABLE.NAME + "顾客想点菜啦")
                        elif customer_group.NEED == True and customer_group.NEED_REGISTERED == True and \
                            customer_group.EATING == False:
                            self.warning_text_control("第" + customer_group.TABLE.NAME + "顾客想问菜怎么还没上")
                    if customer_group.LEAVE==True:
                        self.leaving_queue.append(customer_group)
                        self.customer_leave(customer_group,self.using_queue)


                    if customer_group.TABLE != "":

                        table = customer_group.TABLE
                        for i in range(len(customer_group.customer_list)):
                            seatX = table.seat.get(i + 1).get("pos")[0]  # 335,280
                            seatY = table.seat.get(i + 1).get("pos")[1]
                            # print(f'seatX:{seatX},seatY:{seatY}')
                            customer = customer_group.customer_list[i]
                            # if i==1:
                                # print(f'seatX{seatX},seatY{seatY},customerY{customer.y},customerX{customer.x}')
                            # customer.find_path([5 - i * 5,5-i*5], self.table_list[customer_group.TABLE])
                            # if customer.y<seatY:
                            #     customer.move(2, [5, 5], (0, seatY))
                            # elif customer.y>seatY:
                            #     customer.move(3, [5, 5], (0, seatY))
                            # elif customer.y==seatY:
                            #     if customer.x<seatX:
                            #         customer.move(0, [5, 5], (seatX, 0))
                            #     # elif customer.x>seatX:
                            #     #     customer.move(1, [5, 5], (seatX, 0))

                            if customer.x < 280:
                                customer.move(0, [5, 5], (280, 0))
                            elif customer.x >= 280 and customer.x<=seatX and customer.y == seatY:
                                customer.move(0, [5, 5], (425, 325))
                            elif customer.x >= 280 and customer.x<=seatX and customer.y < seatY:
                                # print(f'{i}goes')
                                customer.move(2, [5, 5], (0, seatY))
                            elif customer.x == 280 and customer.y > seatY:
                                # print(customer.order,customer.y,5-i)
                                customer.move(3, [5, 5], (0, seatY))
                            elif customer.y == seatY and customer.x < seatX and customer.x > 280:
                                customer.move(0, [5, 5], (seatX, 0))
                            else:
                                if customer_group.LEAVE==True:
                                    customer.MOVE = True
                                else:
                                    customer.MOVE = False
                                # customer.MOVE=False


                            # print("第" + str(i) + "人在moving,他的坐标是("+str(customer.x)+","+str(customer.y)+")")
                            if customer.MOVE == True:
                                self.util.blit_image(self.screen,
                                                     Image.CUSTOMER.get(customer.type).get(customer.d)[customer.order],
                                                     30,
                                                     50, customer.x - 15, customer.y - 25)
                            else:
                                if customer.NEED==False:
                                    customer.ask_for_food()
                                    customer.NEED=True
                                customer_group.NEED = True
                                # customer_group.WAIT = True
                                # self.warn = True
                                # if customer_group.WAIT_TIME > 0:
                                #     pass
                                # else:
                                #     customer_group.WAIT_TIME = pygame.time.get_ticks()
                                customer = customer_group.customer_list[i]
                                customer.seat_key = i+1
                                customer.find_seat(i,self.screen)

                            if customer.saved_food is not None:
                                self.food_table_pos(customer)



                            # 等候5秒左右发出需求
                    if customer_group.NEED == True and customer_group.EATING==False:

                        for i in range(len(customer_group.customer_list)):
                            # 等候5秒左右发出需求
                            customer = customer_group.customer_list[i]
                            if customer.food is not None:
                                self.bubble_rect = self.util.blit_image(self.screen, Image.BUBBLE, 30, 30,
                                                                        destX=
                                                                        customer_group.TABLE.seat[i + 1].get("pos")[
                                                                            0],
                                                                        destY=
                                                                        customer_group.TABLE.seat[i + 1].get("pos")[
                                                                            1] - 50)
                                self.food_rect = self.util.blit_image(self.screen, Image.FOOD.get(customer.food), 30,
                                                                      30,
                                                                      destX=customer_group.TABLE.seat[i + 1].get("pos")[
                                                                          0],
                                                                      destY=customer_group.TABLE.seat[i + 1].get("pos")[
                                                                                1] - 50)
                    # 计时，顾客完成就餐，离开
                for group in self.leaving_queue:
                    if group.total!=0 and group.PAID==False:
                        money_rect = self.util.blit_image(self.screen, Image.MONEY, 30, 30,
                                                          destX=group.TABLE.rect.centerx-20,
                                                          destY=group.TABLE.rect.centery-20)

                if self.waiter.food["left"] is not None:
                    self.waiter.pick_food(self.waiter.food["left"], "left")
                if self.waiter.food["right"] is not None:
                    self.waiter.pick_food(self.waiter.food["right"], "right")

                if self.waiter.MOVE == True:
                    # print(self.waiter.y) kitchen 800 250
                    if self.waiter.STATUS=="pick_food" and self.waiter.kitchen is not None:
                        # self.waiter_move(self.waiter.kitchen,self.table_rect_list)
                        self.waiter.find_path([5,5],(self.waiter.x,self.waiter.y),self.waiter.kitchen)

                    elif self.waiter.STATUS=="discard_food" and self.cabin is not None:
                        temp = self.table_rect_list.append(self.waiter.kitchen)
                        # self.waiter_move((self.cabin.x-20,self.cabin.y+20),temp)
                        self.waiter.find_path([5, 5], (self.waiter.x, self.waiter.y), (self.cabin.x-20,self.cabin.y+20))
                        self.waiter.STATUS = "none"

                    else:

                        self.waiter.find_path([5, 5], (self.waiter.x, self.waiter.y), self.dest_table.pos)


                    self.waiter.rect = self.util.blit_image(self.screen, Image.WAITER.get(self.waiter.d)[self.waiter.order], 30, 50,
                                         self.waiter.x - 25, self.waiter.y - 50)
                else:
                    if self.waiter.STATUS == "register":
                        food_list = self.waiter.register["group"].food_list()
                        self.kitchen.record_food(food_list)
                        # self.waiter.register["group"].WAIT = True
                        # self.warn = True
                        # if self.waiter.register["group"].WAIT_TIME > 0:
                        #     pass
                        # else:
                        #     self.waiter.register["group"].WAIT_TIME = pygame.time.get_ticks()
                        self.waiter.register["group"].NEED_REGISTERED = True
                        # print(self.waiter.register["group"].NEED_REGISTERED)
                        self.waiter.STATUS = "none"

                    elif self.waiter.STATUS=="pick_food":
                        # print(222)

                        pass
                    elif self.waiter.STATUS=="send_food":
                        # print(111)
                        customer_group = self.waiter.send["group"]
                        for customer in customer_group.customer_list:
                            print(f'food:{customer.food}')
                            if customer.food is not None:

                                if self.waiter.food["left"] and customer.food == self.waiter.food["left"]:
                                    customer.saved_food = customer.food
                                    self.waiter.food["left"] = None
                                    customer.food = None
                                elif self.waiter.food["right"] and customer.food == self.waiter.food["right"]:
                                    customer.saved_food = customer.food
                                    self.waiter.food["right"] = None
                                    customer.food = None


                        isALLSent = customer_group.check_food()
                        if isALLSent == True:
                            customer_group.EATING = True
                        # if len(list(map(lambda x:x.food is None,customer_group.customer_list)))==0:
                        #     # customer_group.NEED = False
                        # if customer_group is not None:
                        #     # customer_group.WAIT = False
                        #     # customer_group.finish_eating()

                    elif self.waiter.STATUS=="profit":
                        group = self.waiter.profit["group"]
                        group.PAID = True
                        self.score.update(group.total)
                        group.total = 0

                        # print(group.total)


                        # self.waiter.STATUS = "none"


                    self.waiter.rect = self.util.blit_image(self.screen, Image.WAITER.get(self.waiter.d)[self.waiter.order], 30, 50,
                                         self.waiter.x - 25, self.waiter.y - 50)

                # 更新排队的队伍形式
                # for customer_group in self.waiting_queue:
                # for group_order in range(len(self.waiting_queue)):
                #     if self.waiting_queue[group_order].LEAVE == True:
                #         pass
                #     else:
                #         for customer_order in range(len(self.waiting_queue[group_order].customer_list)):
                #             # print("第"+str(group_order)+"组第"+str(customer_order)+"人在moving")
                #             # 仅更新对象类的变量,绘图在主程序内绘制
                #             customer = self.waiting_queue[group_order].customer_list[customer_order]
                #
                #         # if len(self.waiting_queue) == 0:
                #         #
                #         #     customer.move(0, [5 - customer_order,
                #         #                       5 - customer_order],
                #         #                   (150, 325 + customer_order * 10))
                #         # else:
                #         # print("调用")
                #             customer.move(0, [5 - customer_order,
                #                           5 - customer_order], (
                #                           150 - len(self.waiting_queue) * 30,
                #                           325 + customer_order * 10))

                            # if group_order == 0 and customer_order == len(self.waiting_queue[group_order].customer_list) - 1:
                            #     if customer.x == 150 - len(self.waiting_queue) * 30 and customer.y == 325 + customer_order * 10:
                            #         self.waiting_queue[0].WAIT = True
                            #         self.warn = True
                            #         if self.waiting_queue[0].WAIT_TIME > 0:
                            #             pass
                            #         else:
                            #             self.waiting_queue[0].WAIT_TIME = pygame.time.get_ticks()


            #更新厨房供菜
            if self.kitchen is not None and len(self.kitchen.prepare_list) != 0:
                self.kitchen.all_food_rect = []
                for i in range(1, 7):
                    food_rect = self.util.blit_image(self.screen, Image.FOOD.get(self.kitchen.prepare_list[i - 1]), 30,
                                                     30,
                                                     destX=850 + i * 20,
                                                     destY=260)
                    self.kitchen.all_food_rect.append((food_rect,self.kitchen.prepare_list[i-1],i-1))
                    if i + 1 > len(self.kitchen.prepare_list):
                        break

            # # #
            #     # 更新食物的提供形式 rect
            #     count = 0
            #     for food_rect, food_order in self.kitchen.all_food_rect:
            #         rect = self.util.blit_image(self.subWindow, food_rect, destX=food_rect.x,
            #                                     destY=self.kitchen.rect.y + 20 + count * 50)
            #         count = count + 1
            self.sub_event_handler()
            pygame.display.update()


if __name__ == '__main__':
    mainEntry = MainEntry()
    mainEntry.start_game()
