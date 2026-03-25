import tkinter as tk
from tkinter import ttk, messagebox
from servicios.tarea_servicio import TareaServicio
from modelos.tarea import Tarea

class AppTkinter:
    def __init__(self, servicio: TareaServicio):
        self.servicio = servicio
        self.root = tk.Tk()
        self.root.title("Lista de Tareas")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")

        # Campo de entrada
        self.entry = tk.Entry(self.root, font=("Arial", 12), width=50)
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", lambda e: self.agregar_tarea())  # Evento Enter

        # Botones
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Añadir Tarea", command=self.agregar_tarea, bg="#4CAF50", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Marcar Completada", command=self.marcar_completada, bg="#2196F3", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self.eliminar_tarea, bg="#f44336", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

        # Lista de tareas con Treeview (mejor que Listbox para estilos)
        self.tree = ttk.Treeview(self.root, columns=("ID", "Descripcion"), show="headings", height=15)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Descripcion", text="Descripción")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Descripcion", width=500)
        self.tree.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Estilo para tareas completadas
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 11))
        style.map("Treeview", foreground=[("selected", "black")])

        # Evento doble clic (opcional/extra)
        self.tree.bind("<Double-1>", lambda e: self.marcar_completada())

        self.actualizar_lista()

    def agregar_tarea(self):
        desc = self.entry.get().strip()
        if not desc:
            messagebox.showwarning("Atención", "Escribe una descripción")
            return
        self.servicio.agregar_tarea(desc)
        self.entry.delete(0, tk.END)
        self.actualizar_lista()

    def marcar_completada(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona una tarea")
            return
        item = self.tree.item(seleccion[0])
        tarea_id = int(item["values"][0])
        if self.servicio.completar_tarea(tarea_id):
            self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona una tarea")
            return
        item = self.tree.item(seleccion[0])
        tarea_id = int(item["values"][0])
        if self.servicio.eliminar_tarea(tarea_id):
            self.actualizar_lista()

    def actualizar_lista(self):
        # Limpiar
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar con estilo visual
        for tarea in self.servicio.listar_tareas():
            tag = "completada" if tarea.completado else "normal"
            desc = f"{tarea.descripcion} [Hecho]" if tarea.completado else tarea.descripcion
            self.tree.insert("", tk.END, values=(tarea.id, desc), tags=(tag,))

        # Configurar tags para cambio visual
        self.tree.tag_configure("completada", foreground="gray", font=("Arial", 11, "overstrike"))

    def ejecutar(self):
        self.root.mainloop()