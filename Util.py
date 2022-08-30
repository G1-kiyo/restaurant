#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pygame

class Util:

    def blit_image(self,surface,path,imgWidth=None,imgHeight=None,destX=None,destY=None):
        # print(self)
        img = pygame.image.load(path)
        if imgHeight is None and imgWidth is None:
            surface.blit(img,(destX,destY))
            rect = img.get_rect()
        else:
            surface.blit(pygame.transform.scale(img, (imgWidth, imgHeight)), (destX, destY))
            rect = pygame.Rect((destX,destY,imgWidth,imgHeight))

        # rect = img.get_rect()
        # rect[0] = destX
        # rect[1] = destY
        return rect

    def cancel_image(self,surface,x,y,w,h):
        surface.blit(surface,(x,y),area=pygame.Rect(x,y,w,h))
        pygame.display.update()

    def draw_text(self,surface,font_path,font_size,text,font_color,font_bg,destX,destY,w,h):
        pygame.font.init()
        font = pygame.font.Font(font_path, font_size)
        font.set_bold(True)

        text_surface = font.render(text, True,font_color,font_bg)
        # 文本rect
        text_rect = text_surface.get_rect()
        text_rect.center = (destX+w/2 , destY+h/2)
        # 积分框rect
        #self.score_rect = Util.blit_image(surface, path, imgWidth, imgHeight, destX, destY)

        # 带有文本的积分框
        # 第一个参数可以是图像，也可以是某个surface对象，第二个参数可以是目标坐标点或者rect
        surface.blit(text_surface, text_rect)
        return text_rect