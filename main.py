import pygame as pg

# Инициализация pg
pg.init()

# Размеры окна
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550


class Game:
    def __init__(self):

        # Создание окна
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")

        self.run()

    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    def update(self):
        ...

    def draw(self):
        pg.display.flip()


if __name__ == "__main__":
    Game()