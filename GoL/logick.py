import random
import pygame
from konst import *
pygame.init()
screen = pygame.display.set_mode((WIDTH + 100, HEIGHT))
def paint():
    newR = random.randint(0, 255)
    newG = random.randint(0, 255)
    newB = random.randint(0, 255)
    return (newR, newG, newB)


class square:
    def __init__(self, placeX, placeY):
        self.color = WHITE
        self.placeX = placeX
        self.placeY = placeY
        self.life = False
    def alive(self):
        self.life = True
        self.color = BLACK#paint()#BLACK  #ЦВЕТ КВАДРАТОВ (РАЗНЫЙ\ЧЕРНЫЙ)
        return pygame.draw.rect(screen, self.color, [self.placeX * 10 , self.placeY * 10 , RAZMERKLETKA, RAZMERKLETKA])
    def kill(self):
        self.life = False
        self.color = WHITE
        return pygame.draw.rect(screen, self.color, [self.placeX * 10, self.placeY * 10, RAZMERKLETKA, RAZMERKLETKA])
    def info(self):
        return print(self.color, self.life, self.placeX, self.placeY)
    def refresh(self, bull):
        if bull:
            self.alive()
        if not bull:
            self.kill()

def startLifeMap(razmerH, razmerW):
    lifeMap = []
    for y in range(WIDTH_M):
        for x in range(HEIGHT_M):
            lifeMap.append([x, y, square(x, y)])
    return lifeMap

def setka(screen):
    for x in range(0, WIDTH, RAZMERKLETKA ):
        pygame.draw.line(screen, GREY, [x, 0], [x, HEIGHT])
    for y in range(0, HEIGHT, RAZMERKLETKA):
        pygame.draw.line(screen, GREY, [0, y], [WIDTH, y])

def perevodBigInSmall(mesto):
    koordinaty = (mesto[0] // 10, mesto[1] // 10)
    return koordinaty

def gameOfLife(lifeMap):
    spisokLife = []
    for i in range(HEIGHT_M * WIDTH_M):
        spisokLife.append(0)
    for i in range(HEIGHT_M * WIDTH_M):
        spisokLife[i] = lifeMap[i][2].life
    for y in range(HEIGHT_M):
        for x in range(WIDTH_M):
            count = 0
            for j in range(y - 1, y + 2):               # смотрим от предыдущих координат до следующих и ставим +2, ибо
                for i in range(x - 1, x + 2):           # рэндж заканчивает перед точкой остановки(стоп)
                    if j < 0:
                        j += HEIGHT_M
                    if j >= HEIGHT_M:
                        j -= HEIGHT_M
                    if i < 0:
                        i += WIDTH_M
                    if i >= WIDTH_M:
                        i -= WIDTH_M

                    if lifeMap[j * HEIGHT_M + i][2].life:
                        count += 1


            if lifeMap[y * HEIGHT_M + x][2].life:
                count -= 1
            if not lifeMap[y * HEIGHT_M + x][2].life and count == 3:
                spisokLife[y * HEIGHT_M + x] = True
            if lifeMap[y * HEIGHT_M + x][2].life and (count < 2 or count > 3):
                spisokLife[y * HEIGHT_M + x] = False
            if lifeMap[y * HEIGHT_M + x][2].life and (count == 2 or count == 3):
                spisokLife[y * HEIGHT_M + x] = True
    for i in range(len(spisokLife)):
        if spisokLife[i]:
            if  not lifeMap[i][2].life:
                lifeMap[i][2].alive()
        if not spisokLife[i]:
            lifeMap[i][2].kill()



def proverka(lifeMap, event):
    for y in range(HEIGHT_M):
        for x in range(WIDTH_M):
            if (lifeMap[y * HEIGHT_M + x][0], lifeMap[y * HEIGHT_M + x][1]) == perevodBigInSmall(event.pos):
                print("popal")
                print(lifeMap[y * HEIGHT_M + x][2].info())
                print(lifeMap[y * HEIGHT_M + x][0], lifeMap[y * HEIGHT_M + x][1])
                lifeMap[y * HEIGHT_M + x - HEIGHT_M - 1][2].alive()

def randomLifeMap(lifeMap):
    for i in range(HEIGHT_M * WIDTH_M):
        lifeMap[i][2].refresh(random.randint(0, 1))
    return lifeMap

def killLifeMap(lifeMap):
    for i in range(HEIGHT_M * WIDTH_M):
        lifeMap[i][2].kill()
    return lifeMap

