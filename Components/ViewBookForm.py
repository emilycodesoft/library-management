from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)

# modelos requeridos para este componente: ViewBookForm
from Classes.Libro import Libro

# componentes requeridos para este componente: EditBookForm
from Components.ViewButton import ViewButton

# stores requeridas para este componente: ViewBookForm
from Store.BooksStore import BookStore

control_map = return_control_reference()


# clase principal
class ViewBookForm(UserControl):
    def __init__(self, page=None):
        super().__init__()
        self.page = page

    def view_book_form_instance(self):
        add_control_reference("ViewBookForm", self)

    # header del formulario
    def form_header(self):
        return Container(
            content=Text("Ver Libro", style=TextThemeStyle.TITLE_LARGE),
            margin=margin.only(bottom=20),
        )

    # campo de texto del formulario
    def input_form_field(self, label: str, multiline=False, value=""):
        return TextField(label=label, multiline=multiline, value=value)

    def build(self):
        self.view_book_form_instance()

        viewButton = ViewButton(self.page)

        # se busca el libro seleccionado
        id = BookStore["state"]["bookSelected"]
        if id:
            book = Libro.buscar(id)

        return Column(
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.form_header(),
                Column(
                    controls=[
                        self.input_form_field("Titulo", value=book["titulo"]),
                        self.input_form_field("Autor", value=book["autor"]),
                        self.input_form_field(
                            "Descripción (opcional)",
                            value=book["descripcion"],
                            multiline=True,
                        ),
                        self.input_form_field(
                            "Cantidad de Copias", value=book["ctdCopias"]
                        ),
                        self.input_form_field(
                            "Fecha de publicacion", value=book["fechaPublicacion"]
                        ),
                        self.input_form_field("Editorial", value=book["editorial"]),
                        self.input_form_field("ISBN (opcional)", value=book["ISBN"]),
                    ]
                ),
                Column(controls=[viewButton]),
            ],
        )
