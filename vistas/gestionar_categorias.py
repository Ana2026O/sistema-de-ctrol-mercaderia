import json
import customtkinter as ctk
from tkinter import ttk, messagebox
from tkinter import ttk
from pathlib import Path

CARPETA_DATOS = Path(__file__).resolve().parent.parent / "datos"
CARPETA_DATOS.mkdir(exist_ok=True)

ARCHIVO_CATEGORIAS = CARPETA_DATOS / "categorias.json"
class GestionarCategorias(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestionar Categorías")
        self.geometry("950x700")
        self.resizable(False, False)

        self.configure(fg_color="#E8EEF5")

 #para recuperar datos json de categorias y subcategorias
        if ARCHIVO_CATEGORIAS.exists():
            with open(ARCHIVO_CATEGORIAS, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        else:
            datos = {
                "categorias": [
                    [1, "Gaseosas"],
                    [2, "Jugos"],
                    [3, "Agua"]
                ],
                "subcategorias": [
                    [1, "Cola", "Gaseosas"],
                    [2, "Lima-Limón", "Gaseosas"],
                    [3, "Naranja", "Jugos"]
                ]
            }

        # Título
        titulo = ctk.CTkLabel(
            self,
            text="GESTIONAR CATEGORÍAS Y SUBCATEGORÍAS",
            font=("Arial", 24, "bold"),
            text_color="#0B3D91"
        )
        titulo.pack(pady=(20, 10))

        # Línea
        linea = ctk.CTkFrame(
            self,
            width=850,
            height=3,
            fg_color="#0B3D91"
        )

        linea.pack(pady=10)

        # Categoría

        ctk.CTkLabel(
            self,
            text="Categoría:"
        ).pack()

        self.txt_categoria = ctk.CTkEntry(
            self,
            width=300
        )
        self.txt_categoria.pack(pady=5)

        btn_categoria = ctk.CTkButton(
            self,
            text="Registrar Categoría",
            width=250,
            command=self.registrar_categoria
        )
        btn_categoria.pack(pady=10)

        # Subcategoría

        ctk.CTkLabel(
            self,
            text="Subcategoría:"
        ).pack()

        self.txt_subcategoria = ctk.CTkEntry(
            self,
            width=300
        )
        self.txt_subcategoria.pack(pady=5)

        ctk.CTkLabel(
            self,
            text="Categoría asociada:"
        ).pack()

        self.cmb_categoria = ctk.CTkComboBox(
            self,
            values=[
                "Gaseosas",
                "Jugos",
                "Agua"
            ],
            width=300
        )

        self.cmb_categoria.pack(pady=5)

        btn_subcategoria = ctk.CTkButton(
            self,
            text="Registrar Subcategoría",
            width=250,
            command=self.registrar_subcategoria
        )
        btn_subcategoria.pack(pady=15)

        # Tabla categorías

        ctk.CTkLabel(
            self,
            text="Categorías Registradas",
            font=("Arial", 16, "bold")
        ).pack()

        self.tabla_cat = ttk.Treeview(
            self,
            columns=("ID", "Categoria"),
            show="headings",
            height=4
        )

        self.tabla_cat.heading("ID", text="ID")
        self.tabla_cat.heading("Categoria", text="Categoría")

        self.tabla_cat.pack(pady=10)

        for categoria in datos["categorias"]:
            self.tabla_cat.insert("", "end", values=categoria)

        self.cmb_categoria.configure(
            values=[c[1] for c in datos["categorias"]]
        )

        # Tabla subcategorías

        ctk.CTkLabel(
            self,
            text="Subcategorías Registradas",
            font=("Arial", 16, "bold")
        ).pack()

        self.tabla_sub = ttk.Treeview(
            self,
            columns=(
                "ID",
                "Subcategoria",
                "Categoria"
            ),
            show="headings",
            height=4
        )

        self.tabla_sub.heading("ID", text="ID")
        self.tabla_sub.heading(
            "Subcategoria",
            text="Subcategoría"
        )
        self.tabla_sub.heading(
            "Categoria",
            text="Categoría"
        )

        self.tabla_sub.pack(pady=10)

        for subcategoria in datos["subcategorias"]:
            self.tabla_sub.insert("", "end", values=subcategoria)


        btn_modificar = ctk.CTkButton(
            self,
            text="Modificar",
            width=180,
            command=self.modificar
        )
        
        btn_modificar.pack(pady=5)

        btn_eliminar = ctk.CTkButton(
            self,
            text="Eliminar",
            width=180,
            fg_color="#B22222",
            hover_color="#8B0000",
            command=self.eliminar
        )
        btn_eliminar.pack(pady=5)

        btn_volver = ctk.CTkButton(
            self,
            text="Volver",
            width=180,
            fg_color="gray"
        )
        btn_volver.pack(pady=10)

    def registrar_categoria(self):

        nombre = self.txt_categoria.get().strip()

        if not nombre:
            messagebox.showwarning(
                "Datos incompletos",
                "Ingrese una categoría."
            )
            return

        numero = len(self.tabla_cat.get_children()) + 1

        self.tabla_cat.insert(
            "",
            "end",
            values=(numero, nombre)
        )

        categorias = [
            self.tabla_cat.item(fila)["values"][1]
            for fila in self.tabla_cat.get_children()
        ]

        self.cmb_categoria.configure(values=categorias)
        self.txt_categoria.delete(0, "end")
        self.guardar_datos()

    def registrar_subcategoria(self):
        nombre = self.txt_subcategoria.get().strip()
        categoria = self.cmb_categoria.get().strip()

        if not nombre or not categoria:
            messagebox.showwarning(
                "Datos incompletos",
                "Complete los campos."
            )
            return

        numero = len(self.tabla_sub.get_children()) + 1

        self.tabla_sub.insert(
            "",
            "end",
            values=(numero, nombre, categoria)
        )

        self.txt_subcategoria.delete(0, "end")

        messagebox.showinfo(
            "Correcto",
            "Subcategoría registrada."
        )
        self.guardar_datos()

    def guardar_datos(self):
        datos = {
            "categorias": [
                self.tabla_cat.item(fila)["values"]
                for fila in self.tabla_cat.get_children()
            ],
            "subcategorias": [
                self.tabla_sub.item(fila)["values"]
                for fila in self.tabla_sub.get_children()
            ]
        }

        with open(ARCHIVO_CATEGORIAS, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
     
    def modificar(self):

        
        seleccionado = self.tabla_cat.selection()
        seleccionado_sub = self.tabla_sub.selection()

        if not seleccionado and not seleccionado_sub:
            messagebox.showwarning(
                "Modificar registro",
                "Seleccione una categoría o subcategoría para modificar."
            )
            return

        if seleccionado:
            fila = seleccionado[0]
            valores = self.tabla_cat.item(fila)["values"]

            nuevo = ctk.CTkInputDialog(
                text="Ingrese el nuevo nombre de la categoría:",
                title="Modificar categoría"
            ).get_input()

            if not nuevo or not nuevo.strip():
                return

            anterior = valores[1]
            nuevo = nuevo.strip()

            self.tabla_cat.item(fila, values=(valores[0], nuevo))

            for sub in self.tabla_sub.get_children():
                datos = self.tabla_sub.item(sub)["values"]

                if datos[2] == anterior:
                    self.tabla_sub.item(
                        sub,
                        values=(datos[0], datos[1], nuevo)
                    )

            self.cmb_categoria.configure(
                values=[
                    self.tabla_cat.item(f)["values"][1]
                    for f in self.tabla_cat.get_children()
                ]
            )

        else:
            fila = seleccionado_sub[0]
            valores = self.tabla_sub.item(fila)["values"]

            nuevo = ctk.CTkInputDialog(
                text="Ingrese el nuevo nombre de la subcategoría:",
                title="Modificar subcategoría"
            ).get_input()

            if not nuevo or not nuevo.strip():
                return

            self.tabla_sub.item(
                fila,
                values=(valores[0], nuevo.strip(), valores[2])
            )

        self.guardar_datos()
        messagebox.showinfo("Correcto", "Registro modificado.")  

    def eliminar(self):

        seleccionado = self.tabla_cat.selection()

        if seleccionado:
            valores = self.tabla_cat.item(seleccionado[0])["values"]
            categoria = valores[1]

            # Verificamos si tiene subcategorías
            for fila in self.tabla_sub.get_children():
                datos = self.tabla_sub.item(fila)["values"]

                if datos[2] == categoria:
                    messagebox.showwarning(
                        "Aviso",
                        "No se puede eliminar: tiene subcategorías asociadas."
                    )
                    return

            self.tabla_cat.delete(seleccionado[0])

        else:
            seleccionado = self.tabla_sub.selection()

            if not seleccionado:
                messagebox.showwarning("Aviso", "Seleccione un registro.")
                return

            self.tabla_sub.delete(seleccionado[0])

        self.guardar_datos()

        messagebox.showinfo("Correcto", "Registro eliminado.")


if __name__ == "__main__":
    app = GestionarCategorias()
    app.mainloop()