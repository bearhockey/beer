import finn.Color as Color
from finn.State import State
from finn.components.Ellipse import Ellipse
from finn.Scene import Scene

from src.scenes.main_brew import BrewMan
from src.scenes.game_sidebar import GameSideBar
from src.scenes.main_inventory import Inventory

from src.obj.ingredient import Ingredient
from src.obj.grain import Grain
from src.obj.hops import Hops
from src.obj.yeast import Yeast


class Game(State):
    def __init__(self, board, settings):
        super(Game, self).__init__(board)
        width = settings.screen_size[0]
        height = settings.screen_size[1]
        border = 10
        side_width = 200
        # actual game shit
        self.inventory = []
        self.add_inventory(Ingredient(name="Test", price=50, i_type="fake"))
        self.add_inventory(Grain(name="Chocolate Malt", price=3.65, sg=4.0, srm=12.0))
        self.add_inventory(Hops(name="Cascade", price=40, aa=7.2, ba=13))
        self.add_inventory(Yeast(name="Ale II", price=90, style="ale"))
        self.add_inventory(Grain(name="Debittered Black", price=4.44, sg=2.1, srm=20.1))
        # windows
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
                            "inv": Inventory(self)}
        self.main_window.scene_change(self.main_scenes["brew"])
        self.side_scene = self.side_window.scene_change(GameSideBar(self))
        self.main_scenes["map"].sprites.append(Ellipse(position=(250, 350),
                                                       x_radius=100,
                                                       y_radius=50))

    def add_inventory(self, inv):
        if inv not in self.inventory:
            self.inventory.append(inv)
            print "Added {0} to inv".format(inv.name)
