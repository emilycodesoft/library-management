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

    def filter_books_table(self, e):
        for key, value in control_map.items():
            if key == "BooksTable":
                if (len(value.controls[0].controls[0].rows)) != 0:
                    for data in value.controls[0].controls[0].rows[:]:
                        if e.data.lower() in data.cells[1].content.value.lower():
                            data.visible = True
                            data.update()
                        else:
                            data.visible = False
                            data.update()

    def build(self):
        self.search_input_instance()

        return TextField(label="Buscar Libro", on_change=self.filter_books_table)
