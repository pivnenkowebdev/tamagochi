import pygame as pg

# Инициализация pg
pg.init()

# Размеры окна
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550

ICON_SIZE = 80
PADDING = 5

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60

font = pg.font.Font(None, 40)



def load_image(file, width, height):
    image = pg.image.load(file).convert_alpha()
    image = pg.transform.scale(image, (width, height))
    return image


def text_render(text):
    return font.render(str(text), True, 'black')


class Button:
    def __init__(self, text, x, y):
        self.idle_image = load_image('image/button.png', BUTTON_WIDTH, BUTTON_HEIGHT)
        self.pressed_image = load_image('image/button_clicked.png', BUTTON_WIDTH, BUTTON_HEIGHT)
        self.image = self.idle_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.text = text_render(text)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

        self.is_pressed = False


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def update(self):
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if self.is_pressed:
                self.image = self.pressed_image
            else:
                self.image = self.idle_image

    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_pressed = True
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.is_pressed = False








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

        button_x = SCREEN_WIDTH - BUTTON_WIDTH - PADDING

        self.eat_button = Button('еда', button_x, PADDING + ICON_SIZE)
        self.clouthes_button = Button('одежда', button_x, PADDING + ICON_SIZE + 70)
        self.games_button = Button('игры', button_x, PADDING + ICON_SIZE + 140)


        self.INCREASE_COINS = pg.USEREVENT + 1
        pg.time.set_timer(self.INCREASE_COINS, 1000)


        self.run()

    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()

    def event(self):


        for event in pg.event.get():

            if event.type == self.INCREASE_COINS:
                self.money += 1

            if event.type == pg.QUIT:
                pg.quit()
                exit()
            self.eat_button.is_clicked(event)
            self.clouthes_button.is_clicked(event)
            self.games_button.is_clicked(event)
    def update(self):
        self.eat_button.update()
        self.clouthes_button.update()
        self.games_button.update()
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

        self.eat_button.draw(self.screen)
        self.clouthes_button.draw(self.screen)
        self.games_button.draw(self.screen)

        pg.display.flip()






if __name__ == "__main__":
    Game()