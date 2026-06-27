def mostrar_menu():
    print("""=== MENÚ PRINCIPAL ===
1. Registrar pasajero
2. Buscar pasajero por código
3. Eliminar pasajero
4. Agregar consumo a la cuenta
5. Actualizar seguimiento de gastos
6. Mostrar pasajeros
7. Salir""")
    
def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción deseada (1-7): "))
            if 1 <= opc <= 7:
                return opc
            else:
                print("Error: debe ingresar una opción entre 1 y 7")
        except:
            print("Error: debe ingresar un número entero")

def validar_codigo_pasajero(codigo_pasajero,pasajeros):
    if not codigo_pasajero.upper().startswith("C"):
        return False, "Error: el código debe empezar con la letra C."
    elif len(codigo_pasajero) != 5:
        return False, "Error: el código debe contener exactamente 5 caracteres"
    elif " " in codigo_pasajero:
        return False, "Error: el código no debe contener espacios"
    elif buscar_pasajero(codigo_pasajero,pasajeros) >= 0:
        return False, "Error: el código ya existe, intente nuevamente"
    else:
        return True, ""

def validar_numero_cabina(numero_cabina):
    if len(numero_cabina) != 3:
        return False, "Error: valor debe contener 3 dígitos"
    if " " in numero_cabina:
        return False, "Error: el valor no debe contener espacios"
    try:
        numero_cabina = int(numero_cabina)
        return True, ""
    except:
        return False, "Error: debe ingresar números enteros"


def validar_nombre_completo(nombre_completo):
    if len(nombre_completo) < 6:
        return False, "Error: el nombre debe contener al menos 6 caracteres"
    elif nombre_completo.isnumeric():
        return False, "Error: el nombre no debe estar conformado únicamente por números"
    else:
        return True, ""
    
def validar_clase_ticket(clase_ticket):
    if clase_ticket.upper() in("E","B","F"):
        return True, ""
    else:
        return False, "Error: la clase debe ser E, B o F"
    
def validar_dias_viaje(dias_viaje):
    try:
        dias_viaje = int(dias_viaje)
        if 1 <= dias_viaje <= 20:
            return True, ""
        else:
            return False, "Error: debe ingresar una cantidad entre 1 y 20"
    except:
        return False, "Error: debe ingresar un número entero"
    
def validar_cuenta_acumulada(cuenta_acumulada):
    try:
        cuenta_acumulada = float(cuenta_acumulada)
        if cuenta_acumulada >= 0:
            return True, ""
        else:
            return False, "Error: debe ingresar una cantidad igual o mayor a 0"
    except:
        return False, "Error: debe ingresar un número"

def agregar_registro(pasajeros):
    while True:
        codigo_pasajero = input("Ingrese código de pasajero: ")
        validar,mensajito = validar_codigo_pasajero(codigo_pasajero,pasajeros)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        numero_cabina = input("Ingrese el número de cabina: ")
        validar,mensajito = validar_numero_cabina(numero_cabina)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        nombre_completo = input("Ingrese su nombre completo: ")
        validar,mensajito = validar_nombre_completo(nombre_completo)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        clase_ticket = input("Ingrese la clase (E,B,F): ")
        validar,mensajito = validar_clase_ticket(clase_ticket)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        dias_viaje = input("Ingrese cantidad de días: ")
        validar,mensajito = validar_dias_viaje(dias_viaje)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        cuenta_acumulada = input("Ingrese la cuenta acumulada: ")
        validar,mensajito = validar_cuenta_acumulada(cuenta_acumulada)
        if validar == True:
            break
        else:
            print(mensajito)
    pasajero = {
        "codigo_pasajero": codigo_pasajero.upper(),
        "numero_cabina": numero_cabina, # sin int para que salga 001 por ejemplo
        "nombre_completo": nombre_completo.title(),
        "clase_ticket": clase_ticket.upper(),
        "dias_viaje": int(dias_viaje),
        "cuenta_acumulada": float(cuenta_acumulada),
        "seguimiento_gastos": False
    }
    pasajeros.append(pasajero)
    print("Se realizó el registro exitosamente!")

def buscar_pasajero(codigo_pasajero,pasajeros):
    for posicion,pasajero in enumerate(pasajeros):
        if pasajero["codigo_pasajero"] == codigo_pasajero.upper():
            return posicion
    return -1

def eliminar_pasajero(codigo_pasajero,pasajeros):
    posicion = buscar_pasajero(codigo_pasajero,pasajeros)
    if posicion >= 0:
        pasajeros.pop(posicion)
        print("Registro eliminado con éxito!")
    else:
        print("El registro no existe o ya fue eliminado")

def agregar_consumo(codigo_pasajero,pasajeros):
    posicion = buscar_pasajero(codigo_pasajero,pasajeros)
    if posicion >= 0:
        while True:
            consumo_extra = input("Ingrese cantidad a agregar: ")
            validar,mensajito = validar_cuenta_acumulada(consumo_extra)
            if validar == True:
                pasajeros[posicion]["cuenta_acumulada"] += float(consumo_extra)
                return
            else:
                print(mensajito)
    else:
        print("El registro no exite")

def actualizar_seguimiento(pasajeros):
    for pasajero in pasajeros:
        if pasajero["clase_ticket"] == "F" or pasajero["cuenta_acumulada"] >= 150000:
            pasajero["seguimiento_gastos"] = "Pasajero VIP / Alto Consumo"
        else:
            pasajero["seguimiento_gastos"] = "Consumo Estándar OK"
    print("Todos los registros fueron actualizados")

def mostrar_pasajeros(pasajeros):
    for pasajero in pasajeros:
        print("\n-------------------------")
        print("Código pasajero:", pasajero["codigo_pasajero"])
        print("Número cabina:", pasajero["numero_cabina"])
        print("Nombre completo:", pasajero["nombre_completo"])
        print("Clase ticket:", pasajero["clase_ticket"])
        print("Días viaje:", pasajero ["dias_viaje"])
        print("Cuenta acumulada:", pasajero["cuenta_acumulada"])
        print("Seguimiento:", pasajero["seguimiento_gastos"])

pasajeros = []
while True:
    mostrar_menu()
    opcion = validar_opcion()

    if opcion == 1:
        agregar_registro(pasajeros)

    elif opcion == 2:
        if len(pasajeros) == 0:
            print("Aún no hay pasajeros registrados")
        else:
            codigo_pasajero = input("Ingrese código de pasajero a buscar: ")
            posicion = buscar_pasajero(codigo_pasajero,pasajeros)
            if posicion == -1:
                print("El registro no existe o ya fue eliminado")
            else:
                print("El pasajero se encuentra en la posición: N°",posicion+1)
                print(pasajeros[posicion])
    
    elif opcion == 3:
        if len(pasajeros) == 0:
            print("Aún no hay pasajeros registrados")
        else:
            codigo_pasajero = input("Ingrese código de pasajero a eliminar: ")
            eliminar_pasajero(codigo_pasajero,pasajeros) 
    elif opcion == 4:
        if len(pasajeros) == 0:
            print("Aún no hay pasajeros registrados")
        else:
            codigo_pasajero = input("Ingrese código a agregar gastos: ")
            agregar_consumo(codigo_pasajero,pasajeros)
    
    elif opcion == 5:
        if len(pasajeros) == 0:
            print("Aún no hay pasajeros registrados")
        else:
            actualizar_seguimiento(pasajeros)
    
    elif opcion == 6:
        if len(pasajeros) == 0:
            print("Aún no hay pasajeros registrados")
        else:
            print("********* PASAJEROS REGISTRADOS *********")
            mostrar_pasajeros(pasajeros)
    
    else:
        print("Adiosito")
        break