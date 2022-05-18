import pygame
import sys
from pygame.locals import*
import numpy as np
from random import randint
from Map import *

class Show:
    def __init__(self,size):
        self.screen=pygame.display.set_mode(size)
        self.bg=(255,255,0)#背景的颜色
        self.COlOR=(255,0,0)#细胞的颜色

