from envio import Envio


def cargar_envios(registros):
    archivo = open("envios-tp3.txt")
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

        # funcion de prueba
        # envio.mostrar_info()


def menu():
    print("1. Obtener registros desde un archivo")
    print("2. Cargar un envío")
    print("3. Salir")
    opc = input("ingrese una opción: ")

    if opc.isalpha():
        print("La opción debe ser un valor numérico")
        return

    elif opc.isnumeric():
        if int(opc) <= 0 or int(opc) >= 4:
            print("Seleccione una opción valida.")
            return

    return int(opc)


if __name__ == "__main__":
    opc = 0
    registros = []

    while opc != 3:
        opc = menu()

        if opc == 1:
            # TODO
            print("\n\nSeleccionó la opcion número 1\n\n")
        elif opc == 2:
            # TODO
            print("\n\nSeleccionó la opcion número 2\n\n")

    print("El programa finalizó")
