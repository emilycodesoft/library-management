# necessary modules
import flet as ft

from Components.Navbar import AppNavbar # Navbar application
from Components.SearchInput import SearchInput # Navbar application
from Components.BooksTable import BooksTable # Navbar application


""" # Definir las clases y métodos del sistema de gestión de biblioteca como se hizo anteriormente
class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
    
    def mostrar_info(self):
       pass

class LibroPrestado(Libro):
    def __init__(self, titulo, autor, genero, prestado_a):
        super().__init__(titulo, autor, genero)
        self.prestado_a = prestado_a
    
    def mostrar_info(self):
        pass

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def mostrar_libros(self):
        lista_libros = "\n".join([f"{libro.titulo} - {libro.autor}" for libro in self.libros])
    
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None
    def editar_libro(self, titulo, nuevo_titulo, nuevo_autor, nuevo_genero):
        libro = self.buscar_libro(titulo)
        if libro:
            libro.titulo = nuevo_titulo
            libro.autor = nuevo_autor
            libro.genero = nuevo_genero
            # messagebox.showinfo("Libro Editado", "El libro ha sido editado exitosamente.")
        else:
            pass
            # messagebox.showinfo("Libro no encontrado", f"No se encontró el libro con el título '{titulo}'.")
    
    def eliminar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            self.libros.remove(libro)
            # messagebox.showinfo("Libro Eliminado", "El libro ha sido eliminado exitosamente.")
        else:
            pass
            # messagebox.showinfo("Libro no encontrado", f"No se encontró el libro con el título '{titulo}'.")
    
    def prestar_libro(self, titulo, usuario):
        libro = self.buscar_libro(titulo)
        if libro:
            libro_prestado = LibroPrestado(libro.titulo, libro.autor, libro.genero, usuario)
            self.libros.remove(libro)
            self.libros.append(libro_prestado)
            # messagebox.showinfo("Libro Prestado", f"El libro '{libro.titulo}' ha sido prestado a '{usuario}'.")
        else:
            pass
            # messagebox.showinfo("Libro no encontrado", f"No se encontró el libro con el título '{titulo}'.") """

# Crear la interfaz gráfica utilizando Flet
""" class GUI:
    def __init__(self, page):
        page.title = "Gestión de Biblioteca"
        # page.vertical_alignment = ft.MainAxisAlignment.CENTER
        # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # Crear botones
        self.btn_mostrar_libros = ft.ElevatedButton(text="Libros", on_click=self.mostrar_libros)
        self.btn_agregar_libro = ft.ElevatedButton(text="Libros Prestados", on_click=self.agregar_libro)
        self.btn_buscar_libro = ft.ElevatedButton(text="Lectores", on_click=self.buscar_libro)

        def salir(e):
            page.window_close()

        page.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.BOOK),
            leading_width=40,
            title=ft.Text("GestiBiblioteca"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                # ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
                # ft.IconButton(ft.icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            text="Salir", checked=False, on_click=salir
                        ),
                    ]
                ),
            ],
        )
        page.add(ft.Row(controls=[self.btn_mostrar_libros, self.btn_agregar_libro, self.btn_buscar_libro]))
        def textbox_changed(e):
            t.value = e.control.value
            page.update()

        t = ft.Text()
        tb = ft.TextField(
            label="Buscar Libro",
            on_change=textbox_changed,
        )

        page.add(ft.Container(content=tb, margin=ft.margin.symmetric(horizontal=20, vertical=15)))
        page.add(
        ft.ElevatedButton("Agregar Libro", icon=ft.icons.ADD, )
        )
        page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Titulo")),
                ft.DataColumn(ft.Text("Autor"), numeric=True),
                ft.DataColumn(ft.Text("# de Copias"), numeric=True),
                ft.DataColumn(ft.Text("Estado"), numeric=True),
                ft.DataColumn(ft.Text("Acciones"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("1")),
                        ft.DataCell(ft.Text("Cien Años de Soledad")),
                        ft.DataCell(ft.Text("Gabriel Garcia Marquez")),
                        ft.DataCell(ft.Text("20")),
                        ft.DataCell(ft.Text("Prestado")),
                        ft.DataCell(ft.Row(controls=[ft.IconButton(
                    icon=ft.icons.VIEW_AGENDA,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause record",
                ), ft.IconButton(
                    icon=ft.icons.EDIT,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause record",
                ), ft.IconButton(
                    icon=ft.icons.DELETE,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause record",
                )])),
                    ],
                ),
            ],
        ),
    )
        # Crear biblioteca
        # self.biblioteca = Biblioteca("Biblioteca Central")
    
    def mostrar_libros(self):
        pass
        self.biblioteca.mostrar_libros()
    
    def agregar_libro(self):
        # Implementa aquí la lógica para crear la interfaz gráfica de agregar libro con Flet
        pass
    
    def buscar_libro(self):
        # Implementa aquí la lógica para crear la interfaz gráfica de buscar libro con Flet
        pass
 """

def salir(page):
    page.window_close()

def main(page: ft.Page):
    page.title = "Gestion de Bibliotecas"
    libros = []

    page.appbar = ft.AppBar(
                leading=ft.Icon(ft.icons.BOOK),
                leading_width=40,
                title=ft.Text("GestiBiblioteca"),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Salir", checked=False, on_click= lambda _: salir(page)
                            ),
                        ]
                    ),
                ],
            )
    page.add(ft.Column( controls=[
                # class instances go here...
                AppNavbar(),
                ft.Container(content=SearchInput(), margin=ft.margin.symmetric(horizontal=20, vertical=15)),
                ft.ElevatedButton("Agregar Libro", icon=ft.icons.ADD, on_click= lambda _: page.go("/books/add-book")),
                ft.Container(content=ft.Column(controls=[BooksTable()]), margin=ft.margin.symmetric(horizontal=20, vertical=15)),        
            ]))
    
    def route_change(route):
        pass
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)