# this is the BookFomr of the desktop application

#modules
from flet import *
from controls import add_control_reference, return_control_reference # this are the functions we created in the control.py script

# we can set the returned dict as a variable at the top of the class
# we'll use it later in the app
control_map = return_control_reference()

# main class
class BookForm (UserControl):
    def __init__(self, page = None):
        self.page = page
        super().__init__()
    def book_form_instance(self):
        # this function sets the class instance as a key:value pair in the global dict.
        add_control_reference("BookForm", self)
    def textbox_changed(e):
        pass
            #t.value = e.control.value
            #page.update()
    def form_header():
        pass
    def input_form_field():
        pass
    def build (self):
        self.book_form_instance()

        return Column(
            controls=[self.form_header(),
            self.input_form_field(),
            self.input_form_field(),
            self.input_form_field(),
            self.input_form_field(),
            self.input_form_field(),
            self.input_form_field(),
            self.input_form_field(),]
        )
