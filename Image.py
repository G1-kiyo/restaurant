#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Image:
    MAIN_SCREEN = "./img/main_screen.png"
    START_BUTTON = "./img/start_button.png"
    MUSIC_SET_PLAY = "./img/music_set_play.png"
    MUSIC_SET_STOP = "./img/music_set_stop.png"

    SUB_SCREEN = "./img/sub_screen.png"
    TABLE = "./img/table.png"
    WAITER = {0: ["./img/waiter/0_1.png", "./img/waiter/0_2.png", "./img/waiter/0_3.png", "./img/waiter/0_4.png"],
              1: ["./img/waiter/1_1.png", "./img/waiter/1_2.png", "./img/waiter/1_3.png", "./img/waiter/1_4.png"],
              2: ["./img/waiter/2_1.png", "./img/waiter/2_2.png", "./img/waiter/2_3.png", "./img/waiter/2_4.png"],
              3: ["./img/waiter/3_1.png", "./img/waiter/3_2.png", "./img/waiter/3_3.png", "./img/waiter/3_4.png"]
              }
    KITCHEN = "./img/kitchen.png"
    FOOD_PROVIDE_TABLE = "./img/food_provide_table.png"
    SCORE = "./img/score.png"
    CABIN = "./img/cabin.png"
    CLOCK = ["./img/clock/clock_1.png", "./img/clock/clock_2.png", "./img/clock/clock_3.png", "./img/clock/clock_4.png",
             "./img/clock/clock_5.png", "./img/clock/clock_6.png"]
    CUSTOMER = {
        1: {0: ["./img/1/0_1.png", "./img/1/0_2.png", "./img/1/0_3.png", "./img/1/0_4.png"],
            1: ["./img/1/1_1.png", "./img/1/1_2.png", "./img/1/1_3.png", "./img/1/1_4.png"],
            2: ["./img/1/2_1.png", "./img/1/2_2.png", "./img/1/2_3.png", "./img/1/2_4.png"],
            3: ["./img/1/3_1.png", "./img/1/3_2.png", "./img/1/3_3.png", "./img/1/3_4.png"]
            },
        2: {0: ["./img/2/0_1.png", "./img/2/0_2.png", "./img/2/0_3.png", "./img/2/0_4.png"],
            1: ["./img/2/1_1.png", "./img/2/1_2.png", "./img/2/1_3.png", "./img/2/1_4.png"],
            2: ["./img/2/2_1.png", "./img/2/2_2.png", "./img/2/2_3.png", "./img/2/2_4.png"],
            3: ["./img/2/3_1.png", "./img/2/3_2.png", "./img/2/3_3.png", "./img/2/3_4.png"]},
        3: {0: ["./img/3/0_1.png", "./img/3/0_2.png", "./img/3/0_3.png", "./img/3/0_4.png"],
            1: ["./img/3/1_1.png", "./img/3/1_2.png", "./img/3/1_3.png", "./img/3/1_4.png"],
            2: ["./img/3/2_1.png", "./img/3/2_2.png", "./img/3/2_3.png", "./img/3/2_4.png"],
            3: ["./img/3/3_1.png", "./img/3/3_2.png", "./img/3/3_3.png", "./img/3/3_4.png"]},
        4: {0: ["./img/4/0_1.png", "./img/4/0_2.png", "./img/4/0_3.png", "./img/4/0_4.png"],
            1: ["./img/4/1_1.png", "./img/4/1_2.png", "./img/4/1_3.png", "./img/4/1_4.png"],
            2: ["./img/4/2_1.png", "./img/4/2_2.png", "./img/4/2_3.png", "./img/4/2_4.png"],
            3: ["./img/4/3_1.png", "./img/4/3_2.png", "./img/4/3_3.png", "./img/4/3_4.png"]},
        5: {0: ["./img/5/0_1.png", "./img/5/0_2.png", "./img/5/0_3.png", "./img/5/0_4.png"],
            1: ["./img/5/1_1.png", "./img/5/1_2.png", "./img/5/1_3.png", "./img/5/1_4.png"],
            2: ["./img/5/2_1.png", "./img/5/2_2.png", "./img/5/2_3.png", "./img/5/2_4.png"],
            3: ["./img/5/3_1.png", "./img/5/3_2.png", "./img/5/3_3.png", "./img/5/3_4.png"]}
    }
    FOOD = {}


    BUBBLE = "./img/bubble.png"

    MONEY = "./img/money.png"

    WARNING = "./img/warning.png"

    SETTING = "./img/setting.png"
    COVER = "./img/cover.png"
    SETTING_BOARD = "./img/setting_board.png"
    PAUSE = "./img/pause.png"
    CLOSE = "./img/close.png"

    FINAL_SCORE = "./img/final_score.png"

    def create_food(self):
        for i in range(1,121):
            self.FOOD[i] = "./img/food/"+str(i)+".png"
