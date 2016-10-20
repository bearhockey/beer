import settings
from finn.Board import Board
from src.Game import Game
from src.Title import Title

settings.init()
s_size = settings.screen_size

game = Board(screen_size=s_size, font_path=settings.font_path)

game.add_game_state("title", Title(board=game))
game.add_game_state("start", Game(board=game, settings=settings))

# start game things
game.set_game_state("title")

game.run_main_loop()
