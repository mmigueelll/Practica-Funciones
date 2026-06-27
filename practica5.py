def mostrar_menu():
    print("""=== MENU PRINCIPAL ===
1. Registrar reserva
2. Buscar reserva pór código
3. Eliminar reserva
4. Actualizar estados de servicio
5. Mostrar todas las reservas
6. Salir""")

def validar_opcion():
    while True:
        try:
            opc = int(input("ingrese opcion deseada (1-6): "))
            if 1 <= opc <= 6:
                return opc
            else:
                print("Error: ingrese una opción entre 1 y 6")
        except:
            print("Error: ingrese un número entero")

def validar_codigo_reserva(codigo_reserva,reservas):
    if not codigo_reserva.upper().startswith("H"):
        return False, "Error: el código debe empezar con la letra H"
    elif len(codigo_reserva) != 5:
        return False, "Error: el código debe contener 5 caracteres exactamente"
    elif " " in codigo_reserva:
        return False, "Error: el código no debe contener espacios"
    elif buscar_reserva(codigo_reserva,reservas) != -1:
        return False, "Error: el código ya existe, intente nuevamente"
    else:
        return True, ""
    
def validar_numero_habitacion(numero_habitacion):
    if len(numero_habitacion) != 3:
        return False, "Error: debe contener 3 caracteres exactamemte"
    elif " " in numero_habitacion:
        return False, "Error: no debe contener espacios"
    try:
        numero_habitacion = int(numero_habitacion)
        return True, ""
    except:
        return False, "Error: debe ingresar un número entero"

def validar_nombre_pasajero(nombre_pasajero:str):
    if len(nombre_pasajero) < 8:
        return False, "Error: el nombre debe contener al menos 8 caracteres"
    elif nombre_pasajero.isnumeric():
        return False, "Error: el nombre no debe estar formado unicamente por números"
    else:
        return True, ""

def validar_tipo_habitacion(tipo_habitacion):
    if not tipo_habitacion.upper() in("S","D","P"):
        return False, "Error: debe ingresar S, D o P"
    else:
        return True, ""

def validar_noches_estadia(noches_estadia):
    try:
        noches_estadia = int(noches_estadia)
        if 1 <= noches_estadia <= 30:
            return True, ""
        else:
            return False, "Error: debe ingresar un número entre 1 y 30"
    except:
        return False, "Error: debe ingresar un número entero"

def validar_monto_pago(monto_pago):
    try:
        monto_pago = float(monto_pago)
        if monto_pago >= 40000:
            return True, ""
        else:
            return False, "Error: debe ingresar una cantidad igual o mayor a 40000"
    except:
        return False, "Error: debe ingresar un número"
    
def agregar_reserva(reservas):
    while True:
        codigo_reserva = input("Ingrese código de reserva: ")
        validar,mensajito = validar_codigo_reserva(codigo_reserva,reservas)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        numero_habitacion = input("Ingrese el número de habitación: ")
        validar,mensajito = validar_numero_habitacion(numero_habitacion)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        nombre_pasajero = input("Ingrese su nombre: ")
        validar,mensajito = validar_nombre_pasajero(nombre_pasajero)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        tipo_habitacion = input("Ingrese el tipo de habitación (S,D,P): ")
        validar,mensajito = validar_tipo_habitacion(tipo_habitacion)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        noches_estadia = input("Ingrese cantidad de noches: ")
        validar,mensajito = validar_noches_estadia(noches_estadia)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        monto_pago = input("Ingrese el monto a pagar: ")
        validar,mensajito = validar_monto_pago(monto_pago)
        if validar == True:
            break
        else:
            print(mensajito)
    reserva = {
        "codigo_reserva": codigo_reserva.upper(),
        "numero_habitacion": int(numero_habitacion),
        "nombre_pasajero": nombre_pasajero.title(),
        "tipo_habitacion": tipo_habitacion.upper(),
        "noches_estadia": int(noches_estadia),
        "monto_pago": float(monto_pago),
        "estado_servicio": "Pendiente de ingreso"
    }
    reservas.append(reserva)
    print("Reserva registrada con éxito")

def buscar_reserva(codigo_reserva,reservas):
    for posicion,reserva in enumerate(reservas):
        if reserva["codigo_reserva"] == codigo_reserva.upper():
            return posicion
    return -1

def eliminar_reserva(codigo_reserva,reservas):
    posicion = buscar_reserva(codigo_reserva,reservas)
    if posicion < 0:
        print("La reserva no existe o ya fue eliminada")
    else:
        reservas.pop(posicion)
        print("Reserva eliminada con éxito")

def actualizar_estados(reservas):
    for reserva in reservas:
        if reserva["tipo_habitacion"] == "P" or reserva["noches_estadia"] >= 7:
            reserva["estado_servicio"] = "Requiere Servicio VIP"
        else:
            reserva["estado_servicio"] = "Servicio Estándar OK"

def mostrar_reservas(reservas):
    for reserva in reservas:
        print("\n-----------------------")
        print("Código reserva:", reserva["codigo_reserva"])
        print("Número habitación:", reserva["numero_habitacion"])
        print("Nombre pasajero:", reserva["nombre_pasajero"])
        print("Tipo habitación:", reserva["tipo_habitacion"])
        print("Noches estadia:", reserva["noches_estadia"])
        print("Monto a pagar:", reserva["monto_pago"])
        print("Estado del servicio:", reserva["estado_servicio"])

reservas = []
while True:
    mostrar_menu()
    opcion = validar_opcion()
    
    if opcion == 1:
        agregar_reserva(reservas)
    
    elif opcion == 2:
        if len(reservas) == 0:
            print("Aún no hay reservas")
        else:
            codigo_reserva = input("Ingrese codigo a buscar: ")
            posicion = buscar_reserva(codigo_reserva,reservas)
            if posicion == -1:
                print("La reserva no existe o ya fue eliminada")
            else:
                print("La reserva se encuentra en la posición: N°",posicion+1)
                print(reservas[posicion])
    
    elif opcion == 3:
        if len(reservas) == 0:
            print("Aún no hay reservas, no se puede eliminar")
        else:
            codigo_reserva = input("Ingrese codigo a eliminar: ")
            eliminar_reserva(codigo_reserva,reservas)
    
    elif opcion == 4:
        if len(reservas) == 0:
            print("Aún no hay reservas")
        else:
            actualizar_estados(reservas)
            print("Todos los estados fueron actualizados")
    
    elif opcion == 5:
        if len(reservas) == 0:
            print("Aún no hay reservas")
        else:
            mostrar_reservas(reservas)
    
    else:
        print("adiosito")
        break