def mostrar_menu():
    print("""=== MENÚ PRINCIPAL ===
1. Registrar arriendo
2. Buscar arriendo por código
3. Eliminar arriendo
4. Actualizar seguros y revisión
5. Mostrar todos los arriendos
6. Salir""")

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción deseada (1-6): "))
            if 1 <= opc <= 6:
                return opc
            else:
                print("Error: ingrese opción entre 1 y 6")
        except:
            print("Error: debe ingresar un número entero")

def validar_codigo_arriendo(codigo_arriendo,arriendos):
    if not codigo_arriendo.upper().startwith("R"):
        return False, "Error: el código debe empezar con R"
    elif len(codigo_arriendo) != 5:
        return False, "Error: el código debe tener exactamente 5 caracteres"
    elif " " in codigo_arriendo:
        return False, "Error: el código no debe contener espacios"
    elif buscar_arriendo(codigo_arriendo,arriendos) >= 0:
        return False, "Error: el código ya existe, intente nuevamente"
    else:
        return True, ""
    
def validar_patente_vehiculo(patente_vehiculo):
    if " " in patente_vehiculo:
        return False, "Error: la patente no debe contener espacios"
    elif len(patente_vehiculo) != 6:
        return False, "Error: la patente debe tener exactamente 6 caracteres"
    else:
        return True, ""

def validar_nombre_cliente(nombre_cliente):
    if len(nombre_cliente) < 8:
        return False, "Error: el nombre debe tener al menos 8 caracteres"
    elif nombre_cliente.isnumeric():
        return False, "Error: el nombre no debe estar conformado unicamente por numeros"
    else:
        return True, ""
    
def validar_tipo_vehiculo(tipo_vehiculo):
    if not tipo_vehiculo.upper().strip() in("S","C","P"):
        return False, "Error: el tipo de vehiculo debe ser S, C o P"
    else:
        return True, ""

def validar_dias_arriendo(dias_arriendo):
    try:
        dias_arriendo = int(dias_arriendo)
        if 1 <= dias_arriendo <= 45:
            return True, ""
        else:
            return False, "Error: debe ingresar una cantidad entre 1 y 45"
    except:
        return False, "Error: debe ingresar la cantidad como número entero"

def validar_garantia_pagada(garantia_pagada):
    try:
        garantia_pagada = float(garantia_pagada)
        if garantia_pagada >= 50000:
            return True, ""
        else:
            return False, "Error: debe ingresar una cantidad mayor o igual a 50000"
    except:
        return False, "Error: debe ingresar la cantidad como numero"

def agregar_arriendo(arriendos):
    while True:
        codigo_arriendo = input("Ingrese el código de arriendo: ")
        validar,mensajito = validar_codigo_arriendo(codigo_arriendo,arriendos)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        patente_vehiculo = input("Ingrese la patente del vehiculo: ")
        validar,mensajito = validar_patente_vehiculo(patente_vehiculo)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        nombre_cliente = input("Ingrese su nombre: ")
        validar,mensajito = validar_nombre_cliente(nombre_cliente)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        tipo_vehiculo = input("Ingrese el tipo de vehiculo (S,C,P): ")
        validar,mensajito = validar_tipo_vehiculo(tipo_vehiculo)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        dias_arriendo = input("Ingrese dias de arriendo: ")
        validar,mensajito = validar_dias_arriendo(dias_arriendo)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        garantia_pagada = input("Ingrese garantia pagada: ")
        validar,mensajito = validar_garantia_pagada(garantia_pagada)
        if validar == True:
            break
        else:
            print(mensajito)
    arriendo = {
        "codigo_arriendo": codigo_arriendo.upper(),
        "patente_vehiculo": patente_vehiculo.upper(),
        "nombre_cliente": nombre_cliente.title(),
        "tipo_vehiculo": tipo_vehiculo.upper().strip(),
        "dias_arriendo": int(dias_arriendo),
        "garantia_pagada": float(garantia_pagada),
        "estado_revision": "Pendiente de inspección"
    }
    arriendos.append(arriendo)
    print("Se registró el arriendo exitosamente")

def buscar_arriendo(codigo_arriendo,arriendos):
    for posicion,arriendo in enumerate(arriendos):
        if arriendo["codigo_arriendo"] == codigo_arriendo.upper():
            return posicion
    return -1
        
def eliminar_arriendo(codigo_arriendo,arriendo):
    posicion = buscar_arriendo(codigo_arriendo,arriendo)
    if posicion >= 0:
        arriendo.pop(posicion)
        print("Arriendo eliminado exitosamente")
    else:
        print("Error: el arriendo no existe o ya fue eliminado")

def actualizar_revision(arriendos):
    for arriendo in arriendos:
        if arriendo["tipo_vehiculo"] == "P" or arriendo["dias_arriendo"] >= 30:
            arriendo["estado_revision"] = "Requiere Seguro Extendido"
        else:
            arriendo["estado_revision"] = "Seguro Estándar OK"
    print("Todas los seguimientos fueron actualizados")

def mostrar_arriendos(arriendos):
    for arriendo in arriendos:
        print("\n---------------------------------")
        print("Codigo arriendo:", arriendo["codigo_arriendo"])
        print("Patente vehículo:", arriendo["patente_vehiculo"])
        print("Nombre cliente:", arriendo["nombre_cliente"])
        print("Tipo vehículo:", arriendo["tipo_vehiculo"])
        print("Dias de arriendo:", arriendo["dias_arriendo"])
        print("Garantia pagada:", arriendo["garantia_pagada"])
        print("Estado de revisión:", arriendo["estado_revision"])

arriendos = []
while True:
    mostrar_menu()
    opcion = validar_opcion()
    
    if opcion == 1:
        agregar_arriendo(arriendos)
    
    elif opcion == 2:
        if len(arriendos) == 0:
            print("Aún no hay arriendos registrados")
        else:
            codigo_arriendo = input("Ingrese codigo a buscar: ").upper()
            posicion = buscar_arriendo(codigo_arriendo,arriendos)
            if posicion != -1:
                print("El arriendo se encuentra en la posición: N°",posicion+1)
            else:
                print("El arriendo no existe o ya fue eliminado")
    
    elif opcion == 3:
        if len(arriendos) == 0:
            print("Aún no hay arriendos registrados")
        else:
            codigo_arriendo = input("Ingrese codigo a eliminar: ").upper()
            eliminar_arriendo(codigo_arriendo,arriendos)
    
    elif opcion == 4:
        if len(arriendos) == 0:
            print("Aún no hay arriendos registrados")
        else:
            actualizar_revision(arriendos)
    
    elif opcion == 5:
        if len(arriendos) == 0:
            print("Aún no hay arriendos registrados")
        else:
            mostrar_arriendos(arriendos)
    
    else:
        print("adiosiwi")
        break