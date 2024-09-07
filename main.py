from envio import Envio


def cargar_envios(): # SIN MODIFICACIÓN
    """
    PUNTO 1:
    Crear el arreglo de registros/objetos desde un archivo.
    Función para cargar los envíos desde el archivo 'envios-tp3.txt'.
    Los registros se almacenan en un arreglo de objetos Envio.
    """
    envios = []

    # Se abre el archivo y obtienen las líneas
    archivo = open("envios-tp3.txt")
    contenido = archivo.readlines()
    archivo.close()

    contador_linea = 0
    for linea in contenido:
        contador_linea += 1
        if contador_linea == 1:  # Saltar la primera línea (el timestamp)
            continue

        envio = Envio()
        envio.codigo_postal = linea[0:8]  # Extraer código postal
        envio.direccion = linea[9:28]  # Extraer dirección física
        envio.tipo_envio = int(linea[29])  # Extraer tipo de envío
        envio.forma_pago = int(linea[30])  # Extraer forma de pago

        envios.append(envio)  # Añadir objeto al arreglo

    return envios


def menu(): # MODIFICADO: Opciones agregadas y cambio de verificación
    print("1. Obtener registros desde un archivo")
    print("2. Cargar un envío")
    print("3. Mostrar envíos")
    print("4. Buscar por dirección y tipo de envío")
    print("5. Buscar por código postal y cambiar forma de pago")
    print("6. Determinar cantidad de envíos válidos por tipo")
    print("7. Determinar importe final acumulado por tipo de envío")
    print("8. Determinar tipo de envío con mayor importe acumulado")
    print("9. Calcular importe final promedio y envíos menores a ese promedio")
    print("10. Salir")
    opc = input("Ingrese una opción: ")

    # MODIFICADO: Verificación final
    if opc.isdigit():
        opc = int(opc)
        if opc >= 1 and opc <= 10:
            return opc
    print("Seleccione una opción válida.")
    return None


def buscar_por_direccion_y_tipo(envios, direccion, tipo_envio): # PTO. 4
    """
    PUNTO 4: 
    Buscar si existe en el arreglo un registro/objeto cuya dirección de envío sea igual 
    a "d" y que sea del tipo de envío "e", siendo "d" y "e" dos valores que se cargan por teclado. 
    Si existe, mostrar todos sus datos. Si no existe indicar con un mensaje. La búsqueda debe 
    detenerse al encontrar el primer registro/objeto que coincida con el criterio pedido.
    """
    for envio in envios:
        if envio.direccion == direccion and envio.tipo_envio == tipo_envio:
            envio.mostrar_info()
            return True
    print("No se encontró un envío con esa dirección y tipo.")
    return False


def buscar_por_codigo_postal(envios, codigo_postal): # PTO. 5
    """
    PUNTO 5: 
    Buscar si existe en el arreglo un registro/objeto cuyo código postal sea igual a cp,
    siendo cp un valor que se carga por teclado. Si existe, cambiar el valor del campo forma de
    pago, de forma que pase a valer el valor contrario (si valía 1, que pase a valer 2, y
    viceversa), y luego mostrar el registro completo modificado. Si no existe indicar con un
    mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el 
    criterio pedido.
    """
    for envio in envios:
        if envio.codigo_postal == codigo_postal:
            # Cambiar la forma de pago (1 a 2, y 2 a 1)
            if envio.forma_pago == 1:
                envio.forma_pago = 2
            else:
                envio.forma_pago = 1
            envio.mostrar_info()
            return True
    print("No se encontró un envío con ese código postal.")
    return False


# Función AUXILIAR para calcular el importe inicial de un envío
def calcular_importe_inicial(envio): # TABLA DE PRECIOS 
    """
    Calcula el importe inicial según el tipo de envío y el destino.
    """
    # Precios simplificados por tipo de envío
    precios = [1100, 1800, 2450, 8300, 10900, 14300, 17900]
    return precios[envio.tipo_envio]


def mostrar_envios(envios): # PTO. 3
    n = len(envios)
    # Algoritmo de Selección Simple para ordenar los envíos por código postal
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if envios[j].codigo_postal < envios[minimo].codigo_postal:
                minimo = j
        # Intercambiar el mínimo con el primer elemento no ordenado
        envios[i], envios[minimo] = envios[minimo], envios[i]

    # Mostrar los envíos ordenados
    for envio in envios:
        envio.mostrar_info()


def contar_envios_validos_por_tipo(envios, tipo_control): # PTO. 6
    """
    PUNTO 6: 
    Si el tipo de control de direcciones en la timestamp era HC, entonces determinar la cantidad
    de envíos que tengan dirección de envío válida, realizados para cada uno de los siete tipos
    de envios posibles. Pero si el tipo de control de direcciones era SC, entonces determine
    la cantidad de envíos de cada uno de los siete tipos posibles, sin importar si la dirección 
    de envío era válida o no.
    """
    contador = [0] * 7  # Inicializar un contador para 7 tipos de envío

    for envio in envios:
        if tipo_control == "HC":
            if validar_direccion(envio.direccion):
                contador[envio.tipo_envio] += 1
        else:  # tipo_control == "SC"
            contador[envio.tipo_envio] += 1

    for i in range(7):
        print(f"Tipo de envío {i}: {contador[i]} envíos")


def validar_direccion(direccion):
    """
    Valida una dirección según las reglas del control HC (Hard Control).
    Se requiere que la dirección tenga solo letras y dígitos, sin dos mayúsculas seguidas,
    y que haya al menos una palabra compuesta solo por dígitos.
    """

    tiene_digitos = False
    no_mayusculas_seguidas = True

    # RecorreR la dirección por caracter
    for i in range(len(direccion)):
        char = direccion[i]
        # Verificar si hay dígitos
        if char >= '0' and char <= '9':
            tiene_digitos = True
        # Verificar si hay dos mayúsculas seguidas
        if char >= 'A' and char <= 'Z' and i > 0:
            char_anterior = direccion[i - 1]
            if char_anterior >= 'A' and char_anterior <= 'Z':
                no_mayusculas_seguidas = False
    # La dirección es válida si tiene dígitos y no hay mayúsculas seguidas
    if tiene_digitos == True and no_mayusculas_seguidas == True:
        return True
    else:
        return False


def calcular_importe_acumulado_por_tipo(envios, tipo_control): # PTO. 7
    """
    PUNTO 7:
    Si el tipo de control de direcciones en la timestamp era HC, entonces determinar el importe
    final acumulado por pagos de envíos que tengan dirección de envío válida, realizados para
    cada uno de los siete posibles tipos de envío (un acumulador por cada uno de los siete tipos).
    Pero si el tipo de control de direcciones era SC, entonces el importe final acumulado de cada
    uno de los siete tipos posibles, sin importar si la dirección de envío era válida o no.
    """
    acumulador = [0] * 7  # Inicializar acumulador para 7 tipos de envío

    for envio in envios:
        importe_inicial = calcular_importe_inicial(envio)
        if envio.forma_pago == 1:  # Descuento por EFECTIVO
            importe_final = int(importe_inicial * 0.9)
        else:
            importe_final = importe_inicial

        if tipo_control == "HC":
            if validar_direccion(envio.direccion):
                acumulador[envio.tipo_envio] += importe_final
        else:  # tipo_control == "SC"
            acumulador[envio.tipo_envio] += importe_final

    for i in range(7):
        print("Tipo de envío", i, ":", acumulador[i], "acumulados")

    return acumulador


def determinar_mayor_importe_acumulado(acumulador): # PTO. 8
    """
    PUNTO 8:
    En base al resultado obtenido en el punto 7, determinar y mostrar cuál fue el tipo de
    envío con mayor importe final acumulado, e indicar además qué porcentaje representa ese monto
    mayor sobre el monto total.
    """
    total_acumulado = 0
    max_importe = acumulador[0]
    tipo_mayor = 0

    # Calcular el total acumulado y el mayor importe
    for i in range(len(acumulador)):
        total_acumulado += acumulador[i]
        if acumulador[i] > max_importe:
            max_importe = acumulador[i]
            tipo_mayor = i

    if total_acumulado == 0:
        print("No hay importes acumulados.")
        return

    porcentaje = (max_importe / total_acumulado) * 100

    print("El tipo de envío con mayor importe acumulado es el tipo", tipo_mayor, "con $", max_importe)
    print("Este importe representa el", porcentaje, "% del total acumulado.")


def calcular_importe_promedio(envios): # PTO. 9
    """
    PUNTO 9:
    Calcular y mostrar el importe final promedio entre todos los envíos del arreglo, e informar
    además cuántos de los envíos tuvieron un importe menor a ese promedio.
    """
    total_importe = 0
    cantidad_envios = len(envios)
    importes_finales = []

    # Calcular el total y guardar los importes finales en una lista
    for envio in envios:
        importe_inicial = calcular_importe_inicial(envio)
        if envio.forma_pago == 1:  # Aplicar 10% de descuento por EFECTIVO
            importe_final = int(importe_inicial * 0.9)
        else:
            importe_final = importe_inicial
        
        total_importe += importe_final
        importes_finales.append(importe_final)

    if cantidad_envios == 0:
        print("No hay envíos para calcular el promedio.")
        return

    # Calcular el promedio
    promedio = total_importe / cantidad_envios
    menores_al_promedio = 0

    # Contar los envíos menores al promedio
    for importe in importes_finales:
        if importe < promedio:
            menores_al_promedio += 1

    print("El importe final promedio es: $", promedio)
    print("Cantidad de envíos con importe menor al promedio:", menores_al_promedio)


def main(): # Todas las opciones agregadas
    opc = 0
    envios = []
    tipo_control = "HC"  # Por defecto el tipo de control es "HC"
    acumulador = []

    while opc != 10:
        opc = menu()

        if opc == None:
            continue

        if opc == 1: # PUNTO 1: Cargar datos desde el archivo y crear el arreglo de envíos
            if len(envios) == 0:  # Cargar los datos para arreglo vacío
                envios = cargar_envios()
                print("\nRegistros cargados\n")
            else:
                x = input("Seguro que quieres borrar los registros? (Ss/Nn): ")
                if x == 'S' or x == 's':
                    print("\nRegistros recargados\n")
                    envios = cargar_envios()
                elif x == 'N' or x == 'n':
                    print("\nOperación cancelada\n")

        elif opc == 2: # PUNTO 2: Cargar un envío manualmente
            print("Carga de datos")

            codigo_postal = input("Ingrese el código postal: ").strip()
            direccion = input("Ingrese la dirección física: ").strip()

            tipo_envio = input("Ingrese el tipo de envío (0 al 6): ")
            while tipo_envio.isdigit() == False or int(tipo_envio) < 0 or int(tipo_envio) > 6:
                print("Tipo de envío inválido.")
                tipo_envio = input("Ingrese el tipo de envío (0 al 6): ")

            forma_pago = input("Ingrese la forma de pago (1: efectivo, 2: tarjeta): ")
            while forma_pago.isdigit() == False or int(forma_pago) < 1 or int(forma_pago) > 2:
                print("Forma de pago inválida.")
                forma_pago = input("Ingrese la forma de pago (1: efectivo, 2: tarjeta): ")

            envio = Envio()
            envio.codigo_postal = codigo_postal
            envio.direccion = direccion
            envio.tipo_envio = int(tipo_envio)
            envio.forma_pago = int(forma_pago)

            envios.append(envio)
            print("\nEnvío cargado exitosamente.\n")

        elif opc == 3:  # Mostrar los envíos ordenados por código postal (Selección Simple)
            mostrar_envios(envios)

        elif opc == 4: # Punto 4: Buscar por dirección y tipo de envío
            direccion = input("Ingrese la dirección a buscar: ").strip()
            tipo_envio = input("Ingrese el tipo de envío (0 al 6): ")

            while tipo_envio.isdigit() == False or int(tipo_envio) < 0 or int(tipo_envio) > 6:
                print("Tipo de envío inválido.")
                tipo_envio = input("Ingrese el tipo de envío (0 al 6): ")
            
            buscar_por_direccion_y_tipo(envios, direccion, int(tipo_envio))

        elif opc == 5: # Punto 5: Buscar por código postal y cambiar forma de pago
            codigo_postal = input("Ingrese el código postal a buscar: ").strip()
            buscar_por_codigo_postal(envios, codigo_postal)

        elif opc == 6: # Punto 6: Contar envíos válidos por tipo
            contar_envios_validos_por_tipo(envios, tipo_control)

        elif opc == 7: # Punto 7: Calcular el importe final acumulado por tipo de envío
            acumulador = calcular_importe_acumulado_por_tipo(envios, tipo_control)

        elif opc == 8: # Punto 8: Determinar el tipo de envío con mayor importe final acumulado
            if len(acumulador) > 0:  # Verificar si ya se ha calculado el acumulador
                determinar_mayor_importe_acumulado(acumulador)
            else:
                print("Primero debe calcular el importe acumulado (Opción 7).")

        elif opc == 9: # Punto 9: Calcular el importe final promedio y envíos menores a ese promedio
            calcular_importe_promedio(envios)

    print("El programa finalizó correctamente.")


if __name__ == "__main__":
    main()
