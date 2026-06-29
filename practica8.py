import os, time, msvcrt

def mostrar_menu():
    print("""=== MENÚ PRINCIPAL ===
1. Registrar envío
2. Buscar envío por código
3. Eliminar envío
4. Agregar costo extra al impuesto
5. Actualizar seguimiento de aduana
6. Mostrar envíos
7. Salir""")
    
def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese la opción deseada (1-7): "))
            if 1 <= opc <= 7:
                return opc
            else:
                print("Error: debe ingresar una opción entre 1 y 7")
        except:
            print("Error: debe ingresar un número entero")

def validar_codigo_envio(codigo_envio,envios):
    if not codigo_envio.upper().startswith("E"):
        return False, "Error: el código debe comenzar con la letra E."
    elif len(codigo_envio) != 5:
        return False, "Error: el código debe contener exactamente 5 caracteres"
    elif " " in codigo_envio:
        return False, "Error: el código no debe contener espacios"
    elif buscar_envios(codigo_envio,envios) >= 0:
        return False, "Error: el código ya existe, intente nuevamente"
    else:
        return True, ""

def validar_codigo_postal(codigo_postal):
    if len(codigo_postal) != 3:
        return False, "Error: el código debe contener exactamente 3 dígitos"
    elif " " in codigo_postal:
        return False, "Error: el código no debe contener espacios"
    try:
        codigo_postal = int(codigo_postal)
        return True, ""
    except:
        return False, "Error: debe ingresar números enteros"

def validar_nombre_destinatario(nombre_destinatario):
    if len(nombre_destinatario) < 6:
        return False, "Error: el nombre debe contener al menos 6 caracteres"
    elif nombre_destinatario.isnumeric():
        return False, "Error: el nombre no debe estar conformado únicamente por números"
    else:
        return True, ""
    
def validar_tipo_transporte(tipo_transporte):
    if not tipo_transporte.upper() in("A","M","T"):
        return False, "Error: debe ingresar un tipo de transporte válido (A, M o T)"
    else:
        return True, ""
    
def validar_peso_kilos(peso_kilos):
    try:
        peso_kilos = int(peso_kilos)
        if 1 <= peso_kilos <= 50:
            return True, ""
        else:
            return False, "Error: debe ingresar una cantidad válida (entre 1 y 50)"
    except:
        return False, "Error: debe ingresar la cantidad en números"
    
def validar_impuesto_acumulado(impuesto_acumulado):
    try:
        impuesto_acumulado = float(impuesto_acumulado)
        if impuesto_acumulado >= 0:
            return True, ""
        else:
            return False, "Error: debe ingresar una cantidad mayor o igual a 0"
    except:
        return False, "Error: debe ingresar la cantidad en números"

def registrar_envio(envios):
    while True:
        codigo_envio = input("Ingrese el código de envío: ")
        validar,mensajito = validar_codigo_envio(codigo_envio,envios)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        codigo_postal = input("Ingrese el código postal: ")
        validar,mensajito = validar_codigo_postal(codigo_postal)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        nombre_destinatario = input("Ingrese nombre del destinatario: ")
        validar,mensajito = validar_nombre_destinatario(nombre_destinatario)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        tipo_transporte = input("Ingrese el tipo de transporte (A,M,T): ")
        validar,mensajito = validar_tipo_transporte(tipo_transporte)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        peso_kilos = input("Ingrese el peso en kilos: ")
        validar,mensajito = validar_peso_kilos(peso_kilos)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        impuesto_acumulado = input("Ingrese el impuesto acumulado: ")
        validar,mensajito = validar_impuesto_acumulado(impuesto_acumulado)
        if validar == True:
            break
        else:
            print(mensajito)
    envio = {
        "codigo_envio": codigo_envio.upper(),
        "codigo_postal": codigo_postal,
        "nombre_destinatario": nombre_destinatario.title(),
        "tipo_transporte": tipo_transporte.upper(),
        "peso_kilos": int(peso_kilos),
        "impuesto_acumulado": float(impuesto_acumulado),
        "seguimiento_aduana": False
    }
    envios.append(envio)
    print("El envío se registró exitosamente!")

def buscar_envios(codigo_envio,envios):
    for posicion,envio in enumerate(envios):
        if envio["codigo_envio"] == codigo_envio.upper():
            return posicion
    return -1

def eliminar_envio(codigo_envio,envios):
    posicion = buscar_envios(codigo_envio,envios)
    if posicion >= 0:
        envios.pop(posicion)
        print("El envío fue eliminado exitosamente!")
    else:
        print("El envío no existe o ya fue eliminado")

def agregar_costo(codigo_envio,envios):
    posicion = buscar_envios(codigo_envio,envios)
    if posicion >= 0:
        costo_agregado = input("Ingrese el costo a agregar: ")
        validar,mensajito = validar_impuesto_acumulado(costo_agregado)
        if validar == True:
            envios[posicion]["impuesto_acumulado"] += float(costo_agregado)
            print("Monto agregado con éxito!")
        else:
            print(mensajito)
    else:
        print("El envío no existe o fue eliminado")

def actualizar_seguimiento(envios):
    for envio in envios:
        if envio["tipo_transporte"] == "A" or envio["impuesto_acumulado"] >= 60000:
            envio["seguimiento_aduana"] = "Revisión de Aduana Prioritaria"
        else:
            envio["seguimiento_aduana"] = "Libre de Impuesto Extra / OK"
    print("Todos los envíos fueron actualizados")

def mostrar_envios(envios):
    for envio in envios:
        print("--------------------------")
        print("Código envío:", envio["codigo_envio"])
        print("Código postal:", envio["codigo_postal"])
        print("Nombre destinatario:", envio["nombre_destinatario"])
        print("Tipo transporte:", envio["tipo_transporte"])
        print("Peso (kg):", envio["peso_kilos"])
        print("Impuesto acumulado:", envio["impuesto_acumulado"])
        print("Seguimiento:", envio["seguimiento_aduana"])

envios = []
while True:
    os.system("cls")
    mostrar_menu()
    opcion = validar_opcion()

    if opcion == 1:
        os.system("cls")
        print("****** REGISTRAR ENVÍO ******")
        registrar_envio(envios)

    elif opcion == 2:
        os.system("cls")
        if len(envios) == 0:
            print("Aún no hay envíos registrados")
        else:
            print("****** BUSCAR ENVÍO ******")
            codigo_envio = input("Ingrese el código de envío a buscar: ")
            posicion = buscar_envios(codigo_envio,envios)
            if posicion == -1:
                print("El envío no existe o fue eliminado")
            else:
                print("El envío se encuentra en la posición: N°",posicion+1)
                print(envios[posicion])
                print("\n. . . Presione una tecla para volver al menú . . .")
                msvcrt.getch()
                print("Espere unos segundos...")

    elif opcion == 3:
        os.system("cls")
        if len(envios) == 0:
            print("Aún no hay envíos registrados")
        else:
            print("****** ELIMINAR ENVÍO ******")
            codigo_envio = input("Ingrese el código de envío a eliminar: ")
            eliminar_envio(codigo_envio,envios)
    
    elif opcion == 4:
        os.system("cls")
        if len(envios) == 0:
            print("Aún no hay envíos registrados")
        else:
            print("****** AGREGAR COSTOS EXTRA ******")
            codigo_envio = input("Ingrese el código de envío a agregar costo: ")
            agregar_costo(codigo_envio,envios)
    
    elif opcion == 5:
        os.system("cls")
        if len(envios) == 0:
            print("Aún no hay envíos registrados")
        else:
            print("****** ACTUALIZACIÓN DE ENVÍOS ******")
            actualizar_seguimiento(envios)
    
    elif opcion == 6:
        os.system("cls")
        if len(envios) == 0:
            print("Aún no hay envíos registrados")
        else:
            print("****** ENVÍOS REGISTRADOS ******")
            mostrar_envios(envios)
            print("\n. . . Presione una tecla para volver al menú . . .")
            msvcrt.getch()
            print("Espere unos segundos...")
    
    else: 
        print("Adiosito uvu")
        break
    time.sleep(2.5)