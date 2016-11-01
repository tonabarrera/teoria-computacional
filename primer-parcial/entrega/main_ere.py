#main_ere.py
# -*- coding: utf-8 -*-
from __future__ import print_function
from automata_ere import verificar_palabras
from diagrama_ere import Diagrama

separador = '*'*50

def iniciar():
    continuar = True
    while continuar:
        opcion = imprimir_menu()
        if opcion == 1:
            entrada_consola()
        elif opcion == 2:
            entrada_archivo()
        elif opcion == 3:
            ver_diagrama()
        else:
            break
        print('*' * 100)
        opcion = input("Reintentar s/n: ")
        if opcion.lower() != 's':
            continuar = False

    print('Saliendo del programa...')

def imprimir_menu():
    print("""Es importante mencionar que en este programa cualquier simbolo que no sea una letra en el alfabeto inglés separa una palabra de otra""")
    print('\n\n%sMenu%s' % (separador, separador))
    print("""
        1.- Entrada en consola
        2.- Ingresar nombre del archivo
        3.- Ver diagrama de estados
        4.- Salir
    """)
    try:
        opcion = int(input("Selecciona una opcion valida: "))
        return opcion
    except Exception as e:
        print('Error ', e)
        return 0

def entrada_consola():
    texto = input("Escribe el texto: ")
    texto += ' '
    palabras_ere = []
    verificar_palabras(texto, palabras_ere)
    print('\n', palabras_ere)

def entrada_archivo():
    archivo = input("Ingresa el nombre del archivo: ")
    try:
        archivo_abierto = open(archivo, 'r')
    except Exception as e:
        print('Error al abrir archivo: ', e)
        return 0

    linea_palabras = []
    num_linea = 1
    palabras_ere = []
    posiciones = []
    for linea in archivo_abierto:
        verificar_palabras(linea, palabras_ere, posiciones)
        linea_palabras.append({'Linea': num_linea, 'Palabras': palabras_ere, 'Posiciones': posiciones})
        num_linea += 1
        palabras_ere = []
        posiciones = []

    imprimir_archivo(linea_palabras)
    archivo_abierto.close()

def imprimir_archivo(linea_palabras):
    print('\n\n')
    for elemento in linea_palabras:
        if len(elemento['Palabras']) > 0:
            print('Numero de linea: ', elemento['Linea'])
            i = 0
            for palabra in elemento['Palabras']:
                print('\tPalabra: %s No. Palabra: %s' % (palabra, elemento['Posiciones'][i]))
                i += 1

def ver_diagrama():
    print('Mostrando diagrama del automata. Cierre la ventana para continuar')
    try:
        diagrama_ere = Diagrama()
        diagrama_ere.master.title('Diagrama del automata ere')
        diagrama_ere.mainloop()
    except Exception as e:
        print("Error", e)

iniciar()
