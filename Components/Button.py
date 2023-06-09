# this is the main file where we handle user input data

# modules
from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
    pageControl,
)  # this are the functions we created in the control.py script

from Helpers.BookForm import BookFormHelper
from Classes.Libro import Libro

# we can set the returned dict as a variable at the top of the class
# we'll use it later in the app
control_map = return_control_reference()
# page here


# this method will handle the main data from the user.
def get_input_data(e):
    # recall that the form instance is saved in the dictionary, we can acces this now.
    data = []
    for key, value in control_map.items():
        # once we are in the key, we need to create a DataRow
        if key == "BookForm":
            # once we have the key, we can now loop over the textfields and get the values
            for user_input in value.controls[0].controls[1].controls[:]:
                # here we can now append that DataRow...
                # data.cells.append(BookFormHelper(user_input.value))
                data.append(user_input.value)
            # now that we have access to the values, we should create a data row + cell to insert it into the table
        # we need to update the datatable after we append the info

    libro = Libro(*data)
    libro.agregar()
    control_map["page"].go("/")  # improve


# main class
class AppButton(UserControl):
    def __init__(self, page=None):
        self.page = page
        super().__init__()

    def app_button_instance(self):
        # this function sets the class instance as a key:value pair in the global dict.
        add_control_reference("AppButton", self)

    def build(self):
        self.app_button_instance()
        return ElevatedButton(
            text="Agregar",
            width=400,
            style=ButtonStyle(padding=20),
            on_click=get_input_data,
        )
