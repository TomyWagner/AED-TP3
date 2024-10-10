from envio import *
import pickle
import os
import random


def menu():

    a = "Menú de opciones\n"
    a += "1. Crear archivo\n"
    a += "2. Cargar datos\n"
    a += "3. Mostrar datos del registro\n"
    a += "4. Mostrar registros por Código Postal\n"
    a += "5. Buscar registro por Código Postal\n"
    a += "6. Mostrar cantidad de envíos por tipo y forma de pago\n"
    a += "7. Mostrar total de envíos por tipo y forma de pago\n"
    a += "8. Calcular y listar envíos con importe mayor al promedio\n"
    a += "0. Salir\n"

    print(a)
    opcion = int(input("Ingrese la opción que desee: "))

    return opcion


# PUNTO 1: 
def generar_archivo_binario(arch1, arch2):
    if not os.path.exists(arch1):
        print("El archivo", arch1, "no existe..")
        return

    if os.path.exists(arch2):
        print("Advertencia: el archivo binario", arch2, "ya existe.")
        respuesta = input("¿Desea sobrescribir el archivo? (s/n): ")
        if respuesta in 'sSnN':
            if respuesta == 'n' or respuesta == 'N':
                print("Operación cancelada. No se ha sobrescrito el archivo binario.")
                return
        else:
            print("Respuesta inválida. Operación cancelada.")
            return

    datos = open(arch1, "rt")

    timestamp = datos.readline()
    hd = datos.readline()

    m = open(arch2, "wb")
    for linea in datos:
        d = linea.split(",")
        codigo = d[0]
        dire = d[1]
        tipo_envio = int(d[2])
        forma_pago = int(d[3])
        env = Envio(codigo, dire, tipo_envio, forma_pago)
        pickle.dump(env, m)

    datos.close()
    m.close()

    print("Archivo binario creado correctamente desde el archivo CSV.")


# PUNTO 2 (TomyWagner): Cargar datos manualmente
def cargar_datos_manual(archivo_binario):
    if not os.path.exists(archivo_binario):
        archivo = open(archivo_binario, "wb")
        archivo.close()

    archivo = open(archivo_binario, "ab")

    codigo_postal = input("Ingrese el código postal del envío: ")
    direccion = input("Ingrese la dirección física del destino: ")
    tipo_envio = -1
    while (tipo_envio < 0) or (tipo_envio > 6):
        tipo_envio = int(input("Ingrese el tipo de envío (número entre 0 y 6): "))
    forma_pago = 0
    while (forma_pago != 1) and (forma_pago != 2):
        forma_pago = int(input("Ingrese la forma de pago (1 = efectivo, 2 = tarjeta de crédito): "))

    nuevo_envio = Envio(codigo_postal, direccion, tipo_envio, forma_pago)
    pickle.dump(nuevo_envio, archivo)
    archivo.close()
    print("El nuevo envío ha sido agregado correctamente.")


# PUNTO 3 (TomyWagner): Mostrar todos los registros del archivo binario
def mostrar_datos(archivo_binario):
    if not os.path.exists(archivo_binario):
        print("El archivo binario no existe. No hay datos que mostrar.")
        return

    archivo = open(archivo_binario, "rb")

    bandera_lectura = True
    while bandera_lectura == True:
        envio_leido = archivo.read(1)
        if envio_leido == b'':
            bandera_lectura = False
        else:
            archivo.seek(-1, 1)
            envio = pickle.load(archivo)
            
            es_numerico = True
            for caracter in envio.cp:
                if caracter not in '0123456789':
                    es_numerico = False

            if es_numerico and len(envio.cp) == 4:
                pais = "Argentina"
            else:
                pais = "Otro país"
            print(f"{envio} - País: {pais}")

    archivo.close()


def main():
    arch1 = "envios-tp4.csv"
    arch2 = "envios-tp4.dat"
    op = -1

    while op != 0:
        op = menu()

        if op == 1:
            generar_archivo_binario(arch1, arch2)
        elif op == 2:
            cargar_datos_manual(arch2)
        elif op == 3:
            mostrar_datos(arch2)
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 8:
            pass
        elif op == 0:
            print("El programa finalizó")

if __name__ == '__main__':
    main()
