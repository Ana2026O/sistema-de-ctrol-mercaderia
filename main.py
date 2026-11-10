# Importamos la ventana Login
from vistas.login import LoginView
from vistas.menu_principal import MenuPrincipal
from vistas.registrar_ingreso import RegistrarIngreso
from vistas.registrar_salida import RegistrarSalida
from vistas.consultar_stock import ConsultarStock
from vistas.gestionar_productos import GestionarProductos
from vistas.gestionar_categorias import GestionarCategorias
from vistas.historial import Historial

# Punto de entrada del programa
if __name__ == "__main__":

    # Crear ventana Login
    app = LoginView()

    # Mantener la aplicación abierta
    app.mainloop()



if __name__ == "__main__":
    app = MenuPrincipal()
    app.mainloop()



if __name__ == "__main__":
    app = RegistrarIngreso()
    app.mainloop()



if __name__ == "__main__":
    app = RegistrarSalida()
    app.mainloop()



if __name__ == "__main__":
    app = ConsultarStock()
    app.mainloop()

    

if __name__ == "__main__":
    app = GestionarProductos()
    app.mainloop()

    

if __name__ == "__main__":
    app = GestionarCategorias()
    app.mainloop()



if __name__ == "__main__":
    app = Historial()
    app.mainloop()
