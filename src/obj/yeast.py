from src.obj.ingredient import Ingredient


class Yeast(Ingredient):
    def __init__(self, name, price=0, quantity=1, style="ale", abv_tol=14.0):
        super(Yeast, self).__init__(name, price, i_type="yeast", quantity=quantity)
        self.style = style
        self.abv_tolerance = abv_tol
        self.extra_text = ["Style: {0}".format(self.style),
                           "ABV Tolerance: {0}".format(self.abv_tolerance)]
