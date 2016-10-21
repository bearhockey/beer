import pygame
import finn.Color as Color
from finn.State import State
from finn.components.Ellipse import Ellipse
from finn.Scene import Scene
from finn.components.Box import Box

from src.scenes.main_brew import BrewMan
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
        self.main_scenes = {"map": Scene(),
                            "brew": BrewMan(self),
                            "inv": Scene()}
        self.main_window.scene_change(self.main_scenes["brew"])
        self.side_scene = self.side_window.scene_change(GameSideBar(self))
        self.main_scenes["map"].sprites.append(Ellipse(position=(250, 350),
                                                       x_radius=100,
                                                       y_radius=50))
        self.main_scenes["inv"].components.append(Box(pygame.Rect(50, 100, 80, 80),
                                                      box_color=Color.blue,
                                                      border_color=Color.d_blue,
                                                      highlight_color=Color.l_gray))
        # actual game shit
        self.inventory = []

    def add_inventory(self, inv):
        if inv not in self.inventory:
            self.inventory.append(inv)
