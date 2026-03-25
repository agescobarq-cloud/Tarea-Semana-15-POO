from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.tareas: list[Tarea] = []
        self.contador_id = 1

    def agregar_tarea(self, descripcion: str) -> Tarea:
        if not descripcion.strip():
            return None
        tarea = Tarea(self.contador_id, descripcion.strip())
        self.tareas.append(tarea)
        self.contador_id += 1
        return tarea

    def completar_tarea(self, tarea_id: int) -> bool:
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                tarea.marcar_completada()
                return True
        return False

    def eliminar_tarea(self, tarea_id: int) -> bool:
        for i, tarea in enumerate(self.tareas):
            if tarea.id == tarea_id:
                del self.tareas[i]
                return True
        return False

    def listar_tareas(self) -> list[Tarea]:
        return self.tareas[:]