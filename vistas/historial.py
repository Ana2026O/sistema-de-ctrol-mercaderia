
import customtkinter as ctk
from tkinter import ttk

from vistas.registrar_ingreso import historial_movimientos


class Historial(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Historial de Movimientos")
        self.geometry("1000x600")
        self.resizable(False, False)

        self.configure(fg_color="#E8EEF5")

        # Título
        titulo = ctk.CTkLabel(
            self,
            text="HISTORIAL DE MOVIMIENTOS",
            font=("Arial", 28, "bold"),
            text_color="#0B3D91"
        )
        titulo.pack(pady=(20, 10))

        # Línea separadora
        linea = ctk.CTkFrame(
            self,
            width=900,
            height=3,
            fg_color="#0B3D91"
        )
        linea.pack(pady=10)

        # Buscar
        ctk.CTkLabel(
            self,
            text="Buscar:"
        ).pack()

        self.txt_buscar = ctk.CTkEntry(
            self,
            width=300
        )
        self.txt_buscar.pack(pady=5)

        btn_buscar = ctk.CTkButton(
            self,
            text="Buscar",
            width=150,
            command=self.buscar_movimientos
        )
        btn_buscar.pack(pady=10)

        # Tabla
        columnas = (
            "Fecha",
            "Tipo",
            "Producto",
            "Cantidad",
            "Proveedor",
            "Comprobante",
            "Motivo"
        )

        self.tabla = ttk.Treeview(
            self,
            columns=columnas,
            show="headings",
            height=12
        )

        # Encabezados
        for col in columnas:
            self.tabla.heading(col, text=col)

        # Anchos
        self.tabla.column("Fecha", width=100)
        self.tabla.column("Tipo", width=80)
        self.tabla.column("Producto", width=150)
        self.tabla.column("Cantidad", width=70)
        self.tabla.column("Proveedor", width=120)
        self.tabla.column("Comprobante", width=130)
        self.tabla.column("Motivo", width=180)

        self.tabla.pack(pady=20)

        # Cargar movimientos
        self.actualizar_tabla()

        # Volver
        btn_volver = ctk.CTkButton(
            self,
            text="Volver",
            width=200,
            fg_color="gray",
            command=self.volver_menu
        )
        btn_volver.pack(pady=15)

    # Actualizar tabla
    def actualizar_tabla(self, movimientos=None):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        if movimientos is None:
            movimientos = historial_movimientos

        for movimiento in movimientos:

            if movimiento["tipo"] == "Ingreso" or movimiento["tipo"] == "Entrada":
                motivo = "—"
            else:
                detalle = movimiento.get("detalle", "—")
                motivo = detalle.replace("Motivo: ", "", 1)

            self.tabla.insert(
                "",
                "end",
                values=(
                    movimiento["fecha"],
                    movimiento["tipo"],
                    movimiento["producto"],
                    movimiento["cantidad"],
                    movimiento.get("proveedor", "—"),
                    movimiento.get("comprobante", "—"),
                    motivo
                )
            )

    # Buscar movimientos
    def buscar_movimientos(self):

        busqueda = self.txt_buscar.get().strip().lower()

        resultados = [
            movimiento
            for movimiento in historial_movimientos
            if busqueda in (
                movimiento["fecha"] + " " +
                movimiento["tipo"] + " " +
                movimiento["producto"] + " " +
                movimiento.get("proveedor", "") + " " +
                movimiento.get("comprobante", "") + " " +
                movimiento.get("detalle", "")
            ).lower()
        ]

        self.actualizar_tabla(resultados)

    # Volver al menú
    def volver_menu(self):

        from vistas.menu_principal import MenuPrincipal

        self.destroy()

        app = MenuPrincipal()
        app.mainloop()


if __name__ == "__main__":
    app = Historial()
    app.mainloop()
