import finn.Color as Color
from finn.State import State
from finn.components.Ellipse import Ellipse

from src.scenes.game_sidebar import GameSideBar


class Game(State):
    def __init__(self, board, settings):
        super(Game, self).__init__(board)
        width = settings.screen_size[0]
        height = settings.screen_size[1]
        border = 10
        side_width = 200
        self.main_window = self.add_window(name="main",
                                           properties={"position": (border, border),
                                                       "size": (width-side_width-border*3, height-(border*2)),
                                                       "name": "main",
                                                       "border_color": Color.white})
        self.side_window = self.add_window(name="side",
                                           properties={"position": (border*2+(width-side_width-border*3), border),
                                                       "size": (side_width, height-(border*2)),
                                                       "name": "side",
                                                       "border_color": Color.white})
        self.scene_one = self.main_window.create_scene()
        self.side_scene = self.side_window.scene_change(GameSideBar(board))
        self.main_window.add_sprite_to_scene(Ellipse(position=(250, 350),
                                                     x_radius=100,
                                                     y_radius=50))
