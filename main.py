from envio import Envio


def cargar_envios(): # SIN MODIFICACIÓN (Agus)
    """
    PUNTO 1 (Agus): Crear el arreglo de registros/objetos desde un archivo.
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


def menu(): # MODIFICADO (TomyWagner): Opciones agregadas y cambio de verificación
    """
    MENÚ (Agus): Función que muestra el menú, verifica el valor ingresado y lo devuelve.
    """
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

    # MODIFICACIÓN (TomyWagner): Verificación acortada
    if opc.isdigit() and 1 <= int(opc) <= 10:
        return int(opc)
    else:
        print("Seleccione una opción válida.")
        return None


def buscar_por_direccion_y_tipo(envios, direccion, tipo_envio): # NUEVO (TomyWagner): PTO. 4
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


def buscar_por_codigo_postal(envios, codigo_postal): # NUEVO (TomyWagner): PTO. 5
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
            # Cambiar la forma de pago (1 a 2 y 2 a 1)
            if envio.forma_pago == 1:
                envio.forma_pago = 2
            else:
                envio.forma_pago = 1
            envio.mostrar_info()
            return True
    print("No se encontró un envío con ese código postal.")
    return False


# Función AUXILIAR para calcular el importe inicial de un envío
def calcular_importe_inicial(envio): # NUEVO (TomyWagner): TABLA DE PRECIOS 
    """
    Calcula el importe inicial según el tipo de envío y el destino.
    """
    # Precios simplificados por tipo de envío
    precios = [1100, 1800, 2450, 8300, 10900, 14300, 17900]
    return precios[envio.tipo_envio]


def mostrar_envios(envios): # NUEVO (TomyWagner): PTO. 3
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


def contar_envios_validos_por_tipo(envios, tipo_control): # NUEVO (TomyWagner): PTO. 6
    """
    PUNTO 6: 
    Si el tipo de control de direcciones en la timestamp era HC, entonces determinar la cantidad
    de envíos que tengan dirección de envío válida, realizados para cada uno de los siete tipos
    de envios posibles. Pero si el tipo de control de direcciones era SC, entonces determine
    la cantidad de envíos de cada uno de los siete tipos posibles, sin importar si la dirección 
    de envío era válida o no. Observación: ni siquiera se les ocurra plantear un esquema de 7
    condiciones y siete contadores separados... Esto se resuelve con un vector de conteo o nada...
    """
    contador = [0] * 7  # Inicializar un contador para los 7 tipos de envío

    for envio in envios:
        if tipo_control == "HC":
            if validar_direccion(envio.direccion):
                contador[envio.tipo_envio] += 1
        else:  # tipo_control == "SC"
            contador[envio.tipo_envio] += 1

    for i in range(7):
        print(f"Tipo de envío {i}: {contador[i]} envíos")


# Función AUXILIAR para validar la dirección (para el control HC)
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
        if '0' <= char <= '9':
            tiene_digitos = True

        # Verificar si hay dos mayúsculas seguidas
        if 'A' <= char <= 'Z' and i > 0:
            char_anterior = direccion[i - 1]
            if 'A' <= char_anterior <= 'Z':
                no_mayusculas_seguidas = False

    # La dirección es válida si tiene dígitos y no hay mayúsculas seguidas
    if tiene_digitos and no_mayusculas_seguidas:
        return True
    else:
        return False


def main(): # MODIFICADO (TomyWagner): Todas las opciones agregadas
    opc = 0
    envios = []
    tipo_control = "HC"  # MODIFICACIÓN (TomyWagner): Por defecto el tipo de control es "HC"

    while opc != 10:
        opc = menu()

        if opc is None:
            continue

        if opc == 1: # PUNTO 1: Cargar datos desde el archivo y crear el arreglo de envíos
            if not envios:  # MODIFICACIÓN (TomyWagner): Cargar los datos para arreglo vacío
                envios = cargar_envios()
                print("\nRegistros cargados\n")
            else:
                x = input("Seguro que quieres borrar los registros? (Ss/Nn): ")
                if x in 'Ss':
                    print("\nRegistros recargados\n")
                    envios = cargar_envios()
                if x in 'Nn':
                    print("\nOperación cancelada\n")

        elif opc == 2: # PUNTO 2: Cargar un envío manualmente
            print("Carga de datos")

            codigo_postal = input("Ingrese el código postal: ").strip()
            direccion = input("Ingrese la dirección física: ").strip()

            tipo_envio = input("Ingrese el tipo de envío (0 al 6): ")
            while not (tipo_envio.isdigit() and 0 <= int(tipo_envio) <= 6):
                print("Tipo de envío inválido.")
                tipo_envio = input("Ingrese el tipo de envío (0 al 6): ")

            forma_pago = input("Ingrese la forma de pago (1: efectivo, 2: tarjeta): ")
            while not (forma_pago.isdigit() and 1 <= int(forma_pago) <= 2):
                print("Forma de pago inválida.")
                forma_pago = input("Ingrese la forma de pago (1: efectivo, 2: tarjeta): ")

            envio = Envio()
            envio.codigo_postal = codigo_postal
            envio.direccion = direccion
            envio.tipo_envio = int(tipo_envio)
            envio.forma_pago = int(forma_pago)

            envios.append(envio)
            print("\nEnvío cargado exitosamente.\n")

        elif opc == 3:  # Mostrar los envíos ordenados por código postal (Según TP: Selección Simple, no Shellsort)
            mostrar_envios(envios)

        elif opc == 4: # Punto 4: Buscar por dirección y tipo de envío
            direccion = input("Ingrese la dirección a buscar: ").strip()
            tipo_envio = input("Ingrese el tipo de envío (0 al 6): ")

            while not (tipo_envio.isdigit() and 0 <= int(tipo_envio) <= 6):
                print("Tipo de envío inválido.")
                tipo_envio = input("Ingrese el tipo de envío (0 al 6): ")
            
            buscar_por_direccion_y_tipo(envios, direccion, int(tipo_envio))

        elif opc == 5: # Punto 5: Buscar por código postal y cambiar forma de pago
            codigo_postal = input("Ingrese el código postal a buscar: ").strip()
            buscar_por_codigo_postal(envios, codigo_postal)

        elif opc == 6: # Punto 6: Contar envíos válidos por tipo
            contar_envios_validos_por_tipo(envios, tipo_control)

        elif opc == 7: # Punto 7: Calcular el importe final acumulado por tipo de envío
            pass

        elif opc == 8: # Punto 8: Determinar el tipo de envío con mayor importe final acumulado
            pass

        elif opc == 9: # Punto 9: Calcular el importe final promedio y envíos menores a ese promedio
            pass

    print("El programa finalizó correctamente.")


if __name__ == "__main__":
    main()
