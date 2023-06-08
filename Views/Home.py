# this is the navbar of the destop application

# modules
from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)  # this are the functions we created in the control.py script

from Components.Navbar import AppNavbar  # Navbar application
from Components.SearchInput import SearchInput  # Navbar application
from Components.BooksTable import BooksTable  # Navbar application

# we can set the returned dict as a variable at the top of the class
# we'll use it later in the app
control_map = return_control_reference()


# main class
class HomeView(UserControl):
    def __init__(self, page):
        self.page = page
        super().__init__()

    def home_view_instance(self):
        # this function sets the class instance as a key:value pair in the global dict.
        add_control_reference("HomeView", self)

    def textbox_changed(e):
        pass
        # t.value = e.control.value
        # page.update()

    def build(self):
        self.home_view_instance()
        return Column(
            controls=[
                # class instances go here...
                AppNavbar(),
                Container(
                    content=SearchInput(),
                    margin=margin.symmetric(horizontal=20, vertical=15),
                ),
                ElevatedButton(
                    "Agregar Libro",
                    icon=icons.ADD,
                    on_click=lambda _: self.page.go("/books/add-book"),
                ),
                Container(
                    content=Column(controls=[BooksTable([])]),
                    margin=margin.symmetric(horizontal=20, vertical=15),
                ),
            ]
        )
