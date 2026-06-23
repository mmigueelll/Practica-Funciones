
def mostrar_menu():
    print("""=== MENÚ PRINCIPAL ===
1. Agregar solicitud
2. Buscar solicitud
3. Eliminar solicitud
4. Actualizar estado de solicitudes
5. Mostrar solicitudes
6. Salir
""")

def leer_opcion():
    while True:
        try:
            opc = int(input("Ingrese la opción deseada (1-6): "))
            if 1<= opc <= 6:
                return opc
            else:
                print("Error: debe elegir una opción entre 1 y 6")
        except:
            print("Error: debe ingresar un número entero")

def validar_id_solicitud(valor,registros):
    if len(valor) < 6:
        return False, "Error: La id debe contener al menos 6 caracteres"
    elif " " in valor:
        return False, "Error: La id no debe contener espacios"
    elif buscar_registro(valor,registros) != -1:
        return False, "Error: La id ya existe, intente con otra"
    else:
        return True, ""

def validar_nombre_equipo(valor):
    if len(valor) < 4:
        return False, "Error: El nombre debe contener al menos 4 caracteres"
    elif " " in valor:
        return False, "Error: El nombre no debe contener espacios"
    else:
        return True, ""

def validar_area(valor):
    if not valor.upper() in("S","R","M"):
        return False, "Error: El area debe ser S, R o M"
    else:
        return True, ""

def validar_prioridad(valor):
    try:
        valor = int(valor)
        if 1<= valor <= 5:
            return True, ""
        else:
            return False, "Error: debe ingresar un número entre 1 y 5"
    except:
        return False, "Error: debe ingresar un número entero"

def validar_costo_estimado(valor):
    try:
        valor = int(valor)
        if valor > 0:
            return True, ""
        else:
            return False, "Error: debe ingresar un número mayor a 0"
    except:
        return False, "Error: debe ingresar un número entero"

def agregar_registro(registros):
    while True:
        id_solicitud = input("Ingrese la id: ")
        validacion,mensajito = validar_id_solicitud(id_solicitud,registros)
        if validacion == True:
            break
        else:
            print(mensajito)
    while True:
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        validacion,mensajito = validar_nombre_equipo(nombre_equipo)
        if validacion == True:
            break
        else:
            print(mensajito)
    while True:
        area = input("Ingrese area (S,R,M): ")
        validacion,mensajito = validar_area(area)
        if validacion == True:
            break
        else:
            print(mensajito)
    while True:
        prioridad = input("Ingrese la prioridad: ")
        validacion,mensajito = validar_prioridad(prioridad)
        if validacion == True:
            break
        else:
            print(mensajito)
    while True:
        costo_estimado = input("Ingrese el costo estimado: ")
        validacion,mensajito = validar_costo_estimado(costo_estimado)
        if validacion == True:
            break
        else:
            print(mensajito)
    registro = {
        "id_solicitud": id_solicitud,
        "nombre_equipo": nombre_equipo.title(),
        "area": area.upper(),
        "prioridad": int(prioridad),
        "costo_estimado": int(costo_estimado),
        "estado": False
    }
    registros.append(registro)
    print("Registro agregado exitosamente")

def buscar_registro(id_solicitud,registros):
    for posicion,registro in enumerate(registros):
        if registro["id_solicitud"] == id_solicitud:
            return posicion
    return -1
            
def eliminar_registro(id_solicitud,registros):
    posicion = buscar_registro(id_solicitud,registros)
    if posicion == -1:
        return False, "Error: El registro no existe o ya fue eliminado"
    else:
        registros.pop(posicion)
        return True, "Registro eliminado con éxito"

def actualizar_estado(registros):
    for registro in registros:
        if registro["prioridad"] >= 4:
            registro["estado"] = True
        else:
            registro["estado"] = False

def mostrar_registros(registros):
    for registro in registros:
        print("Id solicitud:",registro["id_solicitud"])
        print("Nombre equipo:",registro["nombre_equipo"])
        print("Area:",registro["area"])
        print("Prioridad:",registro["prioridad"])
        print("Costo estimado:",registro["costo_estimado"])
        print("Estado:",registro["estado"])


registros = []
while True:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        agregar_registro(registros)
    
    elif opcion == 2:
        print("*** BUSCAR SOLICITUD ***")
        id_solicitud = input("Ingrese id a buscar: ")
        posicion = buscar_registro(id_solicitud,registros)
        if posicion == -1:
            print("El registro no existe o ya fue eliminado")
        else:
            print("El registro se encuentra en la posición: N°",posicion+1)
    
    elif opcion == 3:
        print("*** ELIMINAR REGISTRO ***")
        id_solicitud = input("Ingrese id a eliminar: ")
        validacion,mensajito = eliminar_registro(id_solicitud,registros)
        if validacion == True:
            print(mensajito)
        else:
            print(mensajito)
    
    elif opcion == 4:
        actualizar_estado(registros)
        print("Registros actualizados correctamente")
    
    elif opcion == 5:
        mostrar_registros(registros)
    
    else:
        print("adiosito")
        break