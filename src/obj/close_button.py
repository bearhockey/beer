from finn.components.Box import Box
import finn.Color as Color


class CloseButton(Box):
    def __init__(self, position, width=32):
        super(CloseButton, self).__init__(rect=(position[0], position[1], width, width),
                                          box_color=Color.d_gray,
                                          border_color=Color.l_gray,
                                          highlight_color=Color.white,
                                          border=3,
                                          name="close")
