import pygame as pg

# Инициализация pg
pg.init()

# Размеры окна
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550

ICON_SIZE = 80
PADDING = 5

font = pg.font.Font(None, 40)



def load_image(file, width, height):
    image = pg.image.load(file).convert_alpha()
    image = pg.transform.scale(image, (width, height))
    return image


def text_render(text):
    return font.render(str(text), True, 'blue')

class Game:
    def __init__(self):

        # Создание окна
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")

        self.money = 10
        self.happiness = 100
        self.satiety = 100
        self.health = 100


        self.background = load_image('image/background.png', SCREEN_WIDTH, SCREEN_HEIGHT)
        self.happiness_image = load_image('image/happiness.png', ICON_SIZE, ICON_SIZE)
        self.satiety_image = load_image('image/satiety.png', ICON_SIZE, ICON_SIZE)
        self.health_image = load_image('image/health.png', ICON_SIZE, ICON_SIZE)
        self.money_image = load_image('image/money.png', ICON_SIZE, ICON_SIZE)
        self.pet_image = load_image('image/dog.png', 310, 500)
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
        self.screen.blit(self.happiness_image, (PADDING, PADDING))
        self.screen.blit(text_render(self.happiness), (PADDING + ICON_SIZE, PADDING * 6))

        self.screen.blit(self.satiety_image, (PADDING, PADDING + 60))
        self.screen.blit(text_render(self.satiety), (PADDING + ICON_SIZE, PADDING * 18))

        self.screen.blit(self.health_image, (PADDING, PADDING + 120))
        self.screen.blit(text_render(self.health), (PADDING + ICON_SIZE, PADDING * 30))

        self.screen.blit(self.money_image, (815, 5))
        self.screen.blit(text_render(self.money), (715 + ICON_SIZE, PADDING * 6))

        self.screen.blit(self.pet_image,(285, 100))

        pg.display.flip()






if __name__ == "__main__":
    Game()