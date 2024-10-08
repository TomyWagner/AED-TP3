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

def generar_archivo_binario(arch1, arch2):
    if not os.path.exists(arch1):
        print("El archivo", arch1, "no existe..")
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
        env = envio.Envio(codigo,dire,tipo_envio,forma_pago)
        pickle.dump(env,m)

    datos.close()
    m.close()

def main():
    v = []
    op = -1
    arch1 = "envios-tp4.csv"
    arch2 = "envios-tp4.dat"
    while op != 0:
        op = menu()

        if op == 1:
            generar_archivo_binario(arch1,arch2)
        if op == 2:
            pass
        if op == 3:
            pass
        if op == 4:
            pass
        if op == 5:
            pass
        if op == 6:
            pass
        if op == 7:
            pass
        if op == 8:
            pass
        if op == 0:
            print("El programa finalizó")

if __name__ == '__main__':
    main()