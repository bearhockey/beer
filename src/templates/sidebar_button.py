import pygame
import finn.Color as Color
from finn.components.text.TextBox import TextBox


class SideBarButton(TextBox):
    def __init__(self, rect, name, message, font):
        super(SideBarButton, self).__init__(rect=pygame.Rect(rect),
                                            box_color=Color.d_gray,
                                            border_color=None,
                                            highlight_color=Color.white,
                                            active_color=None,
                                            name=name,
                                            message=message,
                                            text_color=Color.white,
                                            text_outline=True,
                                            font=font)
