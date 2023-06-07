import tkinter as tk
from tkinter import messagebox

class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
    
    def mostrar_info(self):
        messagebox.showinfo("Información del libro", f"Título: {self.titulo}\nAutor: {self.autor}\nGénero: {self.genero}")

class LibroPrestado(Libro):
    def __init__(self, titulo, autor, genero, prestado_a):
        super().__init__(titulo, autor, genero)
        self.prestado_a = prestado_a
    
    def mostrar_info(self):
        messagebox.showinfo("Información del libro prestado", f"Título: {self.titulo}\nAutor: {self.autor}\nGénero: {self.genero}\nPrestado a: {self.prestado_a}")

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def mostrar_libros(self):
        lista_libros = "\n".join([f"{libro.titulo} - {libro.autor}" for libro in self.libros])
        messagebox.showinfo("Libros en la biblioteca", f"Libros en la biblioteca:\n{lista_libros}")
    
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
            messagebox.showinfo("Libro Editado", "El libro ha sido editado exitosamente.")
        else:
            messagebox.showinfo("Libro no encontrado", f"No se encontró el libro con el título '{titulo}'.")
    
    def eliminar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            self.libros.remove(libro)
            messagebox.showinfo("Libro Eliminado", "El libro ha sido eliminado exitosamente.")
        else:
            messagebox.showinfo("Libro no encontrado", f"No se encontró el libro con el título '{titulo}'.")

class GUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Biblioteca")
        
        # Crear botones
        self.btn_mostrar_libros = tk.Button(ventana, text="Mostrar Libros", command=self.mostrar_libros)
        self.btn_mostrar_libros.pack(pady=10)
        
        self.btn_agregar_libro = tk.Button(ventana, text="Agregar Libro", command=self.agregar_libro)
        self.btn_agregar_libro.pack(pady=10)

        self.btn_editar_libro = tk.Button(ventana, text="Editar Libro", command=self.editar_libro)
        self.btn_editar_libro.pack(pady=10)

        self.btn_eliminar_libro = tk.Button(ventana, text="Eliminar Libro", command=self.eliminar_libro)
        self.btn_eliminar_libro.pack(pady=10)
        
        self.btn_buscar_libro = tk.Button(ventana, text="Buscar Libro", command=self.buscar_libro)
        self.btn_buscar_libro.pack(pady=10)
        
        self.btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
        self.btn_salir.pack(pady=10)
        
        # Crear biblioteca
        self.biblioteca = Biblioteca("Biblioteca Central")
    
    def mostrar_libros(self):
        self.biblioteca.mostrar_libros()
    
    def agregar_libro(self):
        ventana_agregar = tk.Toplevel(self.ventana)
        ventana_agregar.title("Agregar Libro")
        
        # Crear campos de entrada
        lbl_titulo = tk.Label(ventana_agregar, text="Título:")
        lbl_titulo.pack()
        entry_titulo = tk.Entry(ventana_agregar)
        entry_titulo.pack(pady=5)
        
        lbl_autor = tk.Label(ventana_agregar, text="Autor:")
        lbl_autor.pack()
        entry_autor = tk.Entry(ventana_agregar)
        entry_autor.pack(pady=5)
        lbl_genero = tk.Label(ventana_agregar, text="Género:")
        lbl_genero.pack()
        entry_genero = tk.Entry(ventana_agregar)
        entry_genero.pack(pady=5)

        # Función para agregar el libro
        def agregar():
            titulo = entry_titulo.get()
            autor = entry_autor.get()
            genero = entry_genero.get()
            
            if titulo and autor and genero:
                libro = Libro(titulo, autor, genero)
                self.biblioteca.agregar_libro(libro)
                messagebox.showinfo("Libro Agregado", "El libro ha sido agregado con éxito.")
                ventana_agregar.destroy()
            else:
                messagebox.showwarning("Campos Incompletos", "Por favor, completa todos los campos.")
        

        # Crear botón de agregar
        btn_agregar = tk.Button(ventana_agregar, text="Agregar", command=agregar)
        btn_agregar.pack(pady=10)

    def buscar_libro(self):
            ventana_buscar = tk.Toplevel(self.ventana)
            ventana_buscar.title("Buscar Libro")
            
            # Crear campo de entrada
            lbl_titulo = tk.Label(ventana_buscar, text="Título:")
            lbl_titulo.pack()
            entry_titulo = tk.Entry(ventana_buscar)
            entry_titulo.pack(pady=5)
            
            # Función para buscar el libro
            def buscar():
                titulo = entry_titulo.get()
                if titulo:
                    libro = self.biblioteca.buscar_libro(titulo)
                    if libro:
                        libro.mostrar_info()
                    else:
                        messagebox.showinfo("Libro no encontrado", f"No se encontró el libro con el título '{titulo}'.")
                    ventana_buscar.destroy()
                else:
                    messagebox.showwarning("Campo Incompleto", "Por favor, ingresa el título del libro.")
            
            # Crear botón de buscar
            btn_buscar = tk.Button(ventana_buscar, text="Buscar", command=buscar)
            btn_buscar.pack(pady=10)




 # Crear la ventana principal
ventana_principal = tk.Tk()
gui = GUI(ventana_principal)
ventana_principal.mainloop()