from src.obj.card import Card


class Ingredient(object):
    def __init__(self, name, price=0, i_type=None, quantity=1):
        self.name = name
        self.price = price
        self.i_type = i_type
        self.quantity = quantity
        self.extra_text = []

    def add(self, number):
        self.quantity += number

    def make_card(self, board, position=(0, 0)):
        return Card(board, self, position)
