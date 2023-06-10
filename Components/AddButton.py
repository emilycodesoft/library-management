from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)

# modelos requeridos para este componente: AddButton
from Classes.Libro import Libro

control_map = return_control_reference()


def get_input_data(e):
    libro = Libro()
    for key, value in control_map.items():
        if key == "AddBookForm":
            libro.titulo = value.controls[0].controls[1].controls[0].value
            libro.autor = value.controls[0].controls[1].controls[1].value
            libro.descripcion = value.controls[0].controls[1].controls[2].value
            libro.ctdCopias = value.controls[0].controls[1].controls[3].value
            libro.fechaPublicacion = value.controls[0].controls[1].controls[4].value
            libro.editorial = value.controls[0].controls[1].controls[5].value
            libro.ISBN = value.controls[0].controls[1].controls[6].value

    # validar que se inserten los datos requeridos
    if (
        not (libro.titulo)
        or not (libro.autor)
        or not (libro.ctdCopias)
        or not (libro.fechaPublicacion)
        or not (libro.editorial)
        or not (libro.ISBN)
    ):
        control_map["page"].snack_bar = SnackBar(
            content=Text("Ingrese todos los valores requeridos"),
            action="Aceptar",
        )
        control_map["page"].snack_bar.open = True
        control_map["page"].update()
        return

    libro.agregar()
    control_map["page"].go("/")


# clase principal
class AddButton(UserControl):
    def __init__(self, page=None):
        super().__init__()
        self.page = page

    def add_button_instance(self):
        add_control_reference("AddButton", self)

    def build(self):
        self.add_button_instance()
        return ElevatedButton(
            text="Agregar",
            width=400,
            style=ButtonStyle(padding=20),
            on_click=get_input_data,
        )
