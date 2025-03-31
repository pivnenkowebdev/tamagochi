import pygame as pg

# Инициализация pg
pg.init()

# Размеры окна
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550

ICON_SIZE = 80
PADDING = 5




def load_image(file, width, height):
    image = pg.image.load(file).convert_alpha()
    image = pg.transform.scale(image, (width, height))
    return image


class Game:
    def __init__(self):

        # Создание окна
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")


        self.happiness = 100
        self.satiety = 100
        self.health = 100


        self.background = load_image('image/background.png', SCREEN_WIDTH, SCREEN_HEIGHT)
        self.happiness = load_image('image/happiness.png', ICON_SIZE, ICON_SIZE)
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

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.happiness, (PADDING, PADDING))

        pg.display.flip()




if __name__ == "__main__":
    Game()