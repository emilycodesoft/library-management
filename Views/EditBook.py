from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)

# componentes requeridos para esta vista: EditBook
from Components.EditBookForm import EditBookForm

control_map = return_control_reference()


# clase principal
class EditBookView(UserControl):
    def __init__(self, page=None):
        super().__init__()
        self.page = page

    # añadimos vista al controlador
    def edit_book_view_instance(self):
        add_control_reference("EditBookView", self)

    def build(self):
        self.edit_book_view_instance()
        editBookForm = EditBookForm(self.page)

        return Column(
            controls=[
                ElevatedButton("Volver", on_click=lambda _: self.page.go("/")),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[editBookForm],
                ),
            ]
        )
