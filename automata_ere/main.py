# -*- coding: utf-8 -*-
from __future__ import print_function
from automata_ere import automata

def iniciar():
    continuar = True
    while continuar:
        opcion = imprimir_menu()
        if opcion == 1:
            texto = input("Escribe el texto: ")
            entrada_consola(texto)
        elif opcion == 2:
            archivo = input("Ingresa el nombre del archivo: ")
            entrada_archivo(archivo)
        elif opcion == 3:
            print('Aqui va el grafico')
        else:
            print("Error")
            return 0
        print('*' * 50)
        opcion = input("Reintentar s/n: ")
        if opcion.lower() != 's':
            continuar = False

def imprimir_menu():
    print('\n\n**********Menu**********')
    print("""
        1.- Entrada en consola
        2.- Ingresar nombre del archivo
        3.- Ver diagrama de estados
    """)
    opcion = int(input("Selecciona una opcion: "))

    return opcion

def entrada_consola(texto):
    texto += ' '
    palabras_ere = automata(texto)
    print()
    print(palabras_ere)

def entrada_archivo(archivo):
    archivo_abierto = open(archivo, 'r')
    linea_palabras = []
    num_linea = 1
    palabras_ere = []
    for linea in archivo_abierto.read().split('\n'):
        linea += ' '
        palabras_ere = automata(linea)
        linea_palabras.append({'Linea': num_linea, 'Palabras': palabras_ere})
        num_linea += 1
    archivo_abierto.close()
    imprimir_archivo(linea_palabras)

def imprimir_archivo(linea_palabras):
    print('\n\n')
    for elemento in linea_palabras:
        if len(elemento['Palabras'])>0:
            print('Numero de linea: %s Palabras encontradas %s' % (elemento['Linea'], elemento['Palabras']))


iniciar()
