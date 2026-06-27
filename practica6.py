def mostrar_menu():
    print("""=== MENÚ PRINCIPAL ===
1. Registrar herramienta
2. Buscar herramienta por código
3. Eliminar herramienta
4. Agregar cobro adicional
5. Actualizar seguimiento de bodega
6. Mostrar herramientas
7. Salir""")

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese la opción que desee (1-7): "))
            if 1 <= opc <= 7:
                return opc
            else:
                print("Error: debe ingresar una opción entre 1 y 7")
        except:
            print("Error: debe ingresar un número entero")

def validar_codigo_herramienta(codigo_herramienta,herramientas):
    if not codigo_herramienta.upper().startswith("H"):
        return False, "Error: el código debe empezar con la letra H"
    elif len(codigo_herramienta) != 5:
        return False, "Error: el código debe contener 5 caracteres exactamente"
    elif " " in codigo_herramienta:
        return False, "Error: el código no debe contener espacios"
    elif buscar_herramienta(codigo_herramienta,herramientas) >= 0:
        return False, "Error: el código ya existe, intente nuevamente"
    else:
        return True, ""

def validar_nombre_herramienta(nombre_herramienta):
    if len(nombre_herramienta) < 6:
        return False, "Error: el nombre debe tener al menos 6 caracteres"
    elif nombre_herramienta.isnumeric():
        return False, "Error: el nombre no debe estar formado únicamente por números"
    else:
        return True, ""

def validar_categoria(categoria):
    if categoria.upper() in("E","M","P"):
        return True, ""
    else:
        return False, "Error: la categoría debe ser E, M o P"

def validar_stock_disponible(stock_disponible):
    try:
        stock_disponible = int(stock_disponible)
        if 1 <= stock_disponible <= 50:
            return True, ""
        else:
            return False, "Error: debe ingresar una cantidad entre 1 y 50"
    except:
        return False, "Error: debe ingresar un número entero"

def validar_cobro_adicional(cobro_adicional):
    try:
        cobro_adicional = float(cobro_adicional)
        if cobro_adicional >= 0:
            return True, ""
        else:
            return False, "Error: debe ingresar una cantidad igual o mayor a 0"
    except:
        return False, "Error: debe ingresar la cantidad en números"

def registrar_herramienta(herramientas):
    while True:
        codigo_herramienta = input("Ingrese código de la herramienta: ")
        validar,mensajito = validar_codigo_herramienta(codigo_herramienta,herramientas)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        nombre_herramienta = input("Ingrese el nombre de la herramienta: ")
        validar,mensajito = validar_nombre_herramienta(nombre_herramienta)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        categoria = input("Ingrese la categoría (E,M,P): ")
        validar,mensajito = validar_categoria(categoria)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        stock_disponible = input("Ingrese el stock: ")
        validar,mensajito = validar_stock_disponible(stock_disponible)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        cobro_adicional = input("Ingrese el cobro adicional: ")
        validar,mensajito = validar_cobro_adicional(cobro_adicional)
        if validar == True:
            break
        else:
            print(mensajito)
    herramienta = {
        "codigo_herramienta": codigo_herramienta.upper(),
        "nombre_herramienta": nombre_herramienta.title(),
        "categoria": categoria.upper(),
        "stock_disponible": int(stock_disponible),
        "cobro_adicional": float(cobro_adicional),
        "seguimiento_bodega": False
    }
    herramientas.append(herramienta)
    print("Herramienta registrada con éxito!")

def buscar_herramienta(codigo_herramienta,herramientas):
    for posicion,herramienta in enumerate(herramientas):
        if herramienta["codigo_herramienta"] == codigo_herramienta.upper():
            return posicion
    return -1

def eliminar_herramienta(codigo_herramienta,herramientas):
    posicion = buscar_herramienta(codigo_herramienta,herramientas)
    if posicion >= 0:
        herramientas.pop(posicion)
        print("Herramienta eliminada con éxito")
    else:
        print("El registro no existe o ya fue eliminado")

def agregar_cobro_adicional(codigo_herramienta,herramientas):
    posicion = buscar_herramienta(codigo_herramienta,herramientas)
    if posicion >= 0:
        while True:
                cobro_extra = input("Ingrese la cantidad a sumar: ")
                validar,mensajito = validar_cobro_adicional(cobro_extra)
                if validar == True:
                    herramientas[posicion]["cobro_adicional"] += float(cobro_extra)
                    print("Cobro agregado con éxito!")
                    return
                else:
                    print(mensajito)
    else:
        print("No se encuentra la herramienta.")

def actualizar_seguimiento(herramientas):
    for herramienta in herramientas:
        if herramienta["cobro_adicional"] >= 8000:
            herramienta["seguimiento_bodega"] = "Requiere Revisión Técnica Urgentemente"
        else:
            herramienta["seguimiento_bodega"] = "Estado Operativo OK"

def mostrar_herramientas(herramientas):
    for herramienta in herramientas:
        print("\n-----------------------------------")
        print("Código herramienta:", herramienta["codigo_herramienta"])
        print("Nombre herramienta:", herramienta["nombre_herramienta"])
        print("Categoría:", herramienta["categoria"])
        print("Stock disponible:", herramienta["stock_disponible"])
        print("Cobro adicional:", herramienta["cobro_adicional"])
        print("Seguimiento:", herramienta["seguimiento_bodega"])

herramientas = []
while True:
    mostrar_menu()
    opcion = validar_opcion()
    
    if opcion == 1:
        registrar_herramienta(herramientas)
    
    elif opcion == 2:
        if len(herramientas) == 0:
            print("Aún no hay herramientas registradas.")
        else:
            codigo_herramienta = input("Ingrese código de herramienta a buscar: ")
            posicion = buscar_herramienta(codigo_herramienta,herramientas)
            if posicion == -1:
                print("El registro no existe o fue eliminado")
            else:
                print("La herramienta se encuentra en la posición: N°",posicion+1)
                print(herramientas[posicion])
    
    elif opcion == 3:
        if len(herramientas) == 0:
            print("Aún no hay herramientas registradas.")
        else:
            codigo_herramienta = input("Ingrese código de herramienta a eliminar: ")
            eliminar_herramienta(codigo_herramienta,herramientas)
    
    elif opcion == 4:
        if len(herramientas) == 0:
            print("Aún no hay herramientas registradas.")
        else:
            codigo_herramienta = input("Ingrese código de herramienta a añadir cobro: ")
            agregar_cobro_adicional(codigo_herramienta,herramientas)
    
    elif opcion == 5:
        if len(herramientas) == 0:
            print("Aún no hay herramientas registradas.")
        else:
            actualizar_seguimiento(herramientas)
            print("Todos los registros fueron actualizados.")
    
    elif opcion == 6:
        if len(herramientas) == 0:
            print("Aún no hay herramientas registradas.")
        else:
            print("********* HERRAMIENTAS REGISTRADAS *********")
            mostrar_herramientas(herramientas)
    
    else:
        print("adiosito")
        break