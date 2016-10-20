import pygame

import finn.Color as Color
from finn.State import State
from finn.components.Box import Box
from templates.title_option import TitleOption


class Title(State):
    def __init__(self, board, image=None, music=None):
        super(Title, self).__init__(board)
        self.screen_size = board.screen_size
        self.font = board.font
        self.title_image = None
        if image:
            self.add_title(pygame.image.load(image))
        if music:
            pygame.mixer.music.load(music)

        x_mid = self.screen_size[0]/2
        y_mid = self.screen_size[1]/2

        self.new_game = TitleOption(rect=(x_mid-40, y_mid+20, 120, 30),
                                    name="new",
                                    message="New Game",
                                    font=self.font)
        self.load_game = TitleOption(rect=(x_mid-40, y_mid+60, 120, 30),
                                     name="load",
                                     message="Load Game",
                                     font=self.font)
        self.options = TitleOption(rect=(x_mid-40, y_mid+100, 100, 30),
                                   name="options",
                                   message="Options",
                                   font=self.font)
        self.quit = TitleOption(rect=(x_mid-40, y_mid+140, 80, 30),
                                name="quit",
                                message='Quit',
                                font=self.font)
        self.buttons = [self.new_game, self.load_game, self.options, self.quit]

    @staticmethod
    def play_title_music():
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

    @staticmethod
    def stop_title_music():
        pygame.mixer.music.fadeout(500)

    def add_title(self, title_image):
        self.title_image = Box(rect=pygame.Rect(10, 10, self.screen_size[0]-20, self.screen_size[1]-20),
                               border_color=Color.white,
                               highlight_color=Color.white,
                               active_color=Color.white,
                               border=4,
                               image=title_image)

    def update(self, key, mouse):
        name = None
        for button in self.buttons:
            if button.update(key=key, mouse=mouse):
                name = button.name
        if name == "new":
            self.board.set_game_state("start")
        if name == "quit":
            self.board.set_game_state("quit")

    def draw(self, screen):
        if self.title_image:
            self.title_image.draw(screen)
        self.new_game.draw(screen)
        self.load_game.draw(screen)
        self.options.draw(screen)
        self.quit.draw(screen)
