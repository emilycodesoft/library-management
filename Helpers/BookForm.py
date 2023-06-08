from flet import *

# this class will generate a new instance of text and insert it into the BookTable


class BookFormHelper(UserControl):
    def __init__(self, user_input):
        self.user_input = user_input
        super().__init__()

    def build(self):
        return TextField(
            value=self.user_input, border_color="transparent", read_only=True
        )  # we pass the form fields values into here
