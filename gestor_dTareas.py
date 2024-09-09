# FASE 1
import datetime

# Creamos la lista para almacenar las tareas
Tareas = []

def menu():
    print("\n--- Menú Gestor de Tareas ---")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def agregar():
    tarea = input("Escribe la tarea: ")
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    Tareas.append(tarea + " (se creó el " + fecha + ")")
    print("Tarea agregada.")

def ver():
    if len(Tareas) == 0:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(Tareas):
            print(f"{i + 1}. {tarea}")

def eliminar_tarea():
    ver()
    if len(Tareas) > 0:
        try:
            num = int(input("Número de tarea a eliminar: ")) - 1
            if 0 <= num < len(Tareas):
                Tareas.pop(num)
                print("Tarea eliminada.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Bucle principal
while True:
    menu()
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        agregar()
    elif opcion == "2":
        ver()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción no válida")

#FASE 2
import datetime


class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.fecha_creacion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        return f"{self.descripcion} (creada el {self.fecha_creacion})"

tareas = []  
etiquetas = set()  

def menu():
    print("\n--- Menú Gestor de Tareas ---")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Ver etiquetas")
    print("5. Salir")

def agregar():
    descripcion = input("Escribe la tarea: ")
    tarea = Tarea(descripcion)
    tareas.append(tarea)
    
    etiqueta = input("Escribe una etiqueta para la tarea (opcional): ")
    if etiqueta:
        etiquetas.add(etiqueta)
    
    print("Tarea agregada.")

def ver():
    if not tareas:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def eliminar_tarea():
    ver()
    if tareas:
        try:
            num = int(input("Número de tarea a eliminar: ")) - 1
            if 0 <= num < len(tareas):
                tareas.pop(num)
                print("Tarea eliminada.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def ver_etiquetas():
    if etiquetas:
        print("\n--- Etiquetas ---")
        for etiqueta in etiquetas:
            print(etiqueta)
    else:
        print("No hay etiquetas.")


def iniciar_gestor():
    while True:
        menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar()
        elif opcion == "2":
            ver()
        elif opcion == "3":
            eliminar_tarea()
        elif opcion == "4":
            ver_etiquetas()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

iniciar_gestor()

