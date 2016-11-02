from ingredient import Ingredient


class Hops(Ingredient):
    def __init__(self, name, price=0, quantity=1, aa=5.0, ba=5.0):
        super(Hops, self).__init__(name, price, i_type="hops", quantity=quantity)
        self.alpha_acid = aa
        self.beta_acid = ba
        self.extra_text = ["Alpha Acid: {0}%".format(self.alpha_acid),
                           "Beta Acid: {0}%".format(self.beta_acid)]
