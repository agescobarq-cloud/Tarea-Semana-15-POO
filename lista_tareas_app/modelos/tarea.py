class Tarea:
    def __init__(self, id: int, descripcion: str, completado: bool = False):
        self.id = id
        self.descripcion = descripcion
        self.completado = completado

    def marcar_completada(self):
        self.completado = True

    def __str__(self):
        estado = "[Hecho]" if self.completado else "[Pendiente]"
        return f"{estado} {self.descripcion}"