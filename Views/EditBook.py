# this is the navbar of the destop application

# modules
from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)  # this are the functions we created in the control.py script

from Components.BookForm import BookForm

# we can set the returned dict as a variable at the top of the class
# we'll use it later in the app
control_map = return_control_reference()


# main class
class EditBookView(UserControl):
    def __init__(self, page=None):
        self.page = page
        super().__init__()

    def edit_bookview_instance(self):
        # this function sets the class instance as a key:value pair in the global dict.
        add_control_reference("EditBookView", self)

    def textbox_changed(e):
        pass
        # t.value = e.control.value
        # page.update()

    def build(self):
        self.edit_bookview_instance()
        BookF = BookForm(self.page)
        return Column(
            controls=[
                # class instances go here...
                ElevatedButton("Volver", on_click=lambda _: self.page.go("/")),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[BookF],
                ),
            ]
        )
