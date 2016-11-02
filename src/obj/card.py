from finn.components.Box import Box
import finn.components.text.Text as Text
import finn.Color as Color


class Card(Box):
    def __init__(self, board, ingredient, position):
        color_chart = {"grain": (140, 140, 40),
                       "hops": (10, 160, 30),
                       "yeast": (200, 200, 180)}
        super(Card, self).__init__((position[0], position[1], 150, 200),
                                   box_color=color_chart[ingredient.i_type],
                                   border_color=Color.d_gray,
                                   highlight_color=Color.white,
                                   border=3,
                                   name="{0}_card".format(ingredient.name))
        self.board = board
        self.ingredient = ingredient

    def card_text(self, screen, font, text, y_offset):
        pos = (self.rect.x, self.rect.y)
        Text.draw_text(screen=screen,
                       font=font,
                       text=text,
                       color=Color.white,
                       position=(pos[0]+5, pos[1]+5+y_offset),
                       width=self.rect.width-5,
                       shadow=True)

    def show_card(self, screen):
        # worry about scale later
        fonts = self.board.fonts
        self.card_text(screen, fonts["NORMAL"], self.ingredient.name, y_offset=0)
        self.card_text(screen, fonts["SMALL"], self.ingredient.i_type.upper(), y_offset=60)
        self.card_text(screen, fonts["SMALL"], "${0}/lb".format(self.ingredient.price), y_offset=80)
        if self.ingredient.extra_text:
            offset = 90
            for line in self.ingredient.extra_text:
                offset += 20
                self.card_text(screen, fonts["SMALL"], line, y_offset=offset)

    def draw(self, screen):
        Box.draw(self, screen)
        self.show_card(screen)
