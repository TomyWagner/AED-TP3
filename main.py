from envio import Envio


def cargar_envios():
    """ función para cargar los registros desde el archivo envíos.txt

        Parámetros
            registros (Envío[]): Es el arreglo de envíos
    """
    # FIXME hay un error al verificar
    # cuando se ingresan números y letras
    envios = []

    archivo = open("envios-tp3.txt")
    contenido = archivo.readlines()
    archivo.close()

    contandor_linea = 0
    for linea in contenido:
        contandor_linea += 1
        if contandor_linea == 1:
            continue

        envio = Envio()
        envio.codigo_postal = linea[0:8]
        envio.direccion = linea[9:28]
        envio.tipo_envio = int(linea[29])
        envio.forma_pago = int(linea[30])

        envios.append(envio)

    return envios


def menu():
    """ esta función muestra el menú, verifica el valor ingresado
         y lo devuelve. (Solo muestra las diferentes operaciones
         que puede hacer el programa).
    """

    print("1. Obtener registros desde un archivo")
    print("2. Cargar un envío")
    print("3. Mostrar envíos")
    print("4. Salir")
    opc = input("ingrese una opción: ")

    # verificación -----
    if opc == "":
        print("Seleccione una opción valida.")
        return

    elif opc.isalpha():
        print("La opción debe ser un valor numérico")
        return

    elif opc.isdigit():
        if int(opc) <= 0 or int(opc) >= 5:
            print("Seleccione una opción valida.")
            return
    # -----------------

    return int(opc)


if __name__ == "__main__":
    opc = 0
    envios = []

    while opc != 4:
        opc = menu()

        if opc == 1:
            # si el arreglo esta vacío
            # cargar datos
            if envios == []:
                envios = cargar_envios()
                print("\nRegistros cargados\n")

            # si el arreglo no esta vacío,
            # cancelar la operación o volver a cargar
            else:
                x = input("Seguro que quieres borrar los registros? (Ss/Nn): ")
                if x in 'Ss':
                    print("\nRegistros cargados\n")
                    envios = cargar_envios()
                if x in 'Nn':
                    print("\nOperación cancelada\n")

        elif opc == 2:
            print("Carga de datos")

            codigo_postal = input("Ingrese el código postal: ")
            direccion = input("Ingrese la dirección física: ")

            # valida el tipo de envío y la forma de pago --------

            # FIXME hay un error al poner números y letras juntos
            # creo que es porque la función isalpha devuelve True
            # solo si todos los caracteres son letras, lo mismo pasa
            # con isdigit.
            tipo_envio = input("Ingrese el tipo de envío (del 0 al 6): ")
            while tipo_envio.isalpha() or (tipo_envio.isdigit() and (int(tipo_envio) <= -1 or int(tipo_envio) >= 7)):
                print("Error")
                tipo_envio = input("Ingrese el tipo de envío (del 0 al 6): ")

            forma_pago = input("Ingrese el tipo de envío (del 1 al 2): ")
            while forma_pago.isalpha() or (forma_pago.isdigit() and (int(forma_pago) <= 0 or int(forma_pago) >= 3)):
                print("Error")
                forma_pago = input("Ingrese el tipo de envío (del 1 al 2): ")
            # ---------------------------------------------------

            envio = Envio()
            envio.codigo_postal = codigo_postal
            envio.direccion = direccion
            envio.tipo_envio = tipo_envio
            envio.forma_pago = forma_pago

            # agrega el envío al final del arreglo
            envios.append(envio)

            # código de prueba
            print("\n\n")
            for e in envios:
                e.mostrar_info()

        elif opc == 3:
            # TODO muestra los objetos del arreglo, ordenados por
            # código postal, de menor a mayor.
            # Cada registro debe ocupar una sola linea en pantalla, y debe
            # mostrarse también el nombre del país que corresponde cada
            # código postal
            # Agregar la posibilidad de que el usuario elija si quiere
            # mostrar todos los registros, o mostrar solo los m primeros
            # cargando m por teclado
            print("\n\nSeleccionó la opción número 3\n\n")

    print("El programa finalizó correctamente.")
