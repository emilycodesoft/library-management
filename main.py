# modulos necesarios
import flet as ft

from Views.Home import HomeView
from Views.AddBook import AddBookView
from Views.EditBook import EditBookView
from Views.ViewBook import ViewBookView

from controls import (
    add_control_reference,
)


def salir(page):
    page.window_close()


def main(page: ft.Page):
    page.title = "Gestion de Bibliotecas"

    # Establece la aplicación en modo oscuro
    page.theme_mode = "dark"

    # agrega la pagina a un controlador general
    add_control_reference("page", page)

    # El navbar de la Aplicación
    bar = ft.AppBar(
        leading=ft.Icon(ft.icons.BOOK),
        leading_width=40,
        title=ft.Text("GestiBiblioteca"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        text="Salir", checked=False, on_click=lambda _: salir(page)
                    ),
                ]
            ),
        ],
    )

    # Vistas
    Home = HomeView(page)
    AddBook = AddBookView(page)
    EditBook = EditBookView(page)
    ViewBook = ViewBookView(page)

    # funcion que se ejecuta cada vez que la ruta cambia
    def route_change(route):
        page.views.clear()

        # Vista principal
        page.views.append(
            ft.View(
                "/",
                [bar, Home],
                scroll=ft.ScrollMode.AUTO,
            )
        )

        # Vista de añadir
        if page.route == "/books/add-book":
            page.views.append(
                ft.View(
                    "/books/add-book",
                    [bar, AddBook],
                    scroll=ft.ScrollMode.AUTO,
                )
            )
        # Vista de editar
        if page.route == "/books/edit-book":
            page.views.append(
                ft.View(
                    "/books/edit-book",
                    [bar, EditBook],
                    scroll=ft.ScrollMode.ALWAYS,
                )
            )
        # Vista de ver
        if page.route == "/books/view-book":
            page.views.append(
                ft.View(
                    "/books/view-book",
                    [bar, ViewBook],
                    scroll=ft.ScrollMode.ALWAYS,
                )
            )
        # actualiza la pagina con la nueva vista
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # cuando cambie la ruta se ejecuta estan funciones
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
