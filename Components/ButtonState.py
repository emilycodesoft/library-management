from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)

# modelos requeridos para este componente: AddButton
from Classes.Libro import Libro

control_map = return_control_reference()


def get_input_data(state):
    state.get_input_data()


# clase principal
class AppButton(UserControl):
    _state = None

    def __init__(self, page=None, text=""):
        super().__init__()
        self.page = page
        self.text = text

    def app_button_instance(self):
        add_control_reference("AppButton", self)

    def build(self):
        self.app_button_instance()
        return ElevatedButton(
            text=self.text,
            width=400,
            style=ButtonStyle(padding=20),
            on_click=lambda _: get_input_data(self._state),
        )
