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

        envio.obtener_codigo_postal(linea)
        envio.obtener_direccion(linea)
        envio.obtener_tipo_envio(linea)
        envio.obtener_forma_pago(linea)

        envios.append(envio)

    return envios


def menu():
    """ esta función sirve de menú, verifica el valor ingresado
         y lo devuelve. (Solo muestra las diferentes operaciones
         que puede hacer el programa).
    """
    # Debe haber una mejor forma de hacer esto.

    print("1. Obtener registros desde un archivo")
    print("2. Cargar un envío")
    print("3. Mostrar envíos")
    print("4. Salir")
    opc = input("ingrese una opción: ")

    if opc == "":
        print("Seleccione una opción valida.")
        return

    if opc.isalpha():
        print("La opción debe ser un valor numérico")
        return

    elif opc.isnumeric():
        if int(opc) <= 0 or int(opc) >= 5:
            print("Seleccione una opción valida.")
            return

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

            # si el arreglo no esta vacío
            # cancelar la operación o volver a cargar
            else:
                x = input("Seguro que quieres borrar los registros? (Ss/Nn): ")
                print("\n")
                if x in 'Ss':
                    envios = cargar_envios()
                print("\nRegistros cargados\n")
                if x in 'Nn':
                    print("\nOperación cancelada\n")

        elif opc == 2:
            # TODO cargar por teclado los datos de envío, aplicando procesos
            # de validación para los campos tipo de envío y forma de pago,
            # agregar un objeto con esos datos al arreglo.
            # Cada vez que se elija esta opción, EL NUEVO REGISTRO DEBE
            # AGREGARSE AL FINAL DEL ARREGLO.
            #
            # Si se elige esta opción, los datos anteriores
            # deben ser MANTENIDOS en el arreglo sin importar si fueron
            # originalmente cargados desde el archivo o fueron cargados
            # manualmente desde esta misma opción
            print("\n\nSeleccionó la opción número 2\n\n")
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
