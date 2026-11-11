
import customtkinter as ctk
from tkinter import messagebox


# Clase Administrador: lógica de autenticación
class Administrador:

    def __init__(self, usuario, password):
        self.__usuario = usuario
        self.__password = password

    def validar_credenciales(self, usuario, password):
        return (
            usuario == self.__usuario
            and password == self.__password
        )


# Pantalla de inicio de sesión
class LoginView(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Control de Mercadería")
        self.geometry("900x600")
        self.resizable(False, False)
        self.configure(fg_color="#001F6B")

        # Administrador de prueba
        self.administrador = Administrador("admin", "1234")

        # Título
        titulo = ctk.CTkLabel(
            self,
            text="Sistema de Control de Mercadería",
            font=("Arial", 28, "bold"),
            text_color="white"
        )
        titulo.pack(pady=40)

        # Separador
        linea = ctk.CTkFrame(
            self,
            width=800,
            height=4,
            fg_color="white"
        )
        linea.pack(pady=(0, 30))

        # Usuario
        lbl_usuario = ctk.CTkLabel(
            self,
            text="Usuario:",
            font=("Arial", 18, "bold"),
            text_color="white"
        )
        lbl_usuario.pack(pady=(10, 5))

        self.txt_usuario = ctk.CTkEntry(
            self,
            width=300,
            height=40,
            placeholder_text="Ingrese su usuario"
        )
        self.txt_usuario.pack()

        # Contraseña
        lbl_password = ctk.CTkLabel(
            self,
            text="Contraseña:",
            font=("Arial", 18, "bold"),
            text_color="white"
        )
        lbl_password.pack(pady=(20, 5))

        self.txt_password = ctk.CTkEntry(
            self,
            width=300,
            height=40,
            placeholder_text="Ingrese su contraseña",
            show="*"
        )
        self.txt_password.pack()

        # Botón ingresar
        btn_ingresar = ctk.CTkButton(
            self,
            text="Ingresar",
            width=220,
            height=45,
            font=("Arial", 18, "bold"),
            command=self.iniciar_sesion
        )
        btn_ingresar.pack(pady=30)

        # Credenciales de prueba
        lbl_info = ctk.CTkLabel(
            self,
            text="Usuario: admin    |    Contraseña: 1234",
            font=("Arial", 14),
            text_color="white"
        )
        lbl_info.pack()

    def iniciar_sesion(self):

        usuario = self.txt_usuario.get().strip()
        password = self.txt_password.get()

        if not usuario or not password:
            messagebox.showwarning(
                "Datos incompletos",
                "Ingrese usuario y contraseña."
            )
            return

        if self.administrador.validar_credenciales(usuario, password):

            messagebox.showinfo(
                "Acceso correcto",
                "Bienvenido al sistema."
            )

            from vistas.menu_principal import MenuPrincipal

            self.destroy()

            app = MenuPrincipal()
            app.mainloop()
            
        else:
            messagebox.showerror(
                "Error de acceso",
                "Usuario o contraseña incorrectos."
            )


if __name__ == "__main__":
    app = LoginView()
    app.mainloop()
