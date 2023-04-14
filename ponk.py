import pygame as pg
import sys


class Paddle:
    def __init__(self, x):
        self.image = pg.Surface((20, 70))  # изображение из поверхности
        self.image.fill(())
        self.rect = self.image.get_rect()  # прямоугольник из изображениыя
        self.rect.x = x
        self.rect.y = 300  # TODO: поместить ракетку посерелине высоты
        self.color = (225, 225, 225)


class Ball:
    pass


class Score:
    pass


class Game:
    def __init__(self):
        self.SCREEN_COLOR = (0, 0, 0)
        self.player_1 = Paddle(100)
        self.player_2 = Paddle(700)

    def run(self):
        pg.init()
        screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Понг")
        while True:  # главный цикл программы

            # работа с событиями
            for event in pg.event.get():  # идём по всем событиям
                if event.type == pg.QUIT:  # ловим событие выхода
                    pg.quit()  # выгружает модули из памяти
                    sys.exit()  # закрывает окно

                if event.type == pg.KEYDOWN:  # ловим нажатия клавиш
                    if event.key == pg.K_ESCAPE:  # нажат Esc
                        pg.quit()
                        sys.exit()

            # отрисовка(reder)
            screen.fill(self.SCREEN_COLOR)  # заливаем весь экран
            pg.display.flip()