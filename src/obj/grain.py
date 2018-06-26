from src.obj.ingredient import Ingredient


class Grain(Ingredient):
    def __init__(self, name, price=0, quantity=1, grain="barley", sg=1.0, srm=1):
        super(Grain, self).__init__(name, price, i_type="grain", quantity=quantity)
        self.grain = grain
        self.sg = sg
        self.srm = srm
        self.extra_text = ["Grain: {0}".format(self.grain),
                           "SG: {0}".format(self.sg),
                           "SRM: {0}".format(self.srm)]
