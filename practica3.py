def mostrar_menu():
    print("""=== MENÚ PRINCIPAL ===
1. Registrar consulta paciente
2. Buscar consulta por código
3. Eliminar consulta
4. Actualizar prioridad de atención
5. Mostrar todas las consultas
6. Salir""")
    

def leer_opcion():
    while True:
        try:
            opc = int(input("Ingrese opcion deseada (1-6): "))
            if 1 <= opc <= 6:
                return opc
            else:
                print("Error: ingrese una opción del 1 al 6")
        except:
            print("Error: debe ingresar un número entero")

def validar_codigo_paciente(codigo_paciente,consultas):
    if codigo_paciente[0].upper() != "C":
        return False, "Error: el código debe empezar con la letra C"
    elif len(codigo_paciente) != 5:
        return False, "Error: el código debe tener exactamente 5 caracteres"
    elif " " in codigo_paciente:
        return False, "Error: el código no debe contener espacios"
    if busqueda_consulta(codigo_paciente,consultas) >= 0:
        return False, "Error: el código ya existe, intente nuevamente"
    else:
        return True, ""

def validar_nombre_completo(nombre_completo:str):
    if len(nombre_completo) < 6:
        return False, "Error: el nombre debe tener al menos 6 caracteres"
    elif nombre_completo.isnumeric():
        return False, "Error: el nombre no puede estar conformado unicamente por números"
    else:
        return True, ""

def validar_tipo_atencion(tipo_atencion):
    if not tipo_atencion.upper() in ("G","E","U"):
        return False, "Error: el tipo de atencion debe ser G, E o U"
    else:
        return True, ""

def validar_edad_paciente(edad_paciente):
    try:
        edad_paciente = int(edad_paciente)
        if 0 <= edad_paciente <= 100:
            return True, ""
        else:
            return False, "Error: la edad mínima es 0 y la edad máxima es 110"
    except:
        return False, "Error: debe ingresar un número entero"

def validar_costo_consulta(costo_consulta):
    try:
        costo_consulta = float(costo_consulta)
        if costo_consulta > 0:
            return True, ""
        else:
            return False, "Error: debe ingresar un valor mayor a 0"
    except:
        return False, "Error: debe ingresar un número"


def agregar_consulta(consultas):
    while True:
        codigo_paciente = input("Ingrese código paciente: ")
        validar,mensajito = validar_codigo_paciente(codigo_paciente, consultas)
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
        tipo_atencion = input("Ingrese tipo atención (G,E,U): ")
        validar,mensajito = validar_tipo_atencion(tipo_atencion)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        edad_paciente = input("Ingrese la edad del paciente: ")
        validar,mensajito = validar_edad_paciente(edad_paciente)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        costo_consulta = input("Ingrese el costo de la consulta: ")
        validar,mensajito = validar_costo_consulta(costo_consulta)
        if validar == True:
            break
        else:
            print(mensajito)
    consulta = {
        "codigo_paciente": codigo_paciente.title(),
        "nombre_completo": nombre_completo.title(),
        "tipo_atencion": tipo_atencion.upper(),
        "edad_paciente": int(edad_paciente),
        "costo_consulta": float(costo_consulta),
        "prioridad_atencion": "Atención Normal"

    }
    consultas.append(consulta)
    print("Consulta registrada exitosamente!")

def mostrar_consultas(consultas):
    if len(consultas) == 0:
        print("Aún no hay consultas registradas")
        return
    for consulta in consultas:
        print("\n----------------------------")
        print("Codigo paciente:", consulta["codigo_paciente"])
        print("Nombre completo:", consulta["nombre_completo"])
        print("Tipo atención:", consulta["tipo_atencion"])
        print("Edad:", consulta["edad_paciente"])
        print("Costo consulta:", consulta["costo_consulta"])
        print("Prioridad:", consulta["prioridad_atencion"])

def busqueda_consulta(codigo_paciente,consultas):
    for posicion,consulta in enumerate(consultas):
        if consulta["codigo_paciente"] == codigo_paciente:
            return posicion
    return -1

def eliminar_consulta(codigo_paciente,consultas):
    posicion = busqueda_consulta(codigo_paciente,consultas)
    if posicion >= 0:
        consultas.pop(posicion)
        print("Consulta eliminada con éxito")
    else:
        print("No se ha podido eliminar, la consulta no existe o ya fue eliminada")

def actualizar_prioridad(consultas):
    for consulta in consultas:
        if consulta["tipo_atencion"] == "U" or consulta["edad_paciente"] >= 65:
            consulta["prioridad_atencion"] = "Atención Prioritaria"
        else:
            consulta["prioridad_atencion"] = "Atención Normal"
    print("Todas las prioridades de atención se actualizaron correctamente")

consultas = []
while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_consulta(consultas)
    
    elif opcion == 2:
        if len(consultas) == 0:
           print("No hay consultas aún")
        else:
            codigo_paciente = input("Ingrese código de paciente a buscar: ").title()
            posicion = busqueda_consulta(codigo_paciente,consultas)
            if posicion != -1:
                print("La consulta se encuentra en la posición: N°",posicion+1)
                print(consultas[posicion])
            else:
                print("La consulta no se encontró o ya fue eliminada.")
    
    elif opcion == 3:
        if len(consultas) == 0:
           print("No hay consultas aún")
        else:
            codigo_paciente = input("Ingrese código de paciente a eliminar: ").title()
            eliminar_consulta(codigo_paciente,consultas)
    
    elif opcion == 4:
        if len(consultas) == 0:
           print("No hay consultas aún")
        else:
            actualizar_prioridad(consultas)

    elif opcion == 5:
        if len(consultas) == 0:
           print("No hay consultas aún")
        else:
            mostrar_consultas(consultas)
    
    else:
        print("adiosito")
        break