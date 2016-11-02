import finn.Color as Color
from finn.Scene import Scene
from finn.components.text.TextBox import TextBox

from src.scenes.kettle import Kettle


class BrewMan(Scene):
    def __init__(self, game):
        super(BrewMan, self).__init__()
        self.board = game.board
        self.active_grains = []
        self.kettle = TextBox((20, 50, 150, 350),
                              box_color=Color.d_gray,
                              highlight_color=Color.white,
                              active_color=Color.red,
                              name="kettle",
                              message="Brew Kettle",
                              text_color=Color.white,
                              text_outline=Color.black,
                              font=self.board.font,
                              highlight_text=True)
        self.kettle_inside = TextBox((35, 200, 120, 50),
                                     box_color=Color.black,
                                     name="kettle_contents",
                                     message="EMPTY",
                                     text_color=Color.white,
                                     text_outline=Color.black,
                                     font=self.board.fonts["NORMAL"])
        self.grain_calc()
        self.components.append(self.kettle)
        self.sprites.append(self.kettle_inside)
        self.kettle_window = Kettle(self.board, self.kettle)

    def add_grain(self, grain):
        if grain not in self.active_grains:
            self.active_grains.append(grain)
            self.grain_calc()

    def get_inventory(self, type_filter=None):
        item_list = []
        for item in self.board.get_game_state().inventory:
            if type_filter:
                if item.i_type == type_filter:
                    item_list.append(item)
            else:
                item_list.append(item)
        return item_list

    def grain_calc(self):
        if self.active_grains:
            srm = 0.0
            for card in self.active_grains:
                srm += card.srm
            srm *= 1.0/len(self.active_grains)
            color_val = 210 - srm * 10
            box_color = (color_val, color_val, 0)
        else:
            box_color = Color.black
        self.kettle_inside.box_color = box_color

    def update(self, key, mouse, offset=(0, 0)):
        if self.kettle.active:
            card = self.kettle_window.update(key, mouse, offset)
            if card and card.ingredient:
                self.add_grain(card.ingredient)
                self.kettle_window.close_window()

        else:
            component = self.update_components(key, mouse, offset)
            if component:
                if component.name == "kettle":
                    self.kettle_window.open_window(self.get_inventory(type_filter="grain"))

    def draw(self, screen):
        for component in self.components:
            component.draw(screen)
        for sprite in self.sprites:
            sprite.draw(screen)
        if self.kettle.active:
            self.kettle_window.draw(screen)
