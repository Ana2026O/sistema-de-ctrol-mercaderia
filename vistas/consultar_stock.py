
import customtkinter as ctk
from tkinter import ttk
from vistas.registrar_ingreso import inventario_compartido


class ConsultarStock(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.inventario = inventario_compartido

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
            width=150,
            command=self.buscar_producto
        )
        btn_buscar.pack(pady=10)

        # Tabla de inventario
        columnas = ("ID", "Producto", "Cantidad")

        self.tabla = ttk.Treeview(
            self,
            columns=columnas,
            show="headings",
            height=10
        )

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Producto", text="Producto")
        self.tabla.heading("Cantidad", text="Cantidad")

        self.tabla.column("ID", width=80, anchor="center")
        self.tabla.column("Producto", width=450)
        self.tabla.column("Cantidad", width=150, anchor="center")

        self.tabla.pack(pady=20)

        # Cargar los productos del inventario
        self.actualizar_tabla()

        btn_volver = ctk.CTkButton(
            self,
            text="Volver",
            width=200,
            fg_color="gray",
            command=self.volver_menu
        )
        btn_volver.pack(pady=15)

    # Método para actualizar la tabla
    def actualizar_tabla(self):

        # Limpiar la tabla
        for elemento in self.tabla.get_children():
            self.tabla.delete(elemento)

        # Obtener las existencias
        existencias = self.inventario.consultar_existencias()

        # Mostrar los productos
        for id_producto, (producto, cantidad) in enumerate(
            existencias.items(), start=1
        ):
            self.tabla.insert(
                "",
                "end",
                values=(id_producto, producto, cantidad)
            )

    def buscar_producto(self):

        # Obtener el texto ingresado
        busqueda = self.txt_buscar.get().strip().lower()

        # Limpiar la tabla
        for elemento in self.tabla.get_children():
            self.tabla.delete(elemento)

        # Consultar el inventario
        existencias = self.inventario.consultar_existencias()

        # Recorrer los productos
        for id_producto, (producto, cantidad) in enumerate(
            existencias.items(), start=1
        ):

            # Comprobar si el nombre coincide con la búsqueda
            if busqueda in producto.lower():

                self.tabla.insert(
                    "",
                    "end",
                    values=(id_producto, producto, cantidad)
                )
        # Volver al menú principal
    def volver_menu(self):

        from vistas.menu_principal import MenuPrincipal

        self.destroy()

        app = MenuPrincipal()
        app.mainloop()

if __name__ == "__main__":
    app = ConsultarStock()
    app.mainloop()
