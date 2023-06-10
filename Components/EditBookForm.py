from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)

# componentes requeridos para este componente: EditBookForm
from Components.EditButton import EditButton
from Components.DeleteButton import DeleteButton

# modelos requeridos para este componente: EditBookForm
from Classes.Libro import Libro

# stores requeridas para este componente: EditBookForm
from Store.BooksStore import BookStore

control_map = return_control_reference()


# clase principal
class EditBookForm(UserControl):
    def __init__(self, page=None):
        super().__init__()
        self.page = page

    def edit_book_form_instance(self):
        add_control_reference("EditBookForm", self)

    # header del formulario
    def form_header(self):
        return Container(
            content=Text("Editar Libro", style=TextThemeStyle.TITLE_LARGE),
            margin=margin.only(bottom=20),
        )

    # campo de texto del formulario
    def input_form_field(self, label: str, multiline=False, value=""):
        return TextField(label=label, multiline=multiline, value=value)

    def build(self):
        self.edit_book_form_instance()

        editButton = EditButton(self.page)
        deleteButton = DeleteButton(self.page)

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
                Column(
                    controls=[
                        editButton,
                        deleteButton,
                    ]
                ),
            ],
        )
