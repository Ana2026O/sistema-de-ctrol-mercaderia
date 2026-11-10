import customtkinter as ctk
from tkinter import ttk


class Historial(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Historial de Movimientos")
        self.geometry("900x600")
        self.resizable(False, False)

        self.configure(fg_color="#E8EEF5")

        # Título
        titulo = ctk.CTkLabel(
            self,
            text="HISTORIAL DE MOVIMIENTOS",
            font=("Arial", 28, "bold"),
            text_color="#0B3D91"
        )
        titulo.pack(pady=(20, 10))

        # Línea separadora
        linea = ctk.CTkFrame(
            self,
            width=800,
            height=3,
            fg_color="#0B3D91"
        )
        linea.pack(pady=10)

        # Buscar
        ctk.CTkLabel(
            self,
            text="Buscar:"
        ).pack()

        self.txt_buscar = ctk.CTkEntry(
            self,
            width=300
        )
        self.txt_buscar.pack(pady=5)

        btn_buscar = ctk.CTkButton(
            self,
            text="Buscar",
            width=150
        )
        btn_buscar.pack(pady=10)

        # Tabla
        columnas = (
            "Fecha",
            "Tipo",
            "Producto",
            "Cantidad"
        )

        tabla = ttk.Treeview(
            self,
            columns=columnas,
            show="headings",
            height=12
        )

        for col in columnas:
            tabla.heading(col, text=col)

        tabla.column("Fecha", width=150)
        tabla.column("Tipo", width=150)
        tabla.column("Producto", width=300)
        tabla.column("Cantidad", width=120)

        tabla.pack(pady=20)

        # Datos de ejemplo
        tabla.insert(
            "",
            "end",
            values=("04/11/2026", "Ingreso", "Coca Cola", 20)
        )

        tabla.insert(
            "",
            "end",
            values=("04/11/2026", "Salida", "Agua", 5)
        )

        tabla.insert(
            "",
            "end",
            values=("05/11/2026", "Ingreso", "Sprite", 10)
        )

        # Botón volver
        btn_volver = ctk.CTkButton(
            self,
            text="Volver",
            width=200,
            fg_color="gray"
        )
        btn_volver.pack(pady=15)


if __name__ == "__main__":
    app = Historial()
    app.mainloop()