# 📋Tarea Semana 15 Lista de Tareas - Aplicación GUI con Tkinter

## 🎯 Objetivo del Proyecto

Desarrollar una aplicación de escritorio **interactiva de Lista de Tareas (To-Do List)** utilizando **Tkinter**, respetando estrictamente la **arquitectura modular por capas** (Modelo, Servicio y UI). 

La aplicación permite gestionar tareas diarias de forma fluida: agregar, marcar como completadas (con cambio visual) y eliminar tareas, manejando eventos de teclado y ratón.

## ✨ Características Principales

- ✅ Agregar nuevas tareas con el botón o presionando **Enter** en el campo de texto.
- ✅ Marcar tareas como completadas (cambia a color gris y se tacha el texto).
- ✅ Eliminar tareas seleccionadas.
- ✅ Soporte para **doble clic** sobre una tarea para marcarla como completada (funcionalidad extra).
- ✅ Interfaz limpia y responsive con **Treeview**.
- ✅ Arquitectura limpia separando lógica de negocio de la interfaz gráfica.
- ✅ Empaquetado como ejecutable (.exe) sin consola usando **PyInstaller**.

## 🏗️ Estructura del Proyecto

lista_tareas_app/
├── main.py                  # Orquestador y punto de arranque
├── modelos/
│   └── tarea.py             # Clase Tarea (Modelo)
├── servicios/
│   └── tarea_servicio.py    # Lógica de negocio (Servicio)
└── ui/
└── app_tkinter.py       # Interfaz gráfica y manejo de eventos