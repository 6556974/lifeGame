import pygame
import sys
from pygame.locals import*
import numpy as np
from random import randint
from Map import *
from Show import *
from Logic import *

if __name__ == '__main__':
    mp = Map(10, 800, 500)
    Logic().solve(mp.x_rect, mp.y_rect, mp.ground)
