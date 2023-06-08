# this is the main file where we handle user input data

# modules
from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)  # this are the functions we created in the control.py script

from Helpers.BookForm import BookFormHelper

# we can set the returned dict as a variable at the top of the class
# we'll use it later in the app
control_map = return_control_reference()


# this method will handle the main data from the user.
def get_input_data(page):
    # recall that the form instance is saved in the dictionary, we can acces this now.
    data = DataRow(cells=[])
    for key, value in control_map.items():
        # once we are in the key, we need to create a DataRow
        if key == "BookForm":
            # once we have the key, we can now loop over the textfields and get the values
            # print(control_map)
            for user_input in value.controls[0].controls[1].controls[:]:
                # here we can now append that DataRow...
                print(control_map)
                data.cells.append(BookFormHelper(user_input.value))
            # now that we have access to the values, we should create a data row + cell to insert it into the table
        # we need to update the datatable after we append the info
    for key, value in control_map.items():
        if key == "BooksTable":
            Page.client_storage.set("data", data)
            print(Page.client_storage.get("data"))
            # value.controls[0].controls[0].rows.append(data)
            # value.controls[0].controls[0].update()


# main class
class AppButton(UserControl):
    def __init__(self, page=None):
        self.page = page
        super().__init__()

    def app_button_instance(self):
        # this function sets the class instance as a key:value pair in the global dict.
        add_control_reference("AppButton", self)

    def textbox_changed(e):
        pass
        # t.value = e.control.value
        # page.update()

    def build(self):
        self.app_button_instance()
        return ElevatedButton(
            text="Agregar",
            width=400,
            style=ButtonStyle(padding=20),
            on_click=lambda _: get_input_data(self.page),
        )
