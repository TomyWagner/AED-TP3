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


if __name__ == "__main__":
    registros = []

    cargar_envios(registros)
