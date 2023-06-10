from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)

# componentes requeridos para este componente: AddBookForm
from Components.AddButton import AddButton

control_map = return_control_reference()


# clase principal
class AddBookForm(UserControl):
    def __init__(self, page=None):
        super().__init__()
        self.page = page

    # añadimos el componente al controlador
    def add_book_form_instance(self):
        add_control_reference("AddBookForm", self)

    # header del componente
    def form_header(self):
        return Container(
            content=Text("Agregar Libro", style=TextThemeStyle.TITLE_LARGE),
            margin=margin.only(bottom=20),
        )

    # campo de texto del componente
    def input_form_field(self, label: str, multiline=False, value=""):
        return TextField(label=label, multiline=multiline, value=value)

    def build(self):
        self.add_book_form_instance()

        Button = AddButton(self.page)

        return Column(
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.form_header(),
                Column(
                    controls=[
                        self.input_form_field("Titulo"),
                        self.input_form_field("Autor"),
                        self.input_form_field("Descripción", multiline=True),
                        self.input_form_field("Cantidad de Copias"),
                        self.input_form_field("Fecha de publicacion"),
                        self.input_form_field("Editorial"),
                        self.input_form_field("ISBN"),
                    ]
                ),
                Button,
            ],
        )
