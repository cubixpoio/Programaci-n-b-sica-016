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
