from finn.components.Box import Box
import finn.Color as Color
import finn.components.text.Text as Text


class Ingredient(object):
    def __init__(self, name, price=0, i_type=None, quantity=1):
        self.name = name
        self.price = price
        self.i_type = i_type
        self.quantity = quantity
        # worry about scale later
        self.card = Box((0, 0, 100, 150),
                        box_color=Color.white,
                        border_color=Color.white,
                        border=4,
                        name="{0}_card".format(self.name))

    def add(self, number):
        self.quantity += number

    def show_card(self, screen, pos, parms={}):
        color_chart = {"grain": Color.yellow,
                       "hops": Color.green}
        # worry about scale later
        self.card.move_rect(x=pos[0], y=pos[1])
        self.card.box_color = color_chart[self.i_type]
        self.card.draw(screen)
        Text.draw_text()
