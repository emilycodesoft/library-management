from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)

# componentes requeridos para esta vista: Home
from Components.Navbar import AppNavbar
from Components.SearchInput import SearchInput
from Components.BooksTable import BooksTable
from Store.BooksStore import BookStore

control_map = return_control_reference()


# clase principal
class HomeView(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    # añadimos vista al controlador
    def home_view_instance(self):
        add_control_reference("HomeView", self)

    def add_book(self, e):
        BookStore["state"]["book_state"] = "ADD"
        self.page.go("/books/add-book")

    def build(self):
        self.home_view_instance()

        BookTable = BooksTable(self.page)

        return Column(
            controls=[
                AppNavbar(),
                Container(
                    content=SearchInput(),
                    margin=margin.symmetric(horizontal=20, vertical=15),
                ),
                ElevatedButton(
                    "Agregar Libro",
                    icon=icons.ADD,
                    on_click=self.add_book,
                ),
                Container(
                    content=Column(controls=[BookTable]),
                    margin=margin.symmetric(horizontal=20, vertical=15),
                ),
            ]
        )
