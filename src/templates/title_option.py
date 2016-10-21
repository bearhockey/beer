import finn.Color as Color
from finn.components.text.TextBox import TextBox


class TitleOption(TextBox):
    def __init__(self, rect, name, message, font):
        super(TitleOption, self).__init__(rect=rect,
                                          highlight_color=Color.gray,
                                          active_color=Color.blue,
                                          name=name,
                                          message=message,
                                          text_color=Color.white,
                                          text_outline=True,
                                          font=font,
                                          highlight_text=True,
                                          highlight_box=False)
