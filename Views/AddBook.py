# this is the navbar of the destop application

#modules
from flet import *
from controls import add_control_reference, return_control_reference # this are the functions we created in the control.py script

from Components.SearchInput import SearchInput # Navbar application


# we can set the returned dict as a variable at the top of the class
# we'll use it later in the app
control_map = return_control_reference()

# main class
class AddBookView (UserControl):
    def __init__(self, page = None):
        self.page = page
        super().__init__()
    def add_book_view_instance(self):
        # this function sets the class instance as a key:value pair in the global dict.
        add_control_reference("AddBookView", self)
    def textbox_changed(e):
        pass
            #t.value = e.control.value
            #page.update()
    def salir(page):
        page.window_close()
    def build (self):
        self.add_book_view_instance()

        return Column(controls=[ElevatedButton("Volver", on_click=lambda _: self.page.go("/")),
                             Container(width=400, content=Column(controls=[SearchInput(), SearchInput()]))])