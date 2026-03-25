from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTkinter

if __name__ == "__main__":
    servicio = TareaServicio()
    app = AppTkinter(servicio)
    app.ejecutar()