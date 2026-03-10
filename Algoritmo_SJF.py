# SJF-Trabajo mas corto primero
# listprocess = [1,2,3]
# listtimeprocess = [12,3,10]

import random
from operator import itemgetter

procesos = [
    {"id": 1, "tiempo": 12},
    {"id": 2, "tiempo": 3},
    {"id": 3, "tiempo": 10}
]

def addProcess(procesos, id):
    tiempo = random.randint(1, 100)
    procesos.append({"id": id, "tiempo": tiempo})
    print(f"Proceso {id} agregado con tiempo {tiempo}")

def sjf(procesos):
    ordenados = sorted(procesos, key=itemgetter("tiempo"))
    print("\nOrden de ejecución (SJF):")
    for p in ordenados:
        print(f"Proceso {p['id']} - Tiempo {p['tiempo']}")

def menu():
    id_actual = len(procesos)

    while True:
        try:
            print("\n1. Agregar proceso")
            print("2. Ejecutar SJF")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id_actual += 1
                addProcess(procesos, id_actual)

            elif opcion == "2":
                sjf(procesos)

            elif opcion == "3":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")

        except Exception as e:
            print("Ocurrió un error:", e)

menu()