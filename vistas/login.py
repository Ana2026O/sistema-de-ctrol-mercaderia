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