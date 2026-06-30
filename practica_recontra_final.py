import os, time, msvcrt

def mostrar_menu():
    print("""=== MENÚ PRINCIPAL ===
1. Registrar envío
2. Buscar un envío
3. Actualizar estado del envío
4. Aplicar promoción a envíos
5. Informe general
6. Eliminar envío""")

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese la opción deseada (1-6): "))
            if 1 <= opc <= 6:
                return opc
            else:
                print("Error: debe ingresar una opción entre 1 y 6")
        except:
            print("Error: debe ingresar un número entero")

def validar_codigo_envio(codigo_envio,envios):
    if not codigo_envio.upper().startswith("E"):
        return False, "Error: el código debe comenzar con la letra E"
    elif len(codigo_envio) != 6:
        return False, "Error: el código debe contener exactamente 6 caracteres"
    elif " " in codigo_envio:
        return False, "Error: el código no debe contener espacios"
    elif buscar_envio(codigo_envio,envios) >= 0:
        return False, "Error: el código ya existe, intente nuevamente"
    else:
        return True, ""
    
def validar_cliente(cliente:str):
    if not 5 <= len(cliente) <= 40:
        return False, "Error: el nombre debe contener entre 5 y 40 caracteres"
    elif not cliente.replace(" ", "").isalpha():
        return False, "Error: el nombre solo debe contener letras y espacios"
    else:
        return True, ""

def validar_destino(destino):
    if destino.title() not in("Santiago","Valparaiso","Valparaíso","Concepcion","Concepción","La Serena","Puerto Montt", "Antofagasta"):
        return False, "Error: debe ingresar un destino válido"
    else:
        return True, ""

def validar_peso(peso):
    try:
        peso = float(peso)
        if 0 < peso <= 80:
            return True, ""
        else:
            return False, "Error: debe ingresar un valor entre 0 y 80"
    except:
        return False, "Error: debe ingresar una cantidad númerica"

def validar_tipo_envio(tipo_envio):
    if tipo_envio.title() not in("Normal","Express","Prioritario"):
        return False, "Error: debe ingresar un tipo de envío válido"
    else:
        return True, ""
    
def validar_seguro(seguro):
    if not seguro.title() in("Si","Sí","No"):
        return False, "Error: debe ingresar una opción válida"
    else:
        return True, ""

def calcular_valor_envio(tipo_envio, seguro, peso):
    if tipo_envio == "Normal":
        costo_porkg = 2000
    elif tipo_envio == "Express":
        costo_porkg = 3500
    else:
        costo_porkg = 5000
    
    total = costo_porkg * peso 
    
    if seguro in("Sí", "Si"):
        total += 0.15 * total 
    
    return total

def calcular_dias_estimados(tipo_envio):
    if tipo_envio == "Normal":
        return 7
    elif tipo_envio == "Express":
        return 3
    else:
        return 1

def registrar_envio(envios):
    while True:
        codigo_envio = input("Ingrese el código del envío: ")
        validar,mensajito = validar_codigo_envio(codigo_envio,envios)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        cliente = input("Ingrese el nombre del cliente: ")
        validar,mensajito = validar_cliente(cliente)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        print("== Destinos ==")
        print("""-Santiago
-Valparaíso
-Concepción
-La Serena
-Puerto Montt
-Antofagasta
""")
        destino = input("Ingrese el destino: ")
        validar,mensajito = validar_destino(destino)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        peso = input("Ingrese el peso en kg: ")
        validar,mensajito = validar_peso(peso)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        tipo_envio = input("Ingrese el tipo de envío (Normal, Express o Prioritario): ")
        validar,mensajito = validar_tipo_envio(tipo_envio)
        if validar == True:
            break
        else:
            print(mensajito)
    while True:
        seguro = input("Tiene seguro? (Sí/No): ")
        validar, mensajito = validar_seguro(seguro)
        if validar == True:
            break
        else:
            print(mensajito)
    
    valor_envio = calcular_valor_envio(tipo_envio.title(),seguro.title(),float(peso))
    dias_estimados = calcular_dias_estimados(tipo_envio.title())

    envio = {
        "codigo_envio": codigo_envio.upper(),
        "cliente": cliente.title(),
        "destino": destino.title(),
        "peso": float(peso),
        "tipo_envio": tipo_envio.title(),
        "valor_envio": int(valor_envio),
        "estado": "Pendiente",
        "seguro": seguro.title(),
        "dias_estimados": dias_estimados
    }
    envios.append(envio)
    print("Envío registrado con éxito!")

def buscar_envio(codigo_envio,envios):
    for posicion,envio in enumerate(envios):
        if envio["codigo_envio"] == codigo_envio.upper():
            return posicion
    return -1

def actualizar_envio(codigo_envio, envios):
    posicion = buscar_envio(codigo_envio, envios)
    if posicion >= 0:
        estado_actual = envios[posicion]["estado"]
        
        if estado_actual == "Pendiente":
            envios[posicion]["estado"] = "En tránsito"
            print("El estado cambió a En Tránsito.")
        elif estado_actual == "En tránsito":
            envios[posicion]["estado"] = "Entregado"
            print("El estado cambió a Entregado.")
        elif estado_actual == "Entregado":
            print("Error: el envío ya se encuentra entregado y no puede modificarse.")
    else:
        print("No se encontró el envío")

def aplicar_promocion(envios):
    contador = 0
    acumulador = 0
    for envio in (envios):
        if envio["peso"] > 20 and envio["seguro"] == "No":
            descuento = 0.10 * envio["valor_envio"]
            envio["valor_envio"] -= descuento
            contador += 1
            acumulador += descuento
    return contador,acumulador

def informe_general(envios):
    total_envios=0
    envios_estado_pendiente=0
    envios_estado_entransito=0
    envios_estado_entregado=0
    envios_normal=0
    envios_express=0
    envios_prioritario=0
    acumulador_peso=0
    acumulador_total=0
    envio_mayor_valor= envios[0]

    for envio in envios:
        print("\n-------------------------")
        print("Código envío:", envio["codigo_envio"])
        print("Cliente:", envio["cliente"])
        print("Destino:", envio["destino"])
        print("Peso:", envio["peso"])
        print("Tipo envío:", envio["tipo_envio"])
        print("Valor envío:", envio["valor_envio"])
        print("Estado:", envio["estado"])
        print("Seguro:", envio["seguro"])
        print("Dìas estimados:", envio["dias_estimados"])
        total_envios += 1
        acumulador_peso += envio["peso"]
        acumulador_total += envio["valor_envio"]

        if envio["valor_envio"] > envio_mayor_valor["valor_envio"]:
            envio_mayor_valor = envio

        if envio["estado"] == "Pendiente":
            envios_estado_pendiente += 1
        if envio["estado"] == "En tránsito":
            envios_estado_entransito += 1
        if envio["estado"] == "Entregado":
            envios_estado_entregado += 1

        if envio["tipo_envio"] == "Normal":
            envios_normal += 1
        if envio["tipo_envio"] == "Express":
            envios_express += 1
        if envio["tipo_envio"] == "Prioritario":
            envios_prioritario += 1

    print("\n-----------REGISTRO GENERAL--------------")
    print("Cantidad de envíos registrados:",total_envios)
    print("\nEnvíos pendientes:",envios_estado_pendiente)
    print("Envíos en tránsito:",envios_estado_entransito)
    print("Envíos entregados:",envios_estado_entregado)
    print("\nPeso promedio entre los envíos:",acumulador_peso/len(envios))
    print("\nEnvíos tipo Normal:",envios_normal)
    print("Envíos tipo Express:",envios_express)
    print("Envíos tipo Prioritario:",envios_prioritario)
    print(f"\nEnvío con mayor valor: {envio_mayor_valor['codigo_envio']} (${envio_mayor_valor["valor_envio"]})")
    print("\nTotal recaudado:",acumulador_total)

def eliminar_envio(codigo_envio,envios):
    posicion = buscar_envio(codigo_envio,envios)
    if posicion >= 0:
        if envios[posicion]["estado"] == "Pendiente":
            envios.pop(posicion)
            print("Envío eliminado exitosamente")
        else:
            print("Error, el envío no se puede eliminar.")
    else:
        print("No se encontró el registro del envío")

envios = []
while True:
    os.system("cls")
    mostrar_menu()
    opcion = validar_opcion()

    if opcion == 1:
        registrar_envio(envios)

    elif opcion == 2:
        os.system("cls")
        if len(envios) == 0:
            print("Aún no hay envíos registrados")
        else:
            print("***** BUSCAR ENVÍO *****")
            codigo_envio = input("Ingrese codigo del envio a buscar: ")
            posicion = buscar_envio(codigo_envio,envios)
            if posicion == -1:
                print("El envío no existe o fue eliminado")
            else:
                print("Posición envío: N°",posicion+1)
                print(envios[posicion])
    
    elif opcion == 3:
        os.system("cls")
        if len(envios) == 0:
            print("Aún no hay envíos registrados")
        else:
            print("***** ACTUALIZAR ENVÍO *****")
            codigo_envio = input("Ingerse el código del envío a actualizar: ")
            actualizar_envio(codigo_envio,envios)
    
    elif opcion == 4:
        os.system("cls")
        if len(envios) == 0:
            print("Aún no hay envíos registrados")
        else:
            print("***** PROMOCIONES APLICADAS *****")
            contador,acumulador = aplicar_promocion(envios)
            print("Los envíos fueron actualizados")
            print(f"Se modificaron: {contador} envíos.")
            print(f"Monto total descontado: {acumulador} ")

    elif opcion == 5:
        os.system("cls")
        if len(envios) == 0:
            print("Aún no hay envíos registrados")
        else:
            print("***** ENVÍOS REGISTRADOS *****")
            informe_general(envios)
            print("\n. . . Presione una tecla para volver al menú . . .")
            msvcrt.getch()
            print("Espere unos segundos...")
    
    else:
        os.system("cls")
        if len(envios) == 0:
            print("Aún no hay envíos registrados")
        else:
            print("***** ELIMINAR ENVÍO *****")
            codigo_envio = input("Ingrese código del envío a eliminar: ")
            eliminar_envio(codigo_envio,envios)
    time.sleep(2.5)