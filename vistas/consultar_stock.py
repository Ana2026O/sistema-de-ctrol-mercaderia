import customtkinter as ctk
from tkinter import ttk


class ConsultarStock(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Consultar Inventario")
        self.geometry("900x600")
        self.resizable(False, False)

        self.configure(fg_color="#E8EEF5")

        titulo = ctk.CTkLabel(
            self,
            text="CONSULTAR INVENTARIO",
            font=("Arial", 28, "bold"),
            text_color="#0B3D91"
        )
        titulo.pack(pady=(20, 10))

        linea = ctk.CTkFrame(
            self,
            width=800,
            height=3,
            fg_color="#0B3D91"
        )
        linea.pack(pady=10)

        ctk.CTkLabel(
            self,
            text="Buscar producto:"
        ).pack(pady=(10, 5))

        self.txt_buscar = ctk.CTkEntry(
            self,
            width=300
        )
        self.txt_buscar.pack()

        btn_buscar = ctk.CTkButton(
            self,
            text="Buscar",
            width=150
        )
        btn_buscar.pack(pady=10)

        # Tabla
        columnas = ("ID", "Producto", "Cantidad")

        tabla = ttk.Treeview(
            self,
            columns=columnas,
            show="headings",
            height=10
        )

        tabla.heading("ID", text="ID")
        tabla.heading("Producto", text="Producto")
        tabla.heading("Cantidad", text="Cantidad")

        tabla.column("ID", width=80)
        tabla.column("Producto", width=450)
        tabla.column("Cantidad", width=150)

        tabla.pack(pady=20)

        # Datos de ejemplo
        tabla.insert("", "end", values=(1, "Coca Cola 2.25L", 20))
        tabla.insert("", "end", values=(2, "Agua 1.5L", 15))
        tabla.insert("", "end", values=(3, "Sprite 2.25L", 10))
        tabla.insert("", "end", values=(4, "Jugo Naranja", 8))

        btn_volver = ctk.CTkButton(
            self,
            text="Volver",
            width=200,
            fg_color="gray"
        )
        btn_volver.pack(pady=15)


if __name__ == "__main__":
    app = ConsultarStock()
    app.mainloop()