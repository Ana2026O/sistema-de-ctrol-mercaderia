import customtkinter as ctk


class RegistrarIngreso(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configuración ventana
        self.title("Registrar Ingreso")
        self.geometry("900x600")
        self.resizable(False, False)

        # Fondo
        self.configure(fg_color="#E8EEF5")

        # Título
        titulo = ctk.CTkLabel(
            self,
            text="REGISTRAR INGRESO",
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

        # Proveedor
        lbl_proveedor = ctk.CTkLabel(
            self,
            text="Proveedor:"
        )
        lbl_proveedor.pack()

        self.cmb_proveedor = ctk.CTkComboBox(
            self,
            values=[
                "Distribuidora Norte",
                "Distribuidora Sur",
                "Proveedor A"
            ],
            width=300
        )
        self.cmb_proveedor.pack(pady=5)

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

        # Comprobante
        lbl_comprobante = ctk.CTkLabel(
            self,
            text="Número de comprobante:"
        )
        lbl_comprobante.pack()

        self.txt_comprobante = ctk.CTkEntry(
            self,
            width=300
        )
        self.txt_comprobante.pack(pady=5)

        # Botón Guardar
        btn_guardar = ctk.CTkButton(
            self,
            text="Guardar Ingreso",
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
    app = RegistrarIngreso()
    app.mainloop()