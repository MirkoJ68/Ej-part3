def agregar(tareas):
    tarea = input("Ingrese tarea: ")
    fecha = input("Ingrese fecha: ")
    prioridad = input("Ingrese prioridad: ")

    nueva = {
        "Tarea": tarea,
        "Fecha": fecha,
        "Prioridad": prioridad
    }

    tareas.append(nueva)
    print("Tarea agregada")

def mostrar(tareas):
    if len(tareas) == 0:
        print("No hay tareas")
    else:
        i = 1
        for j in tareas:
            print(f'{i} "-" {j["Tarea"]} {j["Fecha"]} {j["Prioridad"]}')
            i = i + 1

tareas = []
opcion = ""

while opcion != "3":
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Salir")

    opcion = input("Opción: ")
    if opcion == "1":
        agregar(tareas)
    elif opcion == "2":
        mostrar(tareas)
    elif opcion == "3":
        print("Salio")
    else:
        print("Opcion incorrecta")