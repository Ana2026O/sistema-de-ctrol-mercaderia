# Importamos la ventana Login
from vistas.login import LoginView

# Punto de entrada del programa
if __name__ == "__main__":

    # Crear ventana Login
    app = LoginView()

    # Mantener la aplicación abierta
    app.mainloop()


from vistas.menu_principal import MenuPrincipal

if __name__ == "__main__":
    app = MenuPrincipal()
    app.mainloop()