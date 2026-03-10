import time
import random

colaClientes = []
numeroCliente = 1

def addCliente():
    global numeroCliente
    colaClientes.append(numeroCliente)
    print(f"Cliente #{numeroCliente} agregado a la lista de espera")
    numeroCliente += 1

def atenderClientes():
    for c in colaClientes :
        tiempoAtencion = random.randint(1,6)
        print(f"Cliente #{c}")
        time.sleep(tiempoAtencion)
        print(f"el cliente {c} tardo {tiempoAtencion} min")

def menu():
    while True:
        try:
            print("\n1. add cliente")
            print("2. atender clientes")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                addCliente()

            elif opcion == "2":
                atenderClientes()
            
            elif opcion == "3":
                print("Saliendo...")
                break

        except Exception as e:
            print("Ocurrió un error:", e)

menu()