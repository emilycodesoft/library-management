
# this is the header of the destop application

#modules
from flet import *
from controls import add_control_reference, return_control_reference # this are the functions we created in the control.py script

# we can set the returned dict as a variable at the top of the class
# we'll use it later in the app
control_map = return_control_reference()

# main class
class AppHeader (UserControl):
    def __init__(self, page):
        self.page = page
        super().__init__()
    def app_header_instance(self):
        # this function sets the class instance as a key:value pair in the global dict.
        add_control_reference("AppHeader", self)
    def salir(self):
            self.page.windows_close()
    def build (self):
        self.app_header_instance()
        return AppBar(
            leading= Icon( icons.BOOK),
            leading_width=40,
            title= Text("GestiBiblioteca"),
            center_title=False,
            bgcolor= colors.SURFACE_VARIANT,
            actions=[
                #IconButton( icons.WB_SUNNY_OUTLINED),
                # IconButton( icons.FILTER_3),
                PopupMenuButton(
                    items=[
                         PopupMenuItem(
                            text="Salir", checked=False, on_click=self.salir
                        ),
                    ]
                ),
            ],
        )