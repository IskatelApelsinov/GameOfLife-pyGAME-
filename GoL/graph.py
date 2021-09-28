from logick import *


pygame.display.set_caption("Game of life")
clock = pygame.time.Clock()
lifeMap = startLifeMap(HEIGHT_M, WIDTH_M)
screen.fill(WHITE)
pygame.draw.line(screen, GREEN, [660, 70], [660, 80], 2)
pygame.draw.circle(screen, RED, (661, 105), 6, 2)
pygame.draw.aalines(screen, BLUE, False, [[657, 35], [663, 30], [663, 40]])
pygame.draw.aalines(screen, BLACK, False, [[658, 160], [658, 150], [663, 150], [663, 155], [658, 155], [663, 160]])
pygame.draw.circle(screen, BLACK, (660, 175), 6, 1)
pygame.draw.line(screen, BLACK, [655, 180], [665, 170], 3)
pygame.draw.line(screen, BLACK, [601, 0], [601, HEIGHT])   # Граница
pygame.draw.rect(screen, BLACK, [640, 30, RAZMERKLETKA, RAZMERKLETKA])  # Один круг
pygame.draw.rect(screen, BLACK, [640, 70, RAZMERKLETKA, RAZMERKLETKA])  # Вкл игру
pygame.draw.rect(screen, BLACK, [640, 100, RAZMERKLETKA, RAZMERKLETKA]) # Выкл игру
pygame.draw.rect(screen, BLACK, [640, 150, RAZMERKLETKA, RAZMERKLETKA]) # Рандомное поле
pygame.draw.rect(screen, BLACK, [640, 170, RAZMERKLETKA, RAZMERKLETKA]) # Очистить поле

arbeiten = True
lkm = False
pkm = False
start = False
mousePosition = (0, 0)
while arbeiten:
    button = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            arbeiten = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = perevodBigInSmall(event.pos)
            if mousePosition == (64, 3):
                button = 1
            if mousePosition == (64, 7):
                button = 2
            if mousePosition == (64, 10):
                button = 3
            if mousePosition == (64, 15):
                button = 4
            if mousePosition == (64, 17):
                button = 5
            if event.button == 1:
                lkm = True
                pkm = False
            if event.button == 3:
                lkm = False
                pkm = True
    if start:
        gameOfLife(lifeMap)
    for i in lifeMap:
        if (i[0], i[1]) == mousePosition:
            i[2].refresh(lkm)
    if button == 1:
        gameOfLife(lifeMap)
    elif button == 2:
        start = True
    elif button == 3:
        start = False
    elif button == 4:
        randomLifeMap(lifeMap)
    elif button == 5:
        killLifeMap(lifeMap)

    setka(screen)   # CЕТКА НА ЭКРАНЕ
    pygame.display.flip()
    #pygame.display.update()
    clock.tick(FPS)
pygame.quit()