import customtkinter as ctk


class MenuPrincipal(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("Panel Principal")
        self.geometry("900x600")
        self.resizable(False, False)

        # Color de fondo
        self.configure(fg_color="#E8EEF5")

        # Título
        titulo = ctk.CTkLabel(
            self,
            text="PANEL DE CONTROL",
            font=("Arial", 30, "bold"),
            text_color="#0B3D91"
        )
        titulo.pack(pady=(25, 5))

        # Subtítulo
        subtitulo = ctk.CTkLabel(
            self,
            text="Sistema de Recepción y Salida de Mercadería",
            font=("Arial", 15)
        )
        subtitulo.pack()

        # Línea separadora
        linea = ctk.CTkFrame(
            self,
            width=800,
            height=3,
            fg_color="#0B3D91"
        )
        linea.pack(pady=20)

        # Botones
        self.crear_boton("Registrar Ingreso")
        self.crear_boton("Registrar Salida")
        self.crear_boton("Consultar Stock")
        self.crear_boton("Historial")
        self.crear_boton("Gestionar Productos")
        self.crear_boton("Categorías y Subcategorías")

        # Salir
        btn_salir = ctk.CTkButton(
            self,
            text="Salir",
            width=320,
            height=45,
            fg_color="#B22222",
            hover_color="#8B0000",
            command=self.destroy
        )
        btn_salir.pack(pady=25)

    def crear_boton(self, texto):

        boton = ctk.CTkButton(
            self,
            text=texto,
            width=320,
            height=45,
            font=("Arial", 14, "bold")
        )

        boton.pack(pady=8)


if __name__ == "__main__":
    app = MenuPrincipal()
    app.mainloop()