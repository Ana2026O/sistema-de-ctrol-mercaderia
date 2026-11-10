import customtkinter as ctk
from tkinter import ttk


class GestionarCategorias(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestionar Categorías")
        self.geometry("950x700")
        self.resizable(False, False)

        self.configure(fg_color="#E8EEF5")

        # Título
        titulo = ctk.CTkLabel(
            self,
            text="GESTIONAR CATEGORÍAS Y SUBCATEGORÍAS",
            font=("Arial", 24, "bold"),
            text_color="#0B3D91"
        )
        titulo.pack(pady=(20, 10))

        # Línea
        linea = ctk.CTkFrame(
            self,
            width=850,
            height=3,
            fg_color="#0B3D91"
        )

        linea.pack(pady=10)

        # Categoría

        ctk.CTkLabel(
            self,
            text="Categoría:"
        ).pack()

        self.txt_categoria = ctk.CTkEntry(
            self,
            width=300
        )
        self.txt_categoria.pack(pady=5)

        btn_categoria = ctk.CTkButton(
            self,
            text="Registrar Categoría",
            width=250
        )
        btn_categoria.pack(pady=10)

        # Subcategoría

        ctk.CTkLabel(
            self,
            text="Subcategoría:"
        ).pack()

        self.txt_subcategoria = ctk.CTkEntry(
            self,
            width=300
        )
        self.txt_subcategoria.pack(pady=5)

        ctk.CTkLabel(
            self,
            text="Categoría asociada:"
        ).pack()

        self.cmb_categoria = ctk.CTkComboBox(
            self,
            values=[
                "Gaseosas",
                "Jugos",
                "Agua"
            ],
            width=300
        )
        self.cmb_categoria.pack(pady=5)

        btn_subcategoria = ctk.CTkButton(
            self,
            text="Registrar Subcategoría",
            width=250
        )
        btn_subcategoria.pack(pady=15)

        # Tabla categorías

        ctk.CTkLabel(
            self,
            text="Categorías Registradas",
            font=("Arial", 16, "bold")
        ).pack()

        tabla_cat = ttk.Treeview(
            self,
            columns=("ID", "Categoria"),
            show="headings",
            height=4
        )

        tabla_cat.heading("ID", text="ID")
        tabla_cat.heading("Categoria", text="Categoría")

        tabla_cat.pack(pady=10)

        tabla_cat.insert("", "end", values=(1, "Gaseosas"))
        tabla_cat.insert("", "end", values=(2, "Jugos"))
        tabla_cat.insert("", "end", values=(3, "Agua"))

        # Tabla subcategorías

        ctk.CTkLabel(
            self,
            text="Subcategorías Registradas",
            font=("Arial", 16, "bold")
        ).pack()

        tabla_sub = ttk.Treeview(
            self,
            columns=(
                "ID",
                "Subcategoria",
                "Categoria"
            ),
            show="headings",
            height=4
        )

        tabla_sub.heading("ID", text="ID")
        tabla_sub.heading(
            "Subcategoria",
            text="Subcategoría"
        )
        tabla_sub.heading(
            "Categoria",
            text="Categoría"
        )

        tabla_sub.pack(pady=10)

        tabla_sub.insert(
            "",
            "end",
            values=(1, "Cola", "Gaseosas")
        )

        tabla_sub.insert(
            "",
            "end",
            values=(2, "Lima-Limón", "Gaseosas")
        )

        tabla_sub.insert(
            "",
            "end",
            values=(3, "Naranja", "Jugos")
        )

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
        btn_volver.pack(pady=10)


if __name__ == "__main__":
    app = GestionarCategorias()
    app.mainloop()