from flet import *
from controls import (
    add_control_reference,
    return_control_reference,
)

# llamado a la instancia de la base de datos
from firestore import db, firestore

# llamado al store de libros (un diccionario principal para manejar información de los libros entre componentes de manera centralizada)
from Store.BooksStore import BookStore

control_map = return_control_reference()


# clase principal
class BooksTable(UserControl):
    def __init__(self, page=None):
        self.table = None
        self.page = page
        super().__init__()

    def books_table_instance(self):
        add_control_reference("BooksTable", self)

    def view_book(self, id):
        BookStore["state"]["bookSelected"] = id
        self.page.go("/books/view-book")

    def edit_book(self, id):
        BookStore["state"]["bookSelected"] = id
        self.page.go("/books/edit-book")

    def book_row(self, book, id, index):
        return DataRow(
            cells=[
                DataCell(Text(index + 1)),
                DataCell(Text(book["titulo"])),
                DataCell(Text(book["autor"])),
                DataCell(Text(book["ctdCopias"])),
                DataCell(Text(book["editorial"])),
                DataCell(
                    Row(
                        controls=[
                            IconButton(
                                icon=icons.LIBRARY_BOOKS,
                                icon_color="blue400",
                                icon_size=20,
                                tooltip="Ver Libro",
                                on_click=lambda _: self.view_book(id),
                            ),
                            IconButton(
                                icon=icons.EDIT,
                                icon_color="blue400",
                                icon_size=20,
                                tooltip="Editar Libro",
                                on_click=lambda _: self.edit_book(id),
                            ),
                        ],
                    )
                ),
            ],
        )

    def build(self):
        self.books_table_instance()

        # llamado a la collccion de libros en la base de datos
        books_ref = db.collection("books").order_by(
            "timestamp", direction=firestore.Query.DESCENDING
        )
        books = books_ref.stream()

        # instancia de la cabecera de la tabla
        Table = DataTable(
            expand=True,
            columns=[
                DataColumn(Text("#")),
                DataColumn(Text("Titulo")),
                DataColumn(Text("Autor")),
                DataColumn(Text("# de Copias"), numeric=True),
                DataColumn(Text("Editorial")),
                DataColumn(Text("Acciones")),
            ],
            rows=[],
        )

        self.table = Table

        # se añade los libros de acuerdo a la cantidad de libros que haya en la base de datos
        for i, book in enumerate(books):
            bookRow = self.book_row(book.to_dict(), book.id, i)
            Table.rows.append(bookRow)

        return Row(
            expand=True,
            controls=[Table],
        )
