import customtkinter as ctk
from vistas.registrar_ingreso import RegistrarIngreso
from vistas.registrar_salida import RegistrarSalida
from vistas.consultar_stock import ConsultarStock
from vistas.gestionar_productos import GestionarProductos
from vistas.gestionar_categorias import GestionarCategorias
class MenuPrincipal(ctk.CTk):

    # Abre la pantalla de Registrar Ingreso
    def abrir_ingreso(self):

        # Cerramos el menú actual
        self.destroy()

        # Creamos la pantalla de ingreso
        app = RegistrarIngreso()

        # Mostramos la pantalla
        app.mainloop()

    def abrir_salida(self):

        self.destroy()

        app = RegistrarSalida()
        app.mainloop()

        # Abrir historial de movimientos.
    def abrir_historial(self):

        from vistas.historial import Historial

        self.destroy()

        app = Historial()
        app.mainloop()

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

        # Botones del menú
        self.crear_boton(
            "Registrar Ingreso",
            self.abrir_ingreso
        )

        self.crear_boton(
            "Registrar Salida",
         self.abrir_salida
       )
        self.crear_boton("Consultar Stock",self.abrir_stock)
        
        self.crear_boton("Historial", self.abrir_historial)
        self.crear_boton( "Gestionar Productos", self.abrir_productos)
        self.crear_boton( "Categorías y Subcategorías", self.abrir_categorias)

        # Botón Salir
            
        btn_salir = ctk.CTkButton(
            self,
            text="Salir",
            width=320,
            height=45,
            fg_color="#B22222",
            hover_color="#8B0000",
            command=self.salir_login
        )
        btn_salir.pack(pady=25)

    # Método para crear los botones
    def crear_boton(self, texto, comando=None):

        boton = ctk.CTkButton(
            self,
            text=texto,
            width=320,
            height=45,
            font=("Arial", 14, "bold"),
            command=comando
        )

        boton.pack(pady=8)

    def abrir_stock(self):
        self.destroy()
        app = ConsultarStock()
        app.mainloop()

            # Abre la pantalla de gestionar productos.
    def abrir_productos(self):

        # Cerramos el menú actual.
        self.destroy()

        # Creamos la pantalla de productos.
        app = GestionarProductos()
        app.mainloop()

    def abrir_categorias(self):
        self.destroy()
        app = GestionarCategorias()
        app.mainloop()

    # VOLVER AL MENÚ PRINCIPAL
    def volver_menu(self):

        # Importamos el menú principal.
        from vistas.menu_principal import MenuPrincipal

        # Cerramos la pantalla actual.
        self.destroy()

        # Creamos y mostramos el menú principal.
        app = MenuPrincipal()
        app.mainloop()

    # Volver al Login
    def salir_login(self):
        from vistas.login import LoginView

        self.destroy()

        app = LoginView()
        app.mainloop()

if __name__ == "__main__":
    app = MenuPrincipal()
    app.mainloop()
