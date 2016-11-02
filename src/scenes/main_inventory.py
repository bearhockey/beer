from finn.Scene import Scene


class Inventory(Scene):
    def __init__(self, game):
        super(Inventory, self).__init__()
        self.board = game.board
        self.inventory = game.inventory

    def draw(self, screen):
        self.draw_all(screen)
        x = 50
        for card in self.inventory:
            card.show_card(screen, self.board.fonts, pos=(x, 100))
            x += 200

