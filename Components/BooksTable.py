# this is the navbar of the desktop application

#modules
from flet import *
from controls import add_control_reference, return_control_reference # this are the functions we created in the control.py script

# we can set the returned dict as a variable at the top of the class
# we'll use it later in the app
control_map = return_control_reference()

# main class
class BooksTable (UserControl):
    def __init__(self, page = None):
        self.page = page
        super().__init__()
    def books_table_instance(self):
        # this function sets the class instance as a key:value pair in the global dict.
        add_control_reference("BooksTable", self)
    def textbox_changed(e):
        pass
            #t.value = e.control.value
            #page.update()
    def build (self):
        self.books_table_instance()

        return Row(expand=True, controls=[DataTable(
            expand=True,
            columns=[
                DataColumn(Text("ID")),
                DataColumn(Text("Titulo")),
                DataColumn(Text("Autor")),
                DataColumn(Text("# de Copias"), numeric=True),
                DataColumn(Text("Estado")),
                DataColumn(Text("Acciones")),
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text("1")),
                        DataCell(Text("Cien Años de Soledad")),
                        DataCell(Text("Gabriel Garcia Marquez")),
                        DataCell(Text("20")),
                        DataCell(Text("Prestado")),
                        DataCell(Row(controls=[IconButton(
                    icon=icons.ADD_CARD,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause record",
                ), IconButton(
                    icon=icons.ACCESS_ALARM,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause record",
                ),
                  IconButton(
                    icon=icons.EDIT,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause record",
                ), IconButton(
                    icon=icons.DELETE,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause record",
                )])),
                    ],
                ),
            ],
        )])
