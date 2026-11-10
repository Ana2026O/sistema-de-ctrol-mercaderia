import customtkinter as ctk


class RegistrarSalida(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configuración ventana
        self.title("Registrar Salida")
        self.geometry("900x600")
        self.resizable(False, False)

        # Fondo
        self.configure(fg_color="#E8EEF5")

        # Título
        titulo = ctk.CTkLabel(
            self,
            text="REGISTRAR SALIDA",
            font=("Arial", 28, "bold"),
            text_color="#0B3D91"
        )
        titulo.pack(pady=(25, 5))

        # Línea
        linea = ctk.CTkFrame(
            self,
            width=800,
            height=3,
            fg_color="#0B3D91"
        )
        linea.pack(pady=20)

        # Producto
        lbl_producto = ctk.CTkLabel(
            self,
            text="Producto:"
        )
        lbl_producto.pack()

        self.cmb_producto = ctk.CTkComboBox(
            self,
            values=[
                "Coca Cola",
                "Sprite",
                "Agua"
            ],
            width=300
        )
        self.cmb_producto.pack(pady=5)

        # Cantidad
        lbl_cantidad = ctk.CTkLabel(
            self,
            text="Cantidad:"
        )
        lbl_cantidad.pack()

        self.txt_cantidad = ctk.CTkEntry(
            self,
            width=300
        )
        self.txt_cantidad.pack(pady=5)

        # Motivo
        lbl_motivo = ctk.CTkLabel(
            self,
            text="Motivo:"
        )
        lbl_motivo.pack()

        self.cmb_motivo = ctk.CTkComboBox(
            self,
            values=[
                "Traslado",
                "Devolución",
                "Mercadería dañada",
                "Otro"
            ],
            width=300
        )
        self.cmb_motivo.pack(pady=5)

        # Fecha
        lbl_fecha = ctk.CTkLabel(
            self,
            text="Fecha:"
        )
        lbl_fecha.pack()

        self.txt_fecha = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="04/11/2026"
        )
        self.txt_fecha.pack(pady=5)

        # Botón Guardar
        btn_guardar = ctk.CTkButton(
            self,
            text="Guardar Salida",
            width=250
        )
        btn_guardar.pack(pady=20)

        # Botón Volver
        btn_volver = ctk.CTkButton(
            self,
            text="Volver",
            width=250,
            fg_color="gray"
        )
        btn_volver.pack()


if __name__ == "__main__":
    app = RegistrarSalida()
    app.mainloop()