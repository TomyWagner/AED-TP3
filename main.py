from envio import Envio


def cargar_envios(registros):
    """ función para cargar los registros desde el archivo envíos.txt

        Parámetros
            registros (Envío[]): Es el arreglo de envíos
    """
    # FIXME hay un error al verificar
    # cuando se ingresan números y letras

    archivo = open("envíos-tp3.txt")
    contenido = archivo.readlines()
    archivo.close()

    contandor_line = 0
    for line in contenido:
        contandor_line += 1

        if contandor_line == 1:
            continue

        envio = Envio()

        envio.obtener_codigo_postal(line)
        envio.obtener_direccion(line)
        envio.obtener_tipo_envio(line)
        envio.obtener_forma_pago(line)

        # función para probar que se carguen
        # correctamente los datos
        # envio.mostrar_info()


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
    registros = []

    while opc != 4:
        opc = menu()

        if opc == 1:
            # TODO crear el arreglo con los envíos guardados
            # en el archivo envíos.txt
            #
            # Cada vez que se elija esta opción, el arreglo debe ser
            # creado de nuevo desde cero eliminando el anterior
            print("\n\nSeleccionó la opción número 1\n\n")
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
