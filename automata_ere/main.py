# -*- coding: utf-8 -*-
from __future__ import print_function
from automata_ere import automata

def iniciar():
    continuar = True
    while continuar:
        print("""
            1.- Entrada en consola
            2.- Ingresar nombre del archivo
        """)
        opcion = int(input("Selecciona una opcion: "))
        if opcion == 1:
            texto = input("Escribe el texto: ")
            entrada_consola(texto)
        elif opcion == 2:
            archivo = input("Ingresa el nombre del archivo: ")
            entrada_archivo(archivo)
        else:
            print("Error")
            continuar = False
        opcion = input("Reintentar s/n: ")
        if opcion.lower() != 's':
            continuar = False


def entrada_consola(texto):
    texto += ' '
    palabras_ere = automata(texto)
    print(palabras_ere)

def entrada_archivo(archivo):
    archivo_abierto = open(archivo, 'r')
    linea_palabras = []
    num_linea = 0
    palabras_ere = []
    for linea in archivo_abierto.read().split('\n'):
        linea += ' '
        palabras_ere = automata(linea)
        linea_palabras.append({'Numero linea': num_linea, 'Palabras': palabras_ere})
        num_linea += 1

    imprimir_archivo(linea_palabras)

def imprimir_archivo(linea_palabras):
    print(linea_palabras)


iniciar()
