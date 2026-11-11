
import customtkinter as ctk
from tkinter import ttk, messagebox
import json
from pathlib import Path


# RUTA PARA GUARDAR LOS PRODUCTOS.
CARPETA_DATOS = Path(__file__).resolve().parent.parent / "datos"

# Creamos la carpeta si todavía no existe.
CARPETA_DATOS.mkdir(exist_ok=True)

ARCHIVO_PRODUCTOS = CARPETA_DATOS / "productos.json"
ARCHIVO_CATEGORIAS = CARPETA_DATOS / "categorias.json"


# GESTIONAR PRODUCTOS
class GestionarProductos(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestionar Productos")
        self.geometry("900x650")
        self.resizable(False, False)

        self.configure(fg_color="#E8EEF5")

        # Lista de productos.
        self.productos = []

        # Productos iniciales de ejemplo.
        productos_iniciales = [
            {
                "id": 1,
                "nombre": "Coca Cola",
                "categoria": "Gaseosas",
                "subcategoria": "Cola"
            },
            {
                "id": 2,
                "nombre": "Agua",
                "categoria": "Agua",
                "subcategoria": "Mineral"
            },
            {
                "id": 3,
                "nombre": "Sprite",
                "categoria": "Gaseosas",
                "subcategoria": "Lima-Limón"
            }
        ]

        # Recuperamos los productos guardados.
        if ARCHIVO_PRODUCTOS.exists():
            try:
                with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
                    self.productos = json.load(archivo)
            except (json.JSONDecodeError, OSError):
                messagebox.showwarning(
                    "Aviso",
                    "No se pudieron recuperar los productos guardados."
                )
                self.productos = productos_iniciales.copy()
        else:
            self.productos = productos_iniciales.copy()
            self.guardar_productos()

        # Título.
        titulo = ctk.CTkLabel(
            self,
            text="GESTIONAR PRODUCTOS",
            font=("Arial", 28, "bold"),
            text_color="#0B3D91"
        )
        titulo.pack(pady=(20, 10))

        # Línea.
        linea = ctk.CTkFrame(
            self,
            width=800,
            height=3,
            fg_color="#0B3D91"
        )
        linea.pack(pady=10)

        # CARGAR CATEGORÍAS Y SUBCATEGORÍAS
        with open(ARCHIVO_CATEGORIAS, "r", encoding="utf-8") as archivo:
                datos_categorias = json.load(archivo)

        categorias = [fila[1] for fila in datos_categorias["categorias"]]
        subcategorias = [fila[1] for fila in datos_categorias["subcategorias"]]

        # Nombre.
        ctk.CTkLabel(
            self,
            text="Nombre del producto:"
        ).pack()

        self.txt_nombre = ctk.CTkEntry(
            self,
            width=300
        )
        self.txt_nombre.pack(pady=5)

        # Categoría.
        ctk.CTkLabel(
            self,
            text="Categoría:"
        ).pack()

        self.cmb_categoria = ctk.CTkComboBox(
            self,
            values=categorias,
            width=300
     )
        self.cmb_categoria.pack(pady=5)

        # Subcategoría.
        ctk.CTkLabel(
            self,
            text="Subcategoría:"
        ).pack()

        self.cmb_subcategoria = ctk.CTkComboBox(
            self,
            values=subcategorias,
             width=300
        )
        self.cmb_subcategoria.pack(pady=5)

      

        
        # Botón Registrar.
        btn_registrar = ctk.CTkButton(
            self,
            text="Registrar",
            width=200,
            command=self.registrar_producto
        )
        btn_registrar.pack(pady=15)

        # Tabla.
        columnas = (
            "ID",
            "Producto",
            "Categoría",
            "Subcategoría"
        )

        self.tabla = ttk.Treeview(
            self,
            columns=columnas,
            show="headings",
            height=8
        )

        for col in columnas:
            self.tabla.heading(col, text=col)

        self.tabla.column("ID", width=60)
        self.tabla.column("Producto", width=240)
        self.tabla.column("Categoría", width=180)
        self.tabla.column("Subcategoría", width=180)

        self.tabla.pack(pady=20)

        # Al seleccionar un producto cargamos sus datos.
        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_producto
        )

        # Mostramos los productos guardados.
        self.actualizar_tabla()

        # Botón Modificar.
        btn_modificar = ctk.CTkButton(
            self,
            text="Modificar",
            width=180,
            command=self.modificar_producto
        )
        btn_modificar.pack(pady=5)

        # Botón Eliminar.
        btn_eliminar = ctk.CTkButton(
            self,
            text="Eliminar",
            width=180,
            fg_color="#B22222",
            hover_color="#8B0000",
            command=self.eliminar_producto
        )
        btn_eliminar.pack(pady=5)

        # Botón Volver.
        btn_volver = ctk.CTkButton(
            self,
            text="Volver",
            width=180,
            fg_color="gray",
            command=self.volver_menu
        )
        btn_volver.pack(pady=5)

    # GUARDAR PRODUCTOS EN JSON.
    def guardar_productos(self):

        with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
            json.dump(
                self.productos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    # ACTUALIZAR LA TABLA.
    def actualizar_tabla(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for producto in self.productos:
            self.tabla.insert(
                "",
                "end",
                values=(
                    producto["id"],
                    producto["nombre"],
                    producto["categoria"],
                    producto["subcategoria"]
                )
            )

    # REGISTRAR PRODUCTO.
    def registrar_producto(self):

        nombre = self.txt_nombre.get().strip()
        categoria = self.cmb_categoria.get().strip()
        subcategoria = self.cmb_subcategoria.get().strip()

        if not nombre or not categoria or not subcategoria:
            messagebox.showwarning(
                "Datos incompletos",
                "Complete todos los campos."
            )
            return

        # Generamos un ID automático.
        nuevo_id = max(
            [producto["id"] for producto in self.productos],
            default=0
        ) + 1

        nuevo_producto = {
            "id": nuevo_id,
            "nombre": nombre,
            "categoria": categoria,
            "subcategoria": subcategoria
        }

        self.productos.append(nuevo_producto)

        self.guardar_productos()
        self.actualizar_tabla()
        self.limpiar_campos()

        messagebox.showinfo(
            "Producto registrado",
            "El producto se registró correctamente."
        )

    # CARGAR LOS DATOS DEL PRODUCTO SELECCIONADO.
    def seleccionar_producto(self, evento):

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        valores = self.tabla.item(seleccion[0], "values")

        self.txt_nombre.delete(0, "end")
        self.txt_nombre.insert(0, valores[1])

        self.cmb_categoria.set(valores[2])
        self.cmb_subcategoria.set(valores[3])

    # MODIFICAR PRODUCTO.
    def modificar_producto(self):

        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Seleccione un producto de la tabla."
            )
            return

        valores = self.tabla.item(seleccion[0], "values")
        producto_id = int(valores[0])

        nombre = self.txt_nombre.get().strip()
        categoria = self.cmb_categoria.get().strip()
        subcategoria = self.cmb_subcategoria.get().strip()

        if not nombre or not categoria or not subcategoria:
            messagebox.showwarning(
                "Datos incompletos",
                "Complete todos los campos."
            )
            return

        for producto in self.productos:
            if producto["id"] == producto_id:
                producto["nombre"] = nombre
                producto["categoria"] = categoria
                producto["subcategoria"] = subcategoria
                break

        self.guardar_productos()
        self.actualizar_tabla()
        self.limpiar_campos()

        messagebox.showinfo(
            "Producto modificado",
            "El producto se modificó correctamente."
        )

    # ELIMINAR PRODUCTO.
    def eliminar_producto(self):

        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Seleccione un producto de la tabla."
            )
            return

        valores = self.tabla.item(seleccion[0], "values")
        producto_id = int(valores[0])

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Está seguro de eliminar este producto?"
        )

        if not confirmar:
            return

        self.productos = [
            producto
            for producto in self.productos
            if producto["id"] != producto_id
        ]

        self.guardar_productos()
        self.actualizar_tabla()
        self.limpiar_campos()

        messagebox.showinfo(
            "Producto eliminado",
            "El producto se eliminó correctamente."
        )

    # LIMPIAR LOS CAMPOS.
    def limpiar_campos(self):

        self.txt_nombre.delete(0, "end")
        self.cmb_categoria.set("")
        self.cmb_subcategoria.set("")

    # VOLVER AL MENÚ PRINCIPAL.
    def volver_menu(self):

        from vistas.menu_principal import MenuPrincipal

        self.destroy()

        app = MenuPrincipal()
        app.mainloop()


# EJECUCIÓN DIRECTA DE LA PANTALLA.
if __name__ == "__main__":
    app = GestionarProductos()
    app.mainloop()
