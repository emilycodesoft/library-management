# this is the navbar of the destop application

#modules
from flet import *
from controls import add_control_reference, return_control_reference # this are the functions we created in the control.py script

# we can set the returned dict as a variable at the top of the class
# we'll use it later in the app
control_map = return_control_reference()

# main class
class SearchInput (UserControl):
    def __init__(self, page = None):
        self.page = page
        super().__init__()
    def search_input_instance(self):
        # this function sets the class instance as a key:value pair in the global dict.
        add_control_reference("SearchInput", self)
    def textbox_changed(e):
        pass
            #t.value = e.control.value
            #page.update()
    def build (self):
        self.search_input_instance()

        return TextField(
            label="Buscar Libro",
            on_change=self.textbox_changed,
        )
