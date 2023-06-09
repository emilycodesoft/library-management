# necessary modules
import flet as ft

from Views.Home import HomeView
from Views.AddBook import AddBookView
from controls import (
    add_control_reference,
)  # this are the functions we created in the control.py script


def salir(page):
    page.window_close()


# page global en cada componente
# llamado desde el


def main(page: ft.Page):
    page.title = "Gestion de Bibliotecas"
    page.theme_mode = "dark"
    add_control_reference("page", page)

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
                        text="Salir", checked=False, on_click=lambda _: salir(page)
                    ),
                ]
            ),
        ],
    )
    Home = HomeView(page)
    AddBook = AddBookView(page)

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [Home],
            )
        )
        if page.route == "/books/add-book":
            page.views.append(
                ft.View(
                    "/books/add-book",
                    [AddBook],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
