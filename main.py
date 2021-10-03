import pygame
import time
from format_time import format_hour
import datetime

pygame.init()


def create_grid() -> dict:
    grid = {(i, j): (50, 50, 50) for j in range(12) for i in range(12)}
    for i in range(0, 7):
        grid[(i, 10)] = (255, 255, 255)
        
    for i in range(0, 12):
        grid[(i, 11)] = (255, 255, 255)
    return grid


def day_month_pos() -> dict:
    pos = {}
    for i in range(7):
        pos[i] = (i, 10)

    for i in range(1, 13):
        pos[f"{i:02d}"] = (i-1, 11)
    return pos


def position_col() -> dict:
    pos = {"IL": (0, 1, 0), "EST": (3, 5, 0), "UNE": (9, 11, 0), "MINUIT": (0, 5, 1), "DEUX": (7, 10, 1),
           "TROIS": (0, 4, 2), "QUATRE": (6, 11, 2), "CINQ": (0, 3, 3), "SIX": (5, 7, 3),
           "SEPT": (8, 11, 3), "HUIT": (0, 3, 4), "NEUF": (5, 8, 4), "DIX": (9, 11, 4),
           "ONZE": (3, 6, 5), "MIDI": (8, 11, 5), "HEURE": (0, 4, 6), "HEURES": (0, 5, 6),
           "MOINS": (7, 11, 6), "LE": (0, 1, 7), "VINGT": (2, 6, 7), "CINQ2": (8, 11, 7),
           "ET": (0, 1, 8), "QUART": (3, 7, 8), "DIX2": (9, 11, 8), "DEMIE": (4, 8, 9)}

    for key, val in pos.items():
        pos[key] = [(i, val[2])for i in range(val[0], val[1]+1)]
    return pos


def draw_letters(screen: pygame.Surface, grid: dict):
    letters = ["ILKESTPNMUNE",
               "MINUITFDEUXZ",
               "TROISZQUATRE",
               "CINQGSIXSEPT",
               "HUITYNEUFDIX",
               "ERTONZEJMIDI",
               "HEURESWMOINS",
               "LEVINGTGCINQ",
               "ETMQUARTJDIX",
               "HSCXDEMIEDFR",
               "LMMJVSDOGVEL",
               "JFMAMJJASOND"]

    font = pygame.font.SysFont('arial', 30)
    for i, line in enumerate(letters):
        for j, case in enumerate(line):
            letter = font.render(case, False, grid[(j, i)])
            posX = 20 - letter.get_width()//2
            posY = 20 - letter.get_height()//2
            screen.blit(letter, (j*40 + posX, i*40+posY))


def main(screen: pygame.Surface):
    running = True
    color = position_col()

    while running:
        grid = create_grid()
        day_month = day_month_pos()

        day = datetime.datetime.now().weekday()
        month = time.strftime("%m")
        hour = tuple(map(int, time.strftime("%H %M").split()))

        grid[day_month[day]] = (0, 255, 0)
        grid[day_month[month]] = (255, 0, 0)
        for i in format_hour(hour[0], hour[1]).split():
            for j in color[i]:
                grid[j] = (255, 255, 255)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        draw_letters(screen, grid)
        pygame.display.flip()
        pygame.time.wait(100)


if __name__ == '__main__':
    win = pygame.display.set_mode((480, 480))
    main(win)
    pygame.quit()
