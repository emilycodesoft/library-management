# Editorial y Autor Clases
from collections.abc import Iterable
from firestore import db


class Libro:
    def __init__(self):
        self.titulo = None
        self.autor = None
        self.descripcion = None
        self.ctdCopias = None
        self.fechaPublicacion = None
        self.editorial = None
        self.ISBN = None

    def __dir__(self) -> Iterable[str]:
        [
            "titulo",
            "autor",
            "descripcion",
            "ctdCopias",
            "fechaPublicacion",
            "editorial",
            "ISBN",
        ]

    def agregar(self):
        book = {
            "titulo": self.titulo,
            "autor": self.autor,
            "descripcion": self.descripcion,
            "ctdCopias": self.ctdCopias,
            "fechaPublicacion": self.fechaPublicacion,
            "editorial": self.editorial,
            "ISBN": self.ISBN,
        }
        db.collection("books").add(book)

    def editar(self, id):
        print(id)
        print(
            {
                "titulo": self.titulo,
                "autor": self.autor,
                "descripcion": self.descripcion,
                "ctdCopias": self.ctdCopias,
                "fechaPublicacion": self.fechaPublicacion,
                "editorial": self.editorial,
                "ISBN": self.ISBN,
            }
        )
        doc_ref = db.collection("books").document(f"{id}")
        # Set the capital field
        doc_ref.update(
            {
                "titulo": self.titulo,
                "autor": self.autor,
                "descripcion": self.descripcion,
                "ctdCopias": self.ctdCopias,
                "fechaPublicacion": self.fechaPublicacion,
                "editorial": self.editorial,
                "ISBN": self.ISBN,
            }
        )

    @classmethod
    def eliminar(self, id):
        db.collection("books").document("" + f"{id}").delete()

    @classmethod
    def buscar(self, id):
        doc_ref = db.collection("books").document(f"{id}")
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return False
