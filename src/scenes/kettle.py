from finn.components.Box import Box
from finn.Scene import Scene
from src.obj.close_button import CloseButton
import finn.Color as Color


class Kettle(Scene):
    def __init__(self, board, parent_component):
        super(Kettle, self).__init__()
        self.board = board
        self.parent = parent_component
        self.box = Box((40, 300, 800, 250),
                       box_color=Color.l_blue,
                       border_color=Color.white,
                       highlight_box=False,
                       name="kettle_window")
        self.close = CloseButton(position=(self.box.rect.right-35, self.box.rect.top+3))

    def close_window(self):
        del self.components[:]
        self.parent.active = False

    def open_window(self, grain_inventory):
        self.components.append(self.close)
        if grain_inventory:
            x_offset = 50
            for grain in grain_inventory:
                self.components.append(grain.make_card(self.board, position=(x_offset, 310)))
                x_offset += 200

    def update(self, key, mouse, offset=(0, 0)):
        component = self.update_components(key, mouse, offset)
        if component:
            if component.name == "close":
                self.close_window()
            else:
                return component

    def draw(self, screen):
        self.box.draw(screen)
        self.draw_all(screen)
