from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)

control_map = return_control_reference()


# clase principal
class SearchInput(UserControl):
    def __init__(self, page=None):
        super().__init__()
        self.page = page

    def search_input_instance(self):
        add_control_reference("SearchInput", self)

    def textbox_changed(e):
        pass

    def build(self):
        self.search_input_instance()

        return TextField(label="Buscar Libro", on_change=self.textbox_changed)
