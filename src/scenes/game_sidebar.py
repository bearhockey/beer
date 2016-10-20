from finn.Scene import Scene
from src.templates.sidebar_button import SideBarButton


class GameSideBar(Scene):
    def __init__(self, board):
        super(GameSideBar, self).__init__()
        self.board = board
        self.but_map = SideBarButton((20, 50, 150, 45),
                                     name="map",
                                     message="Map",
                                     font=board.font)
        self.components.append(self.but_map)
        self.but_inventory = SideBarButton((20, 100, 150, 45),
                                           name="inventory",
                                           message="Inventory",
                                           font=board.font)
        self.components.append(self.but_inventory)
        self.but_quit = SideBarButton((20, 500, 150, 45),
                                      name="quit",
                                      message="Quit",
                                      font=board.font)
        self.components.append(self.but_quit)

    def update(self, key, mouse, offset=(0, 0)):
        component = self.update_components(key, mouse, offset)
        if component and component.name == "quit":
            print "FUCK"
