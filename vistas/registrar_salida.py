import json
import customtkinter as ctk
from tkinter import messagebox
from datetime import date
from pathlib import Path


# Reutilizamos el detalle, el inventario y el historial del ingreso.
from vistas.registrar_ingreso import (
    DetalleMovimiento,
    inventario_compartido,
    historial_movimientos,
    guardar_historial
)


# CLASE SALIDA
class Salida:

    def __init__(self, motivo, fecha, detalles):
        self.motivo = motivo
        self.fecha = fecha
        self.detalles = detalles

    def registrar(self, inventario):

        # Primero verificamos el stock de TODOS los productos.
        # Esto evita descontar algunos productos si otro no tiene stock.
        cantidades_totales = {}

        for detalle in self.detalles:
            producto = detalle.producto

            cantidades_totales[producto] = (
                cantidades_totales.get(producto, 0)
                + detalle.cantidad
            )

        for producto, cantidad in cantidades_totales.items():

            disponible = inventario.consultar_stock(producto)

            if cantidad > disponible:
                raise ValueError(
                    f"Stock insuficiente de {producto}. "
                    f"Disponible: {disponible}."
                )

        # Si todos tienen stock suficiente, descontamos.
        for detalle in self.detalles:
            inventario.retirar(
                detalle.producto,
                detalle.cantidad
            )


# PANTALLA REGISTRAR SALIDA
class RegistrarSalida(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Utilizamos el mismo inventario que los ingresos.
        self.inventario = inventario_compartido

        # Lista de productos agregados a la salida.
        self.productos_salida = []

        # Configuración de la ventana.
        self.title("Registrar Salida")
        self.geometry("900x650")
        self.resizable(False, False)

        # Fondo.
        self.configure(fg_color="#E8EEF5")

        # Título.
        titulo = ctk.CTkLabel(
            self,
            text="REGISTRAR SALIDA",
            font=("Arial", 28, "bold"),
            text_color="#0B3D91"
        )
        titulo.pack(pady=(15, 5))

        # Línea.
        linea = ctk.CTkFrame(
            self,
            width=800,
            height=3,
            fg_color="#0B3D91"
        )
        linea.pack(pady=10)

        # Producto.
        lbl_producto = ctk.CTkLabel(
            self,
            text="Producto:"
        )
        lbl_producto.pack()

        # Cargar productos desde productos.json.
        carpeta_datos = Path(__file__).resolve().parent.parent / "datos"
        archivo_productos = carpeta_datos / "productos.json"

        productos = []

        if archivo_productos.exists():
            with open(archivo_productos, "r", encoding="utf-8") as archivo:
                datos_productos = json.load(archivo)

            productos = [
                producto["nombre"]
                for producto in datos_productos
            ]      
        

        self.cmb_producto = ctk.CTkComboBox(
            self,
            values=productos,
            width=300
        )
        self.cmb_producto.pack(pady=5)



        # Cantidad.
        lbl_cantidad = ctk.CTkLabel(
            self,
            text="Cantidad:"
        )
        lbl_cantidad.pack()

        self.txt_cantidad = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Ingrese cantidad"
        )
        self.txt_cantidad.pack(pady=5)

        # Motivo.
        lbl_motivo = ctk.CTkLabel(
            self,
            text="Motivo:"
        )
        lbl_motivo.pack()

        self.cmb_motivo = ctk.CTkComboBox(
            self,
            values=[
                "Traslado",
                "Devolución",
                "Mercadería dañada",
                "Otro"
            ],
            width=300,
            command=self.mostrar_otro_motivo
        )
        self.cmb_motivo.pack(pady=5)

        # Campo para especificar otro motivo.
        self.txt_otro_motivo = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Especifique el motivo"
        )

        # Fecha.
        lbl_fecha = ctk.CTkLabel(
            self,
            text="Fecha:"
        )
        lbl_fecha.pack()

        self.txt_fecha = ctk.CTkEntry(
            self,
            width=300
        )
        self.txt_fecha.pack(pady=5)

        self.txt_fecha.insert(
            0,
            date.today().strftime("%d/%m/%Y")
        )

        # Botón agregar producto.
        btn_agregar = ctk.CTkButton(
            self,
            text="Agregar producto",
            width=250,
            command=self.agregar_producto
        )
        btn_agregar.pack(pady=10)

        # Lista de productos.
        lbl_lista = ctk.CTkLabel(
            self,
            text="Productos de la salida:",
            font=("Arial", 14, "bold")
        )
        lbl_lista.pack()

        self.txt_lista = ctk.CTkTextbox(
            self,
            width=500,
            height=100
        )
        self.txt_lista.pack(pady=5)

        self.txt_lista.configure(state="disabled")

        # Botón guardar.
        btn_guardar = ctk.CTkButton(
            self,
            text="Guardar Salida",
            width=250,
            command=self.guardar_salida
        )
        btn_guardar.pack(pady=10)

        # Botón volver.
        btn_volver = ctk.CTkButton(
            self,
            text="Volver",
            width=250,
            fg_color="gray",
            command=self.volver_menu
        )
        btn_volver.pack()

    # Mostrar campo para especificar otro motivo.
    def mostrar_otro_motivo(self, motivo):

        if motivo == "Otro":
            self.txt_otro_motivo.pack(pady=5)
        else:
            self.txt_otro_motivo.pack_forget()

    # Agregar producto a la salida.
    def agregar_producto(self):

        producto = self.cmb_producto.get()
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

        # Creamos el detalle del movimiento.
        detalle = DetalleMovimiento(producto, cantidad)

        self.productos_salida.append(detalle)

        self.actualizar_lista()

        # Limpiamos los campos.
        self.cmb_producto.set("")
        self.txt_cantidad.delete(0, "end")

    # Actualizar lista visual.
    def actualizar_lista(self):

        self.txt_lista.configure(state="normal")
        self.txt_lista.delete("1.0", "end")

        for detalle in self.productos_salida:
            self.txt_lista.insert(
                "end",
                f"{detalle.producto} - Cantidad: {detalle.cantidad}\n"
            )

        self.txt_lista.configure(state="disabled")

    # Guardar salida.
    def guardar_salida(self):

        motivo = self.cmb_motivo.get()
        fecha = self.txt_fecha.get().strip()

        if not motivo or not fecha:
            messagebox.showwarning(
                "Datos incompletos",
                "Seleccione un motivo e ingrese la fecha."
            )
            return

        if motivo == "Otro":
            motivo_especificado = self.txt_otro_motivo.get().strip()

            if not motivo_especificado:
                messagebox.showwarning(
                    "Dato faltante",
                    "Debe especificar el motivo de la salida."
                )
                return

            motivo = motivo_especificado

        if not self.productos_salida:
            messagebox.showwarning(
                "Sin productos",
                "Debe agregar al menos un producto."
            )
            return

        # Creamos el movimiento de salida.
        salida = Salida(
            motivo,
            fecha,
            self.productos_salida.copy()
        )

        try:
            # Validamos y descontamos el inventario.
            salida.registrar(self.inventario)

        except ValueError as error:
            messagebox.showerror(
                "Stock insuficiente",
                str(error)
            )
            return

              # Guardamos cada producto por separado en el historial.
        for detalle in self.productos_salida:
            historial_movimientos.append({
                "fecha": fecha,
                "tipo": "Salida",
                "producto": detalle.producto,
                "cantidad": detalle.cantidad,
                "detalle": f"Motivo: {motivo}"
            })
            
            # Guardamos el historial actualizado en el archivo JSON.
        guardar_historial()

        messagebox.showinfo(
            "Salida registrada",
            "La salida se registró correctamente."
        )

        # Mostramos el stock actualizado.
        for detalle in self.productos_salida:
            stock = self.inventario.consultar_stock(
                detalle.producto
            )
            print(detalle.producto, "Stock:", stock)

        # Limpiamos el formulario.
        self.productos_salida.clear()
        self.actualizar_lista()

        self.cmb_producto.set("")
        self.cmb_motivo.set("")
        self.txt_otro_motivo.delete(0, "end")
        self.txt_fecha.delete(0, "end")
        self.txt_fecha.insert(
            0,
            date.today().strftime("%d/%m/%Y")
        )

    # Volver al menú.
    def volver_menu(self):

        from vistas.menu_principal import MenuPrincipal

        self.destroy()

        app = MenuPrincipal()
        app.mainloop()


if __name__ == "__main__":
    app = RegistrarSalida()
    app.mainloop()
