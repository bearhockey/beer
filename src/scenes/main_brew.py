import finn.Color as Color
from finn.Scene import Scene
from finn.components.text.TextBox import TextBox
from finn.components.Box import Box


class BrewMan(Scene):
    def __init__(self, game):
        super(BrewMan, self).__init__()
        self.board = game.board
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
        self.components.append(self.kettle)
        self.kettle_window = Scene()
        box = Box((40, 300, 800, 250),
                  box_color=Color.l_blue,
                  border_color=Color.white,
                  highlight_box=False,
                  name="kettle_window")
        self.kettle_window.sprites.append(box)

    def update(self, key, mouse, offset=(0, 0)):
        component = self.update_components(key, mouse, offset)
        if self.kettle.active:
            self.kettle_window.update(key, mouse, offset)

    def draw(self, screen):
        for component in self.components:
            component.draw(screen)
        for sprite in self.sprites:
            sprite.draw(screen)
        if self.kettle.active:
            self.kettle_window.draw(screen)
