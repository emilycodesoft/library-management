# necessary modules
import flet as ft

from Views.Home import HomeView
from Views.AddBook import AddBookView


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
                        text="Salir", checked=False, on_click=lambda _: salir(page)
                    ),
                ]
            ),
        ],
    )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [HomeView(lambda _: page.title)],
            )
        )
        if page.route == "/books/add-book":
            page.views.append(
                ft.View(
                    "/books/add-book",
                    [AddBookView(page)],
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
