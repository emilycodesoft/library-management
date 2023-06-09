# Editorial y Autor Clases
from firestore import db


class Libro:
    def __init__(
        self, titulo, autor, descripcion, ctdCopias, fechaPublicacion, editorial, ISBN
    ):
        self.tituto = titulo
        self.autor = autor
        self.descripcion = descripcion
        self.ctdCopias = ctdCopias
        self.fechaPublicacion = fechaPublicacion
        self.editorial = editorial
        self.ISBN = ISBN

    def agregar(self):
        book = {
            "titulo": self.tituto,
            "autor": self.autor,
            "descripcion": self.descripcion,
            "ctdCopias": self.ctdCopias,
            "fechaPublicacion": self.fechaPublicacion,
            "editorial": self.editorial,
            "ISBN": self.ISBN,
        }
        doct_ref = db.collection("books").add(book)

    def editar(self):
        # db.( ....)
        pass

    def eliminar(self):
        pass

    def buscar(self):
        pass
