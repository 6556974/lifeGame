import pygame
import sys
from pygame.locals import*
import numpy as np
from random import randint
from Show import *

class Map:
    def __init__(self,rect_width,width,height):
        self.rect_width = rect_width
        self.size = width, height
        self.x_rect = int(width / rect_width)
        self.y_rect = int(height / rect_width)  # 长宽格子各有多个
        self.ground = np.zeros([self.x_rect, self.y_rect])  # 当前所有细胞占据的矩阵，0是没有。

    def InitGround(self):
        for i in range(1, self.x_rect - 1):
            for j in range(1, self.y_rect - 1):
                if randint(1, 10) < 2:
                    self.ground[i][j] = 1
                else:
                    pass

    def get_rect(self, row, column):  # 计算应该在哪里画方格，以右上角为点。
        x1 = self.rect_width * row
        y1 = self.rect_width * column


    def draw_live(self, x, y):
        pygame.draw.rect(screen, COLOR, get_rect(x, y), 0)

