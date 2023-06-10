from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)

control_map = return_control_reference()


# clase principal
class AppNavbar(UserControl):
    def __init__(self, page=None):
        super().__init__()
        self.page = page

    def app_navbar_instance(self):
        add_control_reference("AppNavBar", self)

    def app_button(self, text: str):
        return ElevatedButton(text=text)

    def build(self):
        self.app_navbar_instance()

        return Row(controls=[self.app_button("Mostrar Libros")])
