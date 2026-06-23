def mostrar_menu():
    print("""=== MENÚ PRINCIPAL ===
1. Registrar inscripción
2. Buscar inscripción
3. Eliminar inscripción
4. Evaluar becas de estudio
5. Mostrar todas las inscripciones
6. Salir
7. Mostrar estudiantes becados""")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese la opción que desee (1-7): "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Opción inválida. Ingrese un número entero entre 1 y 7")
        except:
            print("Error: Debe ingresar un número")

def validar_codigo_inscripcion(inscripciones:list, valor:str):
    if valor[0].upper() != "I":
        return False
    elif len(valor) != 6:
        return False
    elif " " in valor:
        return False
    elif buscar_inscripcion(inscripciones, valor.title()) != -1:
        return False
    else:
        return True

def validar_nombre_estudiante(valor:str):
    if len(valor) < 4:
        return False
    for letra in valor:
        if letra.isdigit():
            return False
    return True

def validar_nivel_curso(valor:str):
    if not valor.upper() in("B","I","A"):
        return False
    return True

def validar_edad_estudiante(valor):
    try:
        edad = int(valor)
        if edad < 14 or edad > 99:
            return False
        else:
            return True
    except:
        return False

def validar_meses_duracion(valor):
    try:
        meses = int(valor)
        if meses < 1 or meses > 12:
            return False
        else:
            return True
    except:
        return False

def agregar_incripcion(inscripciones:list):
    while True:
        codigo_inscripcion = input("Ingrese código de inscripción (EJ: I10020): ")
        if validar_codigo_inscripcion(inscripciones, codigo_inscripcion):
            break
        else:
            print("Error: código de inscripción inválido.")
            continue
    while True:
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")
        if validar_nombre_estudiante(nombre_estudiante):
            break
        else:
            print("Error: nombre de estudiante inválido.")
            continue
    while True:
        nivel_curso = input("Ingrese el nivel de curso al que pertenece (B,I,A): ")
        if validar_nivel_curso(nivel_curso):
            break
        else:
            print("Error: nivel de curso inválido.")
            continue
    while True:
        edad_estudiante = input("Ingrese la edad del estudiante: ")
        if validar_edad_estudiante(edad_estudiante):
            break
        else:
            print("Error: edad inválida.")
            continue
    while True:
        meses_duracion = input("Ingrese los meses de duración: ")
        if validar_meses_duracion(meses_duracion):
            break
        else:
            print("Error: cantidad inválida.")
            continue
    inscripcion = {
        "codigo_inscripcion": codigo_inscripcion.title(),
        "nombre_estudiante": nombre_estudiante.title(),
        "nivel_curso": nivel_curso.upper(),
        "edad_estudiante": int(edad_estudiante),
        "meses_duracion": int(meses_duracion),
        "beca_aprobada": False
    }
    inscripciones.append(inscripcion)
    print("Incripción agregada con éxito.")

def buscar_inscripcion(inscripciones, codigo_inscripcion):
    for posicion in range(len(inscripciones)):
        if inscripciones[posicion]["codigo_inscripcion"] == codigo_inscripcion:
            return posicion
    return -1

def eliminar_inscripcion(inscripciones, codigo_inscripcion):
    if buscar_inscripcion(inscripciones, codigo_inscripcion) == -1:
        return False
    else:
        return True

def evaluar_becas(inscripciones:list):
    for inscripcion in inscripciones:
        if inscripcion["edad_estudiante"] <= 18:
            if inscripcion["meses_duracion"] >= 6:
                inscripcion["beca_aprobada"] = True
            else:
                inscripcion["beca_aprobada"] = False
        else:
            inscripcion["beca_aprobada"] = False

def mostrar_inscripciones(inscripciones):
    for inscripcion in inscripciones:
        print("\n-------------------------------------")
        print("Codigo Inscripción:", inscripcion["codigo_inscripcion"])
        print("Nombre Estudiante:", inscripcion["nombre_estudiante"])
        print("Nivel Curso:", inscripcion["nivel_curso"])
        print("Edad Estudiante:", inscripcion["edad_estudiante"])
        print("Meses Duración:", inscripcion["meses_duracion"])
        print("Beca Aprobada:", inscripcion["beca_aprobada"])

def mostrar_estudiantes_becados(inscripciones):
    aprobados = 0
    for inscripcion in inscripciones:
        if inscripcion["beca_aprobada"] == True:
            print("\n-------------------------------------")
            print("Codigo Inscripción:", inscripcion["codigo_inscripcion"])
            print("Nombre Estudiante:", inscripcion["nombre_estudiante"])
            print("Nivel Curso:", inscripcion["nivel_curso"])
            print("Edad Estudiante:", inscripcion["edad_estudiante"])
            print("Meses Duración:", inscripcion["meses_duracion"])
            print("Beca Aprobada:", inscripcion["beca_aprobada"])
            aprobados +=1
    return aprobados

inscripciones = []
while True:
    mostrar_menu()
    opcion = leer_opcion()
    
    if opcion == 1:
        agregar_incripcion(inscripciones)

    elif opcion == 2:
        if len(inscripciones) == 0:
            print("Aún no hay inscripciones.")
        else:
            print("*** BUSCAR INSCRIPCIÓN ***")
            codigo_inscripcion = input("Ingrese el código de incripción a buscar: ").title()
            posicion = buscar_inscripcion(inscripciones, codigo_inscripcion)
            if posicion != -1:
                print("Reserva encontrada en la posición: ", posicion)
            else:
                print("La inscripción no existe")
    
    elif opcion == 3:
        if len(inscripciones) == 0:
            print("Aún no hay inscripciones.")
        else:
            print("*** ELIMINAR INSCRIPCIÓN ***")
            codigo_inscripcion = input("Ingrese el código de incripción a buscar: ").title()
            posicion = buscar_inscripcion(inscripciones, codigo_inscripcion)
            if eliminar_inscripcion(inscripciones, codigo_inscripcion):
                inscripciones.pop(posicion)
                print("Inscripción eliminada con éxito")
            else:
                print("La inscripcion no existe o ya fue eliminada")
    
    elif opcion == 4:
        if len(inscripciones) == 0:
            print("Aún no hay inscripciones.")
        else:
            evaluar_becas(inscripciones)
            print("Todas las becas fueron actualizadas")
    
    elif opcion == 5:
        if len(inscripciones) == 0:
            print("Aún no hay inscripciones.")
        else:
            print("*****     INSCRIPCIONES     ******")
            mostrar_inscripciones(inscripciones)
    
    elif opcion == 6:
        print("Finalizando ejecución del programa. Adiosito uvu")
        break

    else: 
        if len(inscripciones) == 0:
            print("Aún no hay inscripciones.")
        else:
            aprobados = mostrar_estudiantes_becados(inscripciones)
            if aprobados == 0:
                print("No hay estudiantes aprobados aún")
            else:
                print("*****     INSCRIPCIONES APROBADAS     ******")
                mostrar_estudiantes_becados(inscripciones)