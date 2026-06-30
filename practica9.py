import time, os, msvcrt

def mostrar_menu():
    print("""=== MENÚ PRINCIPAL ===
1. Registrar reserva
2. Buscar reserva por código
3. Eliminar reserva
4. Actualizar seguimiento del pago
5. Mostrar reservas
6. Salir""")

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción deseada (1-6): "))
            if 1 <= opc <= 6:
                return opc
            else:
                print("Error: debe ingresar una opción entre 1 y 6")
        except:
            print("Error: debe ingresar un número entero")

def validar_codigo_reserva(codigo_reserva,reservas):
    if not codigo_reserva.upper().startswith("R"):
        return False, "Error: el código debe comenzar con la letra R"
    elif len(codigo_reserva) != 6:
        return False, "Error: el código debe contener exactamente 6 caracteres"
    elif " " in codigo_reserva:
        return False, "Error: el código no debe contener espacios"
    elif buscar_codigo(codigo_reserva,reservas) >= 0:
        return False, "Error: el código ya existe, intente nuevamente"
    else:
        return True, ""
    
def validar_nombre_cliente(nombre_cliente):
    if not 5 <= len(nombre_cliente) <= 40:
        return False, "Error: el nombre debe tener entre 5 y 40 caracteres"
    elif not nombre_cliente.replace(" ", "").isalpha():
        return False, "Error: el nombre debe contener unicamente letras y espacios"
    else:
        return True, ""
    
def validar_sector_asiento(sector_asiento):
    if not sector_asiento.upper() in("P","G","V"):
        return False, "Error: debe ingresar un sector válido (P, G o V)"
    else:
        return True, ""
    
def validar_cantidad_entradas(cantidad_entradas):
    try:
        cantidad_entradas = int(cantidad_entradas)
        if 1 <= cantidad_entradas <= 10:
            return True, ""
        else:
            return False, "Error: debe ingresar una cantidad entre 1 y 10"
    except:
        return False, "Error: debe ingresar un número entero"
    
def validar_monto_pendiente(monto_pendiente):
    try:
        monto_pendiente = float(monto_pendiente)
        if monto_pendiente >= 0:
            return True, ""
        else:
            return False, "Error: debe ingresar un valor igual o mayor a 0"
    except:
        return False, "Error: debe ingresar una cantidad númerica"

def registrar_reserva(reservas):
    while True:
        codigo_reserva = input("Ingrese el código de reserva: ")
        validar,mensajito = validar_codigo_reserva(codigo_reserva,reservas)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        validar,mensajito = validar_nombre_cliente(nombre_cliente)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        sector_asiento = input("Ingrese el sector (P,G.V): ")
        validar,mensajito = validar_sector_asiento(sector_asiento)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        cantidad_entradas = input("Ingrese la cantidad de entradas: ")
        validar,mensajito = validar_cantidad_entradas(cantidad_entradas)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        monto_pendiente = input("Ingrese la monto pendiente: ")
        validar,mensajito = validar_monto_pendiente(monto_pendiente)
        if validar == True:
            break
        else:
            print(mensajito)
    reserva = {
        "codigo_reserva": codigo_reserva.upper(),
        "nombre_cliente": nombre_cliente.title(),
        "sector_asiento": sector_asiento.upper(),
        "cantidad_entradas": int(cantidad_entradas),
        "monto_pendiente": float(monto_pendiente),
        "seguimiento_pago": False
    }
    reservas.append(reserva)
    print("Reserva registrada exitosamente!")

def buscar_codigo(codigo_reserva,reservas):
    for posicion,reserva in enumerate(reservas):
        if reserva["codigo_reserva"] == codigo_reserva.upper():
            return posicion
    return -1

def eliminar_reserva(codigo_reserva,reservas):
    posicion = buscar_codigo(codigo_reserva,reservas)
    if posicion >= 0:
        reservas.pop(posicion)
        print("Reserva eliminada con éxito!")
    else:
        print("No se pudo eliminar la reserva: no existe o ya fue eliminada")

def actualizar_seguimiento(reservas):
    for reserva in reservas:
        if reserva["monto_pendiente"] >= 15000:
            reserva["seguimiento_pago"] = "Requiere Cobro Urgente"
        else:
            reserva["seguimiento_pago"] = "Cuenta al Día / OK"
    print("Todas las reservas fueron actualizadas")

def mostrar_reservas(reservas):
    for reserva in reservas:
        print("\n------------------------------")
        print("Codigo reserva:", reserva["codigo_reserva"])
        print("Nombre cliente:", reserva["nombre_cliente"])
        print("Sector:", reserva["sector_asiento"])
        print("Cantidad entradas:", reserva["cantidad_entradas"])
        print("Monto pendiente", reserva["monto_pendiente"])
        print("Seguimiento:", reserva["seguimiento_pago"])
        
reservas = []
while True:
    os.system("cls")
    mostrar_menu()
    opcion = validar_opcion()

    if opcion == 1:
        os.system("cls")
        print("******* REGISTRAR RESERVA *******")
        registrar_reserva(reservas)

    elif opcion == 2:
        os.system("cls")
        if len(reservas) == 0:
            print("Aún no hay reservas")
        else:
            print("******* BUSCAR RESERVA *******")
            codigo_reserva = input("Ingrese el código de la reserva a buscar: ")
            posicion = buscar_codigo(codigo_reserva,reservas)
            if posicion == -1:
                print("Reserva no encontrada: no existe o fue eliminada")
            else:
                print("Reserva encontrada en la posición: N°",posicion+1)
                mostrar_reservas([reservas[posicion]])
                print("\n. . . Presione una tecla para volver al menú . . .")
                msvcrt.getch()
                print("Espere unos segundos...")

    elif opcion == 3:
        os.system("cls")
        if len(reservas) == 0:
            print("Aún no hay reservas")
        else:
            print("******* ELIMINAR RESERVA *******")
            codigo_reserva = input("Ingrese el código de la reserva a eliminar: ")
            eliminar_reserva(codigo_reserva,reservas)

    elif opcion == 4:
        os.system("cls")
        if len(reservas) == 0:
            print("Aún no hay reservas")
        else:
            print("******* ACTUALIZACIÓN DE RESERVAS *******")
            actualizar_seguimiento(reservas)

    elif opcion == 5:
        os.system("cls")
        if len(reservas) == 0:
            print("Aún no hay reservas")
        else:
            print("******* RESERVAS REGISTRADAS *******")
            mostrar_reservas(reservas)
            print("\n. . . Presione una tecla para volver al menú . . .")
            msvcrt.getch()
            print("Espere unos segundos...")

    else:
        print("Gracias por utilizar nuestro sistema. ¡Hasta luego!")
        break
    time.sleep(2.5)