from ingredient import Ingredient


class Grain(Ingredient):
    def __init__(self, name, price=0, quantity=1):
        super(Grain, self).__init__(name, price, i_type="grain", quantity=quantity)
