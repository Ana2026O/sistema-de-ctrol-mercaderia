import json
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from pathlib import Path


# RUTAS DE LOS ARCHIVOS
CARPETA_DATOS = Path(__file__).resolve().parent.parent / "datos"
CARPETA_DATOS.mkdir(exist_ok=True)

ARCHIVO_INVENTARIO = CARPETA_DATOS / "inventario.json"
ARCHIVO_HISTORIAL = CARPETA_DATOS / "historial.json"
ARCHIVO_PRODUCTOS = CARPETA_DATOS / "productos.json"
ARCHIVO_PROVEEDORES = CARPETA_DATOS / "proveedores.json"

# DETALLE DEL MOVIMIENTO
class DetalleMovimiento:

    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad


# INVENTARIO
class Inventario:

    def __init__(self):
        self.__existencias = {}

        if ARCHIVO_INVENTARIO.exists():
            with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
                self.__existencias = json.load(archivo)

    def __guardar(self):
        with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as archivo:
            json.dump(
                self.__existencias,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    def ingresar(self, producto, cantidad):

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        actual = self.__existencias.get(producto, 0)
        self.__existencias[producto] = actual + cantidad
        self.__guardar()

    def retirar(self, producto, cantidad):

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        actual = self.consultar_stock(producto)

        if cantidad > actual:
            raise ValueError(
                f"Stock insuficiente de {producto}. Disponible: {actual}"
            )

        self.__existencias[producto] = actual - cantidad
        self.__guardar()

    def consultar_stock(self, producto):
        return self.__existencias.get(producto, 0)

    def consultar_existencias(self):
        return self.__existencias.copy()


# MOVIMIENTO DE INGRESO
class Ingreso:

    def __init__(self, proveedor, comprobante, detalles):
        self.proveedor = proveedor
        self.comprobante = comprobante
        self.detalles = detalles

    def registrar(self, inventario):

        for detalle in self.detalles:
            inventario.ingresar(
                detalle.producto,
                detalle.cantidad
            )


# INVENTARIO COMPARTIDO
inventario_compartido = Inventario()

# HISTORIAL COMPARTIDO
historial_movimientos = []

if ARCHIVO_HISTORIAL.exists():
    with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as archivo:
        historial_movimientos = json.load(archivo)


# GUARDAR HISTORIAL
def guardar_historial():

    with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as archivo:
        json.dump(
            historial_movimientos,
            archivo,
            indent=4,
            ensure_ascii=False
        )


# PANTALLA REGISTRAR INGRESO
class RegistrarIngreso(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Registrar Ingreso")
        self.geometry("900x650")
        self.resizable(False, False)
        self.configure(fg_color="#E8EEF5")

        self.productos_ingresados = []
        self.inventario = inventario_compartido

        # CARGAR PRODUCTOS
        self.productos_disponibles = []

        if ARCHIVO_PRODUCTOS.exists():
            with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
                self.productos_disponibles = json.load(archivo)

        nombres_productos = [
            producto["nombre"]
            for producto in self.productos_disponibles
        ]

        # TÍTULO
        titulo = ctk.CTkLabel(
            self,
            text="REGISTRAR INGRESO",
            font=("Arial", 28, "bold"),
            text_color="#0B3D91"
        )
        titulo.pack(pady=(15, 5))

        # LÍNEA DECORATIVA
        linea = ctk.CTkFrame(
            self,
            width=800,
            height=3,
            fg_color="#0B3D91"
        )
        linea.pack(pady=10)

        # CONTENEDOR DE LAS DOS COLUMNAS
        contenedor = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        contenedor.pack(fill="x", padx=30, pady=5)

        # COLUMNA IZQUIERDA
        columna_izquierda = ctk.CTkFrame(
            contenedor,
            fg_color="white",
            corner_radius=10
        )
        columna_izquierda.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        # COLUMNA DERECHA
        columna_derecha = ctk.CTkFrame(
            contenedor,
            fg_color="white",
            corner_radius=10
        )
        columna_derecha.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        # DATOS DEL PROVEEDOR
        ctk.CTkLabel(
            columna_izquierda,
            text="DATOS DEL PROVEEDOR",
            font=("Arial", 16, "bold"),
            text_color="#0B3D91"
        ).pack(pady=(15, 10))

        ctk.CTkLabel(
            columna_izquierda,
            text="Proveedor:"
        ).pack()

        # Cargar proveedores guardados.
        proveedores = []

        if ARCHIVO_PROVEEDORES.exists():
            with open(ARCHIVO_PROVEEDORES, "r", encoding="utf-8") as archivo:
                proveedores = json.load(archivo)

        self.cmb_proveedor = ctk.CTkComboBox(
            columna_izquierda,
            values=proveedores,
            width=300,
            state="normal"
        )
        self.cmb_proveedor.pack(pady=5)
        self.cmb_proveedor.set("")
        
        btn_agregar_proveedor = ctk.CTkButton(
            columna_izquierda,
            text="Agregar proveedor",
            width=200,
            command=self.agregar_proveedor
        )
        btn_agregar_proveedor.pack(pady=5)

        ctk.CTkLabel(
            columna_izquierda,
            text="Tipo de comprobante:"
        ).pack()

        self.cmb_tipo_comprobante = ctk.CTkComboBox(
            columna_izquierda,
            values=[
                "Factura",
                "Remito",
                "Otro comprobante"
            ],
            width=300
        )
        self.cmb_tipo_comprobante.pack(pady=5)

        ctk.CTkLabel(
            columna_izquierda,
            text="Número de comprobante:"
        ).pack()

        self.txt_numero_comprobante = ctk.CTkEntry(
            columna_izquierda,
            width=300,
            placeholder_text="Ejemplo: 001"
        )
        self.txt_numero_comprobante.pack(pady=5)

        # DATOS DEL PRODUCTO
        ctk.CTkLabel(
            columna_derecha,
            text="DATOS DEL PRODUCTO",
            font=("Arial", 16, "bold"),
            text_color="#0B3D91"
        ).pack(pady=(15, 10))

        ctk.CTkLabel(
            columna_derecha,
            text="Producto:"
        ).pack()

        self.cmb_producto = ctk.CTkComboBox(
            columna_derecha,
            values=nombres_productos,
            width=300,
            command=self.mostrar_categoria_subcategoria
        )
        self.cmb_producto.pack(pady=5)

        ctk.CTkLabel(
            columna_derecha,
            text="Categoría:"
        ).pack()

        self.txt_categoria = ctk.CTkEntry(
            columna_derecha,
            width=300,
            state="readonly"
        )
        self.txt_categoria.pack(pady=5)

        ctk.CTkLabel(
            columna_derecha,
            text="Subcategoría:"
        ).pack()

        self.txt_subcategoria = ctk.CTkEntry(
            columna_derecha,
            width=300,
            state="readonly"
        )
        self.txt_subcategoria.pack(pady=5)

        ctk.CTkLabel(
            columna_derecha,
            text="Cantidad:"
        ).pack()

        self.txt_cantidad = ctk.CTkEntry(
            columna_derecha,
            width=300,
            placeholder_text="Ingrese cantidad"
        )
        self.txt_cantidad.pack(pady=5)

        # BOTÓN AGREGAR PRODUCTO
        btn_agregar = ctk.CTkButton(
            columna_derecha,
            text="Agregar producto",
            width=250,
            command=self.agregar_producto
        )
        btn_agregar.pack(pady=10)

        # LISTA DE PRODUCTOS
        lbl_lista = ctk.CTkLabel(
            self,
            text="PRODUCTOS DEL INGRESO",
            font=("Arial", 15, "bold"),
            text_color="#0B3D91"
        )
        lbl_lista.pack(pady=(10, 0))

        self.txt_lista = ctk.CTkTextbox(
            self,
            width=750,
            height=90
        )
        self.txt_lista.pack(pady=5)

        self.txt_lista.configure(state="disabled")

        # BOTONES INFERIORES
        contenedor_botones = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        contenedor_botones.pack(pady=10)

        btn_guardar = ctk.CTkButton(
            contenedor_botones,
            text="Guardar Ingreso",
            width=200,
            command=self.guardar_ingreso
        )
        btn_guardar.pack(side="left", padx=10)

        btn_volver = ctk.CTkButton(
            contenedor_botones,
            text="Volver",
            width=200,
            fg_color="gray",
            command=self.volver_menu
        )
        btn_volver.pack(side="left", padx=10)

    # MOSTRAR CATEGORÍA Y SUBCATEGORÍA
    def mostrar_categoria_subcategoria(self, producto_seleccionado):

        for producto in self.productos_disponibles:

            if producto["nombre"] == producto_seleccionado:

                self.txt_categoria.configure(state="normal")
                self.txt_categoria.delete(0, "end")
                self.txt_categoria.insert(0, producto["categoria"])
                self.txt_categoria.configure(state="readonly")

                self.txt_subcategoria.configure(state="normal")
                self.txt_subcategoria.delete(0, "end")
                self.txt_subcategoria.insert(0, producto["subcategoria"])
                self.txt_subcategoria.configure(state="readonly")

                break

    # AGREGAR PRODUCTO a la lista
    def agregar_producto(self):

        producto = self.cmb_producto.get().strip()
        cantidad = self.txt_cantidad.get().strip()

        if not producto:
            messagebox.showwarning(
                "Dato faltante",
                "Seleccione un producto."
            )
            return

        try:
            cantidad = int(cantidad)

            if cantidad <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Cantidad incorrecta",
                "Ingrese una cantidad entera mayor que cero."
            )
            return

        detalle = DetalleMovimiento(producto, cantidad)

        self.productos_ingresados.append(detalle)

        self.actualizar_lista()

        self.cmb_producto.set("")
        self.txt_cantidad.delete(0, "end")

        self.txt_categoria.configure(state="normal")
        self.txt_categoria.delete(0, "end")
        self.txt_categoria.configure(state="readonly")

        self.txt_subcategoria.configure(state="normal")
        self.txt_subcategoria.delete(0, "end")
        self.txt_subcategoria.configure(state="readonly")

            # Agregar y guardar proveedor.
    
    # Agregar y guardar proveedor.
    def agregar_proveedor(self):

        proveedor = self.cmb_proveedor.get().strip()

        if not proveedor:
            messagebox.showwarning("Atención", "Escriba un proveedor.")
            return

        proveedores = []

        if ARCHIVO_PROVEEDORES.exists():
            with open(ARCHIVO_PROVEEDORES, "r", encoding="utf-8") as archivo:
                proveedores = json.load(archivo)

        if proveedor in proveedores:
            messagebox.showwarning("Atención", "El proveedor ya existe.")
            return

        proveedores.append(proveedor)

        with open(ARCHIVO_PROVEEDORES, "w", encoding="utf-8") as archivo:
            json.dump(proveedores, archivo, indent=4, ensure_ascii=False)

        self.cmb_proveedor.configure(values=proveedores)
        self.cmb_proveedor.set(proveedor)

        messagebox.showinfo("Correcto", "Proveedor guardado.")
      


    # ACTUALIZAR LISTA
    def actualizar_lista(self):

        self.txt_lista.configure(state="normal")
        self.txt_lista.delete("1.0", "end")

        for detalle in self.productos_ingresados:
            self.txt_lista.insert(
                "end",
                f"{detalle.producto} - Cantidad: {detalle.cantidad}\n"
            )

        self.txt_lista.configure(state="disabled")

    # GUARDAR INGRESO
    def guardar_ingreso(self):

        proveedor = self.cmb_proveedor.get().strip()
        tipo_comprobante = self.cmb_tipo_comprobante.get().strip()
        numero_comprobante = self.txt_numero_comprobante.get().strip()

        prefijos = {
            "Factura": "FAC",
            "Remito": "REM",
            "Otro comprobante": ""
        }

        prefijo = prefijos.get(tipo_comprobante)

        if prefijo:
            comprobante = f"{prefijo}-{numero_comprobante}"
        else:
            comprobante = numero_comprobante

        if (
            not proveedor
            or tipo_comprobante not in prefijos
            or not numero_comprobante.isdigit()
        ):
            messagebox.showwarning(
                "Datos incompletos",
                "Seleccione un proveedor e ingrese el comprobante."
            )
            return

        if not self.productos_ingresados:
            messagebox.showwarning(
                "Sin productos",
                "Debe agregar al menos un producto."
            )
            return

        ingreso = Ingreso(
            proveedor,
            comprobante,
            self.productos_ingresados.copy()
        )

        ingreso.registrar(self.inventario)

        for detalle in self.productos_ingresados:
            historial_movimientos.append({
                "tipo": "Ingreso",
                "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "producto": detalle.producto,
                "cantidad": detalle.cantidad,
                "proveedor": proveedor,
                "comprobante": comprobante,
                "detalle": f"Proveedor: {proveedor} - Comprobante: {comprobante}"
            })

        guardar_historial()

        messagebox.showinfo(
            "Ingreso registrado",
            "El ingreso se registró correctamente."
        )

        for detalle in self.productos_ingresados:
            stock = self.inventario.consultar_stock(detalle.producto)
            print(detalle.producto, "Stock:", stock)

        self.productos_ingresados.clear()
        self.actualizar_lista()

        self.cmb_proveedor.set("")
        self.cmb_tipo_comprobante.set("")
        self.txt_numero_comprobante.delete(0, "end")

        self.cmb_producto.set("")
        self.txt_cantidad.delete(0, "end")

        self.txt_categoria.configure(state="normal")
        self.txt_categoria.delete(0, "end")
        self.txt_categoria.configure(state="readonly")

        self.txt_subcategoria.configure(state="normal")
        self.txt_subcategoria.delete(0, "end")
        self.txt_subcategoria.configure(state="readonly")

    # VOLVER AL MENÚ PRINCIPAL
    def volver_menu(self):

        from vistas.menu_principal import MenuPrincipal

        self.destroy()

        app = MenuPrincipal()
        app.mainloop()


# EJECUCIÓN DIRECTA
if __name__ == "__main__":
    app = RegistrarIngreso()
    app.mainloop()