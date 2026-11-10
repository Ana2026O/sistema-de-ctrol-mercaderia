import customtkinter as ctk


# Ventana principal de acceso al sistema
class LoginView(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("Control de Mercadería")
        self.geometry("900x600")

        # Color de fondo
        self.configure(fg_color="#001F6B")
        # Título principal
        titulo = ctk.CTkLabel(
        self,
        text="Sistema de Control de Mercadería",
        font=("Arial", 28, "bold"),
        text_color="white"
        )

        titulo.pack(pady=40)

       # Línea separadora
        linea = ctk.CTkFrame(
        self,
        width=800,
        height=4,
        fg_color="white"
        )

        linea.pack(pady=(0, 30))
        # Etiqueta Usuario
        lbl_usuario = ctk.CTkLabel(
            self,
            text="Usuario:",
            font=("Arial", 18, "bold"),
            text_color="white"
        )

        lbl_usuario.pack(pady=(20, 5))

        # Campo de texto Usuario
        self.txt_usuario = ctk.CTkEntry(
        self,
        width=300,
        height=40,
        placeholder_text="Ingrese su usuario"
        )

        self.txt_usuario.pack()

    # Etiqueta Contraseña
        lbl_password = ctk.CTkLabel(
        self,
        text="Contraseña:",
        font=("Arial", 18, "bold"),
        text_color="white"
        )

        lbl_password.pack(pady=(20, 5))