# this is the navbar of the destop application

#modules
from flet import *
from controls import add_control_reference, return_control_reference # this are the functions we created in the control.py script

# we can set the returned dict as a variable at the top of the class
# we'll use it later in the app
control_map = return_control_reference()

# main class
class AppNavbar (UserControl):
    def __init__(self, page = None):
        self.page = page
        super().__init__()
    def app_navbar_instance(self):
        # this function sets the class instance as a key:value pair in the global dict.
        add_control_reference("AppNavBar", self)
    def app_button(self, text: str, on_click):
        return ElevatedButton(text=text, on_click=on_click)
    def mostrar_libros (self):
        pass
    def build (self):
        self.app_navbar_instance()

        return Row(controls=[self.app_button("Mostrar Libros", self.mostrar_libros), self.app_button("Libros Prestados", self.mostrar_libros), self.app_button("Lectores", self.mostrar_libros)])
