from finn.Scene import Scene
from src.templates.sidebar_button import SideBarButton


class GameSideBar(Scene):
    def __init__(self, game):
        super(GameSideBar, self).__init__()
        self.board = game.board
        self.main = game.main_window
        self.scenes = game.main_scenes

        self.but_map = self.make_button(50, "map", "Map")
        self.but_brew = self.make_button(100, "brew", "Brew")
        self.but_inventory = self.make_button(150, "inventory", "Inventory")
        self.but_quit = self.make_button(500, "quit", "Quit")

    def make_button(self, y_pos, name, message):
        button = SideBarButton((20, y_pos, 150, 45),
                               name=name,
                               message=message,
                               font=self.board.font)
        self.components.append(button)
        return button

    def update(self, key, mouse, offset=(0, 0)):
        component = self.update_components(key, mouse, offset)
        if component:
            if component.name == "map":
                self.main.scene_change(self.scenes["map"])
            elif component.name == "brew":
                self.main.scene_change(self.scenes["brew"])
            elif component.name == "inventory":
                self.main.scene_change(self.scenes["inv"])
            elif component.name == "quit":
                self.board.set_game_state("quit")
