import customtkinter as ctk
from tkinter import ttk


class GestionarProductos(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestionar Productos")
        self.geometry("900x650")
        self.resizable(False, False)

        self.configure(fg_color="#E8EEF5")

        # Título
        titulo = ctk.CTkLabel(
            self,
            text="GESTIONAR PRODUCTOS",
            font=("Arial", 28, "bold"),
            text_color="#0B3D91"
        )
        titulo.pack(pady=(20, 10))

        # Línea
        linea = ctk.CTkFrame(
            self,
            width=800,
            height=3,
            fg_color="#0B3D91"
        )
        linea.pack(pady=10)

        # Nombre
        ctk.CTkLabel(
            self,
            text="Nombre del producto:"
        ).pack()

        self.txt_nombre = ctk.CTkEntry(
            self,
            width=300
        )
        self.txt_nombre.pack(pady=5)

        # Categoría
        ctk.CTkLabel(
            self,
            text="Categoría:"
        ).pack()

        self.cmb_categoria = ctk.CTkComboBox(
            self,
            values=[
                "Gaseosas",
                "Jugos",
                "Agua",
                "Bebidas con Alcohol"
            ],
            width=300
        )
        self.cmb_categoria.pack(pady=5)

        # Subcategoría
        ctk.CTkLabel(
            self,
            text="Subcategoría:"
        ).pack()

        self.cmb_subcategoria = ctk.CTkComboBox(
            self,
            values=[
                "Cola",
                "Lima-Limón",
                "Naranja",
                "Mineral"
            ],
            width=300
        )
        self.cmb_subcategoria.pack(pady=5)

        # Botón Registrar
        btn_registrar = ctk.CTkButton(
            self,
            text="Registrar",
            width=200
        )
        btn_registrar.pack(pady=15)

        # Tabla
        columnas = (
            "ID",
            "Producto",
            "Categoría",
            "Subcategoría"
        )

        tabla = ttk.Treeview(
            self,
            columns=columnas,
            show="headings",
            height=8
        )

        for col in columnas:
            tabla.heading(col, text=col)

        tabla.column("ID", width=60)
        tabla.column("Producto", width=240)
        tabla.column("Categoría", width=180)
        tabla.column("Subcategoría", width=180)

        tabla.pack(pady=20)

        # Datos de ejemplo
        tabla.insert("", "end", values=(
            1,
            "Coca Cola",
            "Gaseosas",
            "Cola"
        ))

        tabla.insert("", "end", values=(
            2,
            "Agua",
            "Sin Alcohol",
            "Mineral"
        ))

        tabla.insert("", "end", values=(
            3,
            "Sprite",
            "Gaseosas",
            "Lima-Limón"
        ))

        # Botones inferiores
        btn_modificar = ctk.CTkButton(
            self,
            text="Modificar",
            width=180
        )
        btn_modificar.pack(pady=5)

        btn_eliminar = ctk.CTkButton(
            self,
            text="Eliminar",
            width=180,
            fg_color="#B22222",
            hover_color="#8B0000"
        )
        btn_eliminar.pack(pady=5)

        btn_volver = ctk.CTkButton(
            self,
            text="Volver",
            width=180,
            fg_color="gray"
        )
        btn_volver.pack(pady=5)


if __name__ == "__main__":
    app = GestionarProductos()
    app.mainloop()