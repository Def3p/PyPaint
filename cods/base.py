import pygame
from pygame import *


def whiler(screen):

    clock = pygame.time.Clock()
    run = True
    
    # крестики (закрытие)
    but_x1 = pygame.image.load('images/sistem/X1.png')
    but_x2 = pygame.image.load('images/sistem/X2.png')
    bx = False
    # минусы (свернуть)
    but_a1 = pygame.image.load('images/sistem/_1.png')
    but_a2 = pygame.image.load('images/sistem/_2.png')
    ba = False
    # настройки
    but_set1 = pygame.image.load('images/sistem/options1.png')
    but_set2 = pygame.image.load('images/sistem/options2.png')
    but_set_bg = pygame.image.load('images/sistem/bg_options.png')
    but_set_bg = transform.scale(but_set_bg, (130, 38))
    bs = False

    screen.fill((25, 23, 61)) # заливка фона

    while run:
        pygame.draw.rect(screen, (225, 23, 69) , (0, 0, 650, 44) ) # красный прямоугольник

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False # выход
            elif event.type == MOUSEMOTION: # если мышка двигается:
                if 549 > event.pos[0] > 519 and 37 > event.pos[1] > 7:
                    ba = True
                else: ba = False
                if 609 > event.pos[0] > 549 and 37 > event.pos[1] > 7:
                    bs = True
                else: bs = False
                if 639 > event.pos[0] > 609 and 37 > event.pos[1] > 7:
                    bx = True
                else: bx = False
            elif event.type == MOUSEBUTTONDOWN: # если мышка нажата:
                if 549 > event.pos[0] > 519 and 37 > event.pos[1] > 7:
                    pygame.display.iconify()
                elif 639 > event.pos[0] > 609 and 37 > event.pos[1] > 7:
                    run = False # выход
        
        screen.blit(but_set_bg, (514, 3)) # фон для кнопок
        if ba == False:
            screen.blit(but_a1, (519, 7)) # свернуть (не наведено)
        elif ba == True:
            screen.blit(but_a2, (519, 7)) # свернуть (наведено)
        if bs == False:
            screen.blit(but_set1, (549, 7))# опции (не наведено)
        elif bs == True:
            screen.blit(but_set2, (549, 7))# опции (наведено)
        if bx == False:
            screen.blit(but_x1, (609, 7))# крест (не наведено)
        elif bx == True:
            screen.blit(but_x2, (609, 7)) # крест (наведено)

        clock.tick(200) # FPS
        pygame.display.flip() # update
    quit() # выход