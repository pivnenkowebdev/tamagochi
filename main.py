import pygame as pg

# Инициализация pg
pg.init()

# Размеры окна
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550

DOG_WIDTH = 310
DOG_HEIGHT = 500

DOG_Y = 100

ICON_SIZE = 80
PADDING = 5

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60

MENU_NAV_XPAD = 90
MENU_NAV_YPAD = 130


font = pg.font.Font(None, 40)
mini_font = pg.font.Font(None, 20)

class Item:
  def __init__(self, name, price, file):
    self.name = name
    self.price = price
    self.is_bought = False
    self.is_using = False
    self.image = load_image(file, DOG_WIDTH // 1.7, DOG_HEIGHT // 1.7)


class ClothesMenu:
    def __init__(self, game):
        self.game = game
        self.menu_page = load_image("images/menu/menu_page.png", SCREEN_WIDTH, SCREEN_HEIGHT)

        self.bottom_label_off = load_image("images/menu/bottom_label_off.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        self.bottom_label_on = load_image("images/menu/bottom_label_on.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        self.top_label_off = load_image("images/menu/top_label_off.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        self.top_label_on = load_image("images/menu/top_label_on.png", SCREEN_WIDTH, SCREEN_HEIGHT)

        self.items = [Item("Синяя футболка", 10, "images/items/blue t-shirt.png"),
                      Item("Ботинки", 50, "images/items/boots.png"),
                      Item("Шляпа", 50, "images/items/hat.png")]

        self.current_item = 0

        self.item_rect = self.items[0].image.get_rect()
        self.item_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.next_button = Button("Вперёд", SCREEN_WIDTH - MENU_NAV_XPAD - BUTTON_WIDTH, SCREEN_HEIGHT - MENU_NAV_YPAD,
                                   width=int(BUTTON_WIDTH // 1.2), height=int(BUTTON_HEIGHT // 1.2),
                                   func=self.to_next)


    def to_next(self):
        if self. current_item != len(self.items) - 1:
            self.current_item += 1

    def update(self):
        self.next_button.update()

    def is_clicked(self, event):
        self.next_button.is_clicked(event)


    def draw(self, screen):
        screen.blit(self.menu_page, (0, 0))

        screen.blit(self.items[self.current_item], self.item_rect)

        if self.items[self.current_item].is_bought:
            screen.blit(self. bottom_label_on, (0, 0))
        else:
            screen.blit(self.bottom_label_off, (0, 0))

        if self.items[self.current_item].is_using:
            screen.blit(self. top_label_on, (0, 0))
        else:
            screen.blit(self.bottom_label_off, (0, 0))

        self.next_button.draw(screen)

def load_image(file, width, height):
    image = pg.image.load(file).convert_alpha()
    image = pg.transform.scale(image, (width, height))
    return image


def text_render(text):
    return font.render(str(text), True, 'black')


class Button:
    def __init__(self, text, x, y, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text_font=font, func=None):
        self.func = func
        self.idle_image = load_image('image/button.png', width, height)
        self.pressed_image = load_image('image/button_clicked.png', width, height)
        self.image = self.idle_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.text_font = text_font
        self.text = self.text_font.render(str(text), True, 'black')
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
                self.func()
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
        self.coins_per_second = 1
        self.costs_of_upgrade = {100: False, 1000: False, 5000: False, 10000: False}

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

        self.upgrade = Button('Улучшить', SCREEN_WIDTH - ICON_SIZE, 0,
                       width=BUTTON_WIDTH // 3, height=BUTTON_HEIGHT // 3,
                              text_font=mini_font,func=self.increase_money)

        self.INCREASE_COINS = pg.USEREVENT + 1
        pg.time.set_timer(self.INCREASE_COINS, 1000)

        self.run()

    def increase_money(self):
        for cost, check in self.costs_of_upgrade.items():
            if not check and self.money >= cost:
                self.coins_per_second += 1
                self.money -= cost
                self.costs_of_upgrade[cost] = True
                break

    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pg.event.get():

            if event.type == self.INCREASE_COINS:
                self.money += self.coins_per_second

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.money += self.coins_per_second


            if event.type == pg.QUIT:
                pg.quit()
                exit()

            self.eat_button.is_clicked(event)
            self.clouthes_button.is_clicked(event)
            self.games_button.is_clicked(event)
            self.upgrade.is_clicked(event)
    def update(self):
        self.eat_button.update()
        self.clouthes_button.update()
        self.games_button.update()
        self.upgrade.update()
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
        self.upgrade.draw(self.screen)

        pg.display.flip()

if __name__ == "__main__":
    Game()


