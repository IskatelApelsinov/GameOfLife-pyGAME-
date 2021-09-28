WIDTH = 600     #   Ширина поля
HEIGHT = 600        # Высота поля
RAZMERKLETKA = 10
FPS = 30         # Кадры в секунду
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (190, 190, 190)
KREM = (255, 249, 140)
WIDTH_M = int(WIDTH / RAZMERKLETKA)
HEIGHT_M = int(HEIGHT / RAZMERKLETKA)


'''
for event in pygame.event.get():
    if start:
        gameOfLife(lifeMap)
    if event.type == pygame.QUIT:
        arbeiten = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            # proverka(lifeMap, event)
            if perevodBigInSmall(event.pos) == (64, 7):
                start = True
            if perevodBigInSmall(event.pos) == (64, 10):
                start = False
            if perevodBigInSmall(event.pos) == (64, 15):
                randomLifeMap(lifeMap)
            if perevodBigInSmall(event.pos) == (64, 3):
                gameOfLife(lifeMap)
            for i in lifeMap:
                if (i[0], i[1]) == perevodBigInSmall(event.pos):
                    i[2].alive()
        elif event.button == 3:
            for i in lifeMap:
                if (i[0], i[1]) == perevodBigInSmall(event.pos):
                    i[2].kill()
                    
                    
|||||||||||||||||||||||||||||||||||||||||||||||||||||
    for y in range(HEIGHT_M):
        for x in range(WIDTH_M):
            count = 0
            for j in range(y - 1 - 1, y + 1):
                for i in range(x - 1 - 1, x + 1):
                    if lifeMap[j * HEIGHT_M + i][2].life:
                        count += 1
            if lifeMap[y * HEIGHT_M + x][2].life:
                count -= 1
            if not lifeMap[y * HEIGHT_M + x][2].life and count == 3:
                spisokLife[y * HEIGHT_M + x - HEIGHT_M - 1] = True
            if lifeMap[y * HEIGHT_M + x][2].life and (count < 2):
                spisokLife[y * HEIGHT_M + x - HEIGHT_M - 1] = False
            if lifeMap[y * HEIGHT_M + x][2].life and (count == 2 or count == 3):
                spisokLife[y * HEIGHT_M + x - HEIGHT_M - 1] = True
            if lifeMap[y * HEIGHT_M + x][2].life and (count > 3):
                spisokLife[y * HEIGHT_M + x - HEIGHT_M - 1] = False
    for i in range(len(spisokLife)):
        if spisokLife[i]:
            lifeMap[i][2].alive()
        if not spisokLife[i]:
            lifeMap[i][2].kill()
'''