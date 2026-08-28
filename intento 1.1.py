import csv
import os

# LISTAS DEL SISTEMA SERRBIA S.A.C

# SERVICIO
codigos = []
clientes = []
dnis = []

lugares = []
proyectos = []
observaciones = []

maquinarias = []
operadores = []

fechas_inicio = []
fechas_fin = []

# HORAS
horas_maquina = []
horas_operador = []

# COSTOS
tarifas = []
costos = []

# MAQUINARIA
horometro_inicio = []
horometro_final = []

# COMBUSTIBLE
galones_combustible = []
horometro_combustible = []

# MANTENIMIENTO
mantenimientos = []

# GASTOS
gastos_extra = []

# DOCUMENTOS
documentos = []

# LOGIN

def login():

    usuario_correcto = "admin"
    contraseña_correcta = "1234"

    while True:

        print("\n===== INICIO DE SESIÓN =====")

        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        if usuario == usuario_correcto and contraseña == contraseña_correcta:

            print("\nAcceso permitido.")
            print("Bienvenido al Sistema SERRBIA S.A.C.")
            break

        else:

            print("\nUsuario o contraseña incorrectos.")

# REGISTRAR SERVICIO

def registrar_servicio():

    print("\n===== REGISTRAR SERVICIO =====")


    codigo = input("Código del servicio: ")

    cliente = input("Nombre del cliente: ")

    dni = input("DNI/RUC: ")


    lugar = input("Lugar del trabajo: ")

    proyecto = input("Nombre del proyecto: ")

    observacion = input("Trabajo realizado: ")


    operador = input("Operador asignado: ")


    print("\n===== DATOS DE MAQUINARIA =====")

    maquinaria = "Caterpillar 252B2"

    print("Maquinaria:", maquinaria)

    while True:

        try:

            h_inicio = float(input("Horómetro inicial: "))

            break

        except:

            print("Ingrese un valor válido.")

    while True:

        try:

            h_final = float(input("Horómetro final: "))

            if h_final >= h_inicio:
                break

            print("El horómetro final debe ser mayor.")

        except:

            print("Ingrese un valor válido.")

    while True:

        try:

            horas_m = float(
                input("Horas trabajadas por la máquina: ")
            )

            if horas_m > 0:
                break

            print("Debe ser mayor a cero.")

        except:

            print("Ingrese un número válido.")

    while True:

        try:

            horas_o = float(
                input("Horas trabajadas por el operador: ")
            )

            if horas_o > 0:
                break

            print("Debe ser mayor a cero.")

        except:

            print("Ingrese un número válido.")

    tarifa = float(
        input("Costo de alquiler por hora: ")
    )

    gasto = float(
        input("Gastos adicionales: ")
    )

    galones = float(
        input("Galones de combustible cargados: ")
    )

    h_combustible = float(
        input("Horómetro al cargar combustible: ")
    )

    costo = (horas_m * tarifa) + gasto

    # GUARDAR INFORMACIÓN

    codigos.append(codigo)
    clientes.append(cliente)
    dnis.append(dni)
    lugares.append(lugar)
    proyectos.append(proyecto)
    observaciones.append(observacion)
    maquinarias.append(maquinaria)
    operadores.append(operador)
    fechas_inicio.append(
        input("Fecha de inicio: ")
    )
    fechas_fin.append(
        input("Fecha de finalización: ")
    )
    horas_maquina.append(horas_m)
    horas_operador.append(horas_o)
    horometro_inicio.append(h_inicio)
    horometro_final.append(h_final)
    tarifas.append(tarifa)
    costos.append(costo)
    galones_combustible.append(galones)
    horometro_combustible.append(h_combustible)
    mantenimientos.append(
        "Sin mantenimiento registrado"
    )
    gastos_extra.append(gasto)
    documentos.append(
        "Pendiente"
    )

    print("\nServicio registrado correctamente.")

    print(
        f"Costo total: S/. {costo:.2f}"
    )

# MOSTRAR SERVICIOS

def mostrar_servicios():

    if not codigos:

        print("\nNo existen servicios registrados.")

        return

    print("\n===== LISTA DE SERVICIOS =====")

    for i in range(len(codigos)):

        print("\n==============================")

        print("Servicio:", i + 1)

        print("==============================")

        print("Código:", codigos[i])

        print("Cliente:", clientes[i])

        print("DNI/RUC:", dnis[i])

        print("Lugar:", lugares[i])

        print("Proyecto:", proyectos[i])

        print("Trabajo realizado:", observaciones[i])

        print("Maquinaria:", maquinarias[i])

        print("Operador:", operadores[i])

        print("Fecha inicio:", fechas_inicio[i])

        print("Fecha fin:", fechas_fin[i])

        print("Horómetro inicial:",
              horometro_inicio[i])

        print("Horómetro final:",
              horometro_final[i])

        print("Horas máquina:",
              horas_maquina[i])

        print("Horas operador:",
              horas_operador[i])

        print("Tarifa hora:",
              tarifas[i])

        print("Gastos adicionales:",
              gastos_extra[i])

        print("Combustible:",
              galones_combustible[i],
              "galones")

        print("Costo total: S/.",
              costos[i])

# BUSCAR SERVICIO POR CODIGO

def buscar_servicio():

    codigo_buscar = input(
        "\nIngrese código del servicio: "
    )

    if codigo_buscar in codigos:
        i = codigos.index(codigo_buscar)
        print("\n===== SERVICIO ENCONTRADO =====")
        print("Cliente:",
              clientes[i])
        print("Proyecto:",
              proyectos[i])
        print("Lugar:",
              lugares[i])
        print("Maquinaria:",
              maquinarias[i])
        print("Operador:",
              operadores[i])
        print("Horas máquina:",
              horas_maquina[i])
        print("Horas operador:",
              horas_operador[i])
        print("Costo:",
              costos[i])
    else:
        print("\nServicio no encontrado.")

# CALCULAR COSTOS

def calcular_costos():

    if not costos:
        print("\nNo hay información.")
        return
    total = sum(costos)
    print("\n===== COSTOS GENERALES =====")
    print(
        "Cantidad de servicios:",
        len(costos)
    )

    print(
        "Total generado: S/.",
        total
    )

    print(
        "Promedio por servicio: S/.",
        total / len(costos)
    )

# GENERAR REPORTE GENERAL

def generar_reporte():

    if not codigos:
        print("\nNo existen servicios.")
        return
    print("\n===== REPORTE GENERAL =====")
    print(
        "Servicios realizados:",
        len(codigos)
    )

    print(
        "Horas máquina acumuladas:",
        sum(horas_maquina)
    )

    print(
        "Horas operador acumuladas:",
        sum(horas_operador)
    )

    print(
        "Ingresos totales: S/.",
        sum(costos)
    )

    mayor = max(costos)
    menor = min(costos)
    pos_mayor = costos.index(mayor)
    pos_menor = costos.index(menor)
    print("\n===== SERVICIO MAYOR COSTO =====")
    print(
        "Código:",
        codigos[pos_mayor]
    )

    print(
        "Cliente:",
        clientes[pos_mayor]
    )

    print(
        "Proyecto:",
        proyectos[pos_mayor]
    )

    print(
        "Costo:",
        mayor
    )

    print("\n===== SERVICIO MENOR COSTO =====")

    print(
        "Código:",
        codigos[pos_menor]
    )

    print(
        "Cliente:",
        clientes[pos_menor]
    )

    print(
        "Proyecto:",
        proyectos[pos_menor]
    )

    print(
        "Costo:",
        menor
    )
    print("\n===== MAQUINARIA UTILIZADA =====")

    contador_maquina = {}
    for maquina in maquinarias:

        if maquina in contador_maquina:
            contador_maquina[maquina] += 1
        else:
            contador_maquina[maquina] = 1

    for maquina, cantidad in contador_maquina.items():

        print(
            maquina,
            ":",
            cantidad,
            "servicio(s)"
        )

    print("\n===== SERVICIOS POR OPERADOR =====")

    contador_operador = {}
    for operador in operadores:

        if operador in contador_operador:
            contador_operador[operador] += 1
        else:
            contador_operador[operador] = 1

    for operador, cantidad in contador_operador.items():
        print(
            operador,
            ":",
            cantidad,
            "servicio(s)"
        )

# REGISTRAR COMBUSTIBLE

def registrar_combustible():
    if not codigos:
        print("\nNo existen servicios registrados.")
        return

    codigo = input(
        "\nIngrese código del servicio: "
    )

    if codigo in codigos:

        i = codigos.index(codigo)

        print("\n===== REGISTRO DE COMBUSTIBLE =====")

        while True:

            try:

                galones = float(
                    input("Cantidad de galones cargados: ")
                )

                if galones > 0:
                    break

                print("Debe ser mayor a cero.")

            except:

                print("Ingrese un número válido.")

        while True:

            try:
                horometro = float(
                    input("Horómetro al abastecimiento: ")
                )
                if horometro >= 0:
                    break
                print("Valor incorrecto.")
            except:
                print("Ingrese un número válido.")


        galones_combustible[i] = galones
        horometro_combustible[i] = horometro

        print("\nCombustible registrado correctamente.")

    else:

        print("\nCódigo no encontrado.")

# REGISTRAR MANTENIMIENTO

def registrar_mantenimiento():

    if not codigos:

        print("\nNo existen servicios registrados.")

        return

    codigo = input(
        "\nIngrese código del servicio: "
    )

    if codigo in codigos:

        i = codigos.index(codigo)

        print("\n===== INFORME DE MANTENIMIENTO =====")
        print("Ejemplo:")
        print("Cambio de aceite")
        print("Falla hidráulica")
        print("Avería mecánica")
        print("Incidente operativo")
        detalle = input(
            "\nIngrese detalle del mantenimiento: "
        )

        mantenimientos[i] = detalle
        print(
            "\nMantenimiento registrado correctamente."
        )
    else:

        print("\nCódigo no encontrado.")

# MOSTRAR MANTENIMIENTOS
def mostrar_mantenimientos():

    if not codigos:
        print("\nNo hay registros.")
        return

    print(
        "\n===== HISTORIAL DE MANTENIMIENTO ====="
    )

    for i in range(len(codigos)):
        print("\n----------------------------")
        print(
            "Código:",
            codigos[i]
        )
        print(
            "Maquinaria:",
            maquinarias[i]
        )
        print(
            "Detalle:",
            mantenimientos[i]
        )

# REGISTRAR DOCUMENTOS

def registrar_documentos():
    if not codigos:
        print("\nNo existen servicios.")
        return

    codigo = input(
        "\nIngrese código del servicio: "
    )
    if codigo in codigos:
        i = codigos.index(codigo)
        print("\n===== DOCUMENTACIÓN =====")
        print("Ejemplos:")
        print("- SOAT")
        print("- Seguro maquinaria")
        print("- Vida Ley")
        print("- Certificados")
        print("- Documentos legales")

        documento = input(
            "\nDocumento registrado: "
        )
        documentos[i] = documento
        print(
            "\nDocumento almacenado correctamente."
        )
    else:

        print("\nCódigo no encontrado.")

# MOSTRAR DOCUMENTOS

def mostrar_documentos():
    if not codigos:
        print("\nNo existen documentos.")
        return
    print(
        "\n===== DOCUMENTACIÓN REGISTRADA ====="
    )
    for i in range(len(codigos)):
        print("\n----------------------------")
        print(
            "Código:",
            codigos[i]
        )
        print(
            "Cliente:",
            clientes[i]
        )
        print(
            "Documento:",
            documentos[i]
        )

# REGISTRAR GASTOS ADICIONALES

def registrar_gasto():
    if not codigos:
        print("\nNo existen servicios.")
        return
    codigo = input(
        "\nIngrese código del servicio: "
    )
    if codigo in codigos:
        i = codigos.index(codigo)
        while True:
            try:
                gasto = float(
                    input(
                        "Nuevo gasto adicional: "
                    )
                )
                if gasto >= 0:
                    gastos_extra[i] = gasto
                    costos[i] = (
                        horas_maquina[i]
                        *
                        tarifas[i]
                    ) + gasto
                    break
                else:
                    print(
                        "El gasto no puede ser negativo."
                    )
            except:
                print(
                    "Ingrese un valor válido."
                )
        print(
            "\nGasto actualizado correctamente."
        )
    else:
        print(
            "\nCódigo no encontrado."
        )

# GUARDAR DATOS EN CSV

def guardar_datos():
    archivo = "servicios_serrbia.csv"
    with open(
        archivo,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)

        # ENCABEZADOS
        writer.writerow([

            "Codigo",
            "Cliente",
            "DNI_RUC",

            "Lugar",
            "Proyecto",
            "Observacion",

            "Maquinaria",
            "Operador",

            "Fecha_Inicio",
            "Fecha_Fin",

            "Horas_Maquina",
            "Horas_Operador",

            "Horometro_Inicial",
            "Horometro_Final",

            "Tarifa",

            "Costo",

            "Galones_Combustible",
            "Horometro_Combustible",

            "Mantenimiento",

            "Gasto_Extra",

            "Documentos"

        ])

        # DATOS

        for i in range(len(codigos)):
            writer.writerow([
                codigos[i],
                clientes[i],
                dnis[i],

                lugares[i],
                proyectos[i],
                observaciones[i],

                maquinarias[i],
                operadores[i],

                fechas_inicio[i],
                fechas_fin[i],

                horas_maquina[i],
                horas_operador[i],

                horometro_inicio[i],
                horometro_final[i],

                tarifas[i],
                costos[i],

                galones_combustible[i],
                horometro_combustible[i],

                mantenimientos[i],

                gastos_extra[i],

                documentos[i]
            ])
    print(
        "\nDatos guardados correctamente en:",
        archivo
    )

# CARGAR DATOS DESDE CSV

def cargar_datos():

    archivo = "servicios_serrbia.csv"

    if not os.path.exists(archivo):

        return
    with open(
        archivo,
        mode="r",
        newline="",
        encoding="utf-8"
    ) as file:

        lector = csv.reader(file)

        next(lector)

        for fila in lector:

            codigos.append(fila[0])
            clientes.append(fila[1])
            dnis.append(fila[2])
            lugares.append(fila[3])
            proyectos.append(fila[4])
            observaciones.append(fila[5])
            maquinarias.append(fila[6])
            operadores.append(fila[7])
            fechas_inicio.append(fila[8])
            fechas_fin.append(fila[9])
            horas_maquina.append(
                float(fila[10])
            )
            horas_operador.append(
                float(fila[11])
            )
            horometro_inicio.append(
                float(fila[12])
            )
            horometro_final.append(
                float(fila[13])
            )
            tarifas.append(
                float(fila[14])
            )
            costos.append(
                float(fila[15])
            )
            galones_combustible.append(
                float(fila[16])
            )
            horometro_combustible.append(
                float(fila[17])
            )
            mantenimientos.append(
                fila[18]
            )
            gastos_extra.append(
                float(fila[19])
            )
            documentos.append(
                fila[20]
            )

    print(
        "\nDatos cargados correctamente."
    )

# EDITAR SERVICIO

def editar_servicio():

    codigo = input(
        "\nIngrese código del servicio a editar: "
    )

    if codigo in codigos:
        i = codigos.index(codigo)
        print("\n===== EDITAR SERVICIO =====")
        clientes[i] = input(
            "Nuevo cliente: "
        )
        dnis[i] = input(
            "Nuevo DNI/RUC: "
        )
        lugares[i] = input(
            "Nuevo lugar de trabajo: "
        )
        proyectos[i] = input(
            "Nuevo proyecto: "
        )
        observaciones[i] = input(
            "Nueva descripción del trabajo: "
        )
        operadores[i] = input(
            "Nuevo operador: "
        )
        fechas_inicio[i] = input(
            "Nueva fecha inicio: "
        )
        fechas_fin[i] = input(
            "Nueva fecha fin: "
        )
        horas_maquina[i] = float(
            input(
                "Nuevas horas máquina: "
            )
        )
        horas_operador[i] = float(
            input(
                "Nuevas horas operador: "
            )
        )
        tarifas[i] = float(
            input(
                "Nueva tarifa por hora: "
            )
        )
        gastos_extra[i] = float(
            input(
                "Nuevo gasto adicional: "
            )
        )

        costos[i] = (
            horas_maquina[i]
            *
            tarifas[i]
        ) + gastos_extra[i]

        print(
            "\nServicio actualizado correctamente."
        )

    else:

        print(
            "\nCódigo no encontrado."
        )

# ELIMINAR SERVICIO

def eliminar_servicio():

    codigo = input(
        "\nIngrese código del servicio a eliminar: "
    )

    if codigo in codigos:
        i = codigos.index(codigo)
        codigos.pop(i)
        clientes.pop(i)
        dnis.pop(i)
        lugares.pop(i)
        proyectos.pop(i)
        observaciones.pop(i)
        maquinarias.pop(i)
        operadores.pop(i)
        fechas_inicio.pop(i)
        fechas_fin.pop(i)
        horas_maquina.pop(i)
        horas_operador.pop(i)
        horometro_inicio.pop(i)
        horometro_final.pop(i)
        tarifas.pop(i)
        costos.pop(i)
        galones_combustible.pop(i)
        horometro_combustible.pop(i)
        mantenimientos.pop(i)
        gastos_extra.pop(i)
        documentos.pop(i)

        print(
            "\nServicio eliminado correctamente."
        )

    else:

        print(
            "\nCódigo no encontrado."
        )

# BUSCAR POR CLIENTE

def buscar_cliente():

    nombre = input(
        "\nIngrese cliente a buscar: "
    )
    encontrado = False

    for i in range(len(clientes)):

        if clientes[i].lower() == nombre.lower():

            encontrado = True

            print("\n===== SERVICIO =====")

            print(
                "Código:",
                codigos[i]
            )

            print(
                "Proyecto:",
                proyectos[i]
            )
            print(
                "Lugar:",
                lugares[i]
            )
            print(
                "Costo:",
                costos[i]
            )


    if not encontrado:

        print(
            "\nNo se encontraron servicios."
        )

# BUSCAR POR MAQUINARIA

def buscar_maquinaria():

    maquina = input(
        "\nIngrese maquinaria: "
    )

    encontrado = False

    for i in range(len(maquinarias)):

        if maquinarias[i].lower() == maquina.lower():

            encontrado = True

            print("\n===== SERVICIO =====")

            print(
                "Código:",
                codigos[i]
            )

            print(
                "Cliente:",
                clientes[i]
            )

            print(
                "Operador:",
                operadores[i]
            )

            print(
                "Horas máquina:",
                horas_maquina[i]
            )

            print(
                "Costo:",
                costos[i]
            )

    if not encontrado:

        print(
            "\nNo existen registros."
        )

# BUSCAR POR OPERADOR

def buscar_operador():

    nombre = input(
        "\nIngrese operador: "
    )

    encontrado = False

    for i in range(len(operadores)):

        if operadores[i].lower() == nombre.lower():

            encontrado = True
            print("\n===== SERVICIO =====")

            print(
                "Código:",
                codigos[i]
            )

            print(
                "Cliente:",
                clientes[i]
            )

            print(
                "Maquinaria:",
                maquinarias[i]
            )

            print(
                "Horas trabajadas:",
                horas_operador[i]
            )

            print(
                "Costo:",
                costos[i]
            )

    if not encontrado:

        print(
            "\nNo existen servicios."
        )

# ORDENAR POR COSTO

def ordenar_por_costo():

    if not costos:

        print(
            "\nNo existen registros."
        )

        return


    datos = []

    for i in range(len(codigos)):

        datos.append([
            codigos[i],
            clientes[i],
            proyectos[i],
            costos[i]

        ])

    datos.sort(
        key=lambda x:x[3],
        reverse=True
    )

    print(
        "\n===== SERVICIOS ORDENADOS POR COSTO ====="
    )

    for dato in datos:

        print("--------------------")

        print(
            "Código:",
            dato[0]
        )

        print(
            "Cliente:",
            dato[1]
        )

        print(
            "Proyecto:",
            dato[2]
        )

        print(
            "Costo:",
            dato[3]
        )

# ORDENAR POR FECHA

def ordenar_por_fecha():

    if not codigos:
        print(
            "\nNo existen registros."
        )
        return

    datos = []

    for i in range(len(codigos)):

        datos.append([
            codigos[i],
            clientes[i],
            proyectos[i],
            fechas_inicio[i],
            costos[i]
        ])

    datos.sort(
        key=lambda x:x[3]
    )
    print(
        "\n===== SERVICIOS POR FECHA ====="
    )
    for dato in datos:
        print("--------------------")
        print(
            "Código:",
            dato[0]
        )
        print(
            "Cliente:",
            dato[1]
        )
        print(
            "Proyecto:",
            dato[2]
        )
        print(
            "Fecha:",
            dato[3]
        )
        print(
            "Costo:",
            dato[4]
        )

# EJECUCIÓN DEL SISTEMA

login()
cargar_datos()

while True:

    print("\n======================================")
    print("       SISTEMA SERRBIA S.A.C")
    print("======================================")

    print("1.  Registrar servicio")

    print("2.  Mostrar servicios")

    print("3.  Buscar servicio por código")

    print("4.  Calcular costos")

    print("5.  Generar reporte general")

    print("6.  Guardar datos")

    print("7.  Editar servicio")

    print("8.  Eliminar servicio")

    print("9.  Buscar por cliente")

    print("10. Buscar por maquinaria")

    print("11. Buscar por operador")

    print("12. Ordenar servicios por costo")

    print("13. Ordenar servicios por fecha")

    print("14. Registrar combustible")

    print("15. Registrar mantenimiento")

    print("16. Mostrar mantenimiento")

    print("17. Registrar documentos")

    print("18. Mostrar documentos")

    print("19. Registrar gasto adicional")

    print("20. Salir")

    opcion = input(
        "\nSeleccione una opción: "
    )

    if opcion == "1":

        registrar_servicio()

    elif opcion == "2":

        mostrar_servicios()

    elif opcion == "3":

        buscar_servicio()

    elif opcion == "4":

        calcular_costos()

    elif opcion == "5":

        generar_reporte()

    elif opcion == "6":

        guardar_datos()

    elif opcion == "7":

        editar_servicio()

    elif opcion == "8":

        eliminar_servicio()

    elif opcion == "9":

        buscar_cliente()

    elif opcion == "10":

        buscar_maquinaria()

    elif opcion == "11":

        buscar_operador()

    elif opcion == "12":

        ordenar_por_costo()

    elif opcion == "13":

        ordenar_por_fecha()

    elif opcion == "14":

        registrar_combustible()

    elif opcion == "15":

        registrar_mantenimiento()

    elif opcion == "16":

        mostrar_mantenimientos()

    elif opcion == "17":

        registrar_documentos()

    elif opcion == "18":

        mostrar_documentos()

    elif opcion == "19":

        registrar_gasto()

    elif opcion == "20":


        guardar_datos()


        print(
            "\nDatos guardados correctamente."
        )


        print(
            "Gracias por utilizar el Sistema SERRBIA S.A.C."
        )

        break

    else:


        print(
            "\nOpción inválida."
        )