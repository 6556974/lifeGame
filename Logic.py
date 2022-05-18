import pygame
import sys
from pygame.locals import *
import numpy as np
from random import randint
from Map import *


class Logic:
    def live_num(self, ground, x, y):  # 注意：为了避免出现ground[-1][-1]的情况，我们需要从1开始
        neighbour = [ground[x][y - 1], ground[x][y + 1], ground[x - 1][y], ground[x + 1][y]
            , ground[x - 1][y - 1], ground[x + 1][y - 1], ground[x - 1][y + 1], ground[x + 1][y + 1]]
        return sum(neighbour)

    def solve(self, x_rect, y_rect, ground):
        tmp = np.zeros([x_rect, y_rect])
        for i in range(1, x_rect - 1):
            for j in range(1, y_rect - 1):
                if ground[i][j] == 1:
                    if self.live_num(ground, i, j) != 2 and self.live_num(ground, i, j) != 3:
                        tmp[i][j] = 0
                    else:
                        pass
                else:
                    if self.live_num(ground, i, j) == 3:
                        tmp[[i][j]] = 1
                    else:
                        pass
        return tmp


if __name__ == '__main__':
    mp = Map(10, 800, 500)
    Logic().solve(mp.x_rect, mp.y_rect, mp.ground)
