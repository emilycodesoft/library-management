from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)

#  lladamo al store de libros
from Store.BooksStore import BookStore

# modelos requeridos para este componente: AddButton
from Classes.Libro import Libro


control_map = return_control_reference()


def close_dlg(e=None):
    dlg_modal.open = False
    control_map["page"].update()


def delete_book(e):
    libro = Libro()
    libro.eliminar(BookStore["state"]["bookSelected"])
    close_dlg()
    # funcionalidad repetida
    control_map["page"].go("/")
    BookStore["state"]["bookSelected"] = None  # se deselecciona el libro seleccionado


dlg_modal = dlg_modal = AlertDialog(
    modal=True,
    title=Text("Por favor Confima"),
    content=Text("En serio quieres eliminar este libro?"),
    actions=[
        TextButton("Sí", on_click=delete_book),
        TextButton("No", on_click=close_dlg),
    ],
    actions_alignment=MainAxisAlignment.END,
)


def get_input_data(e):
    # llamado a page desde la instancia en los controladores
    control_map["page"].dialog = dlg_modal
    dlg_modal.open = True
    control_map["page"].update()


# clase principal
class DeleteButton(UserControl):
    def __init__(self, page=None):
        super().__init__()
        self.page = page

    def delete_button_instance(self):
        add_control_reference("DeleteButton", self)

    def build(self):
        self.delete_button_instance()
        return ElevatedButton(
            text="Eliminar",
            width=400,
            style=ButtonStyle(padding=20),
            on_click=get_input_data,
        )
