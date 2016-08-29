# -*- coding: utf-8 -*-
from __future__ import print_function

def iniciar():
    continuar = 1
    while continuar == 1:
        print("""
            1.- Entrada en consola
            2.- Ingresar nombre del archivo
        """)
        opcion = int(input("Selecciona una opcion: "))
        if opcion == 1:
            texto = input("Escribe el texto: ")
            type(texto)
            print(texto)
            entrada_consola(texto)
        elif opcion == 2:
            archivo = input("Ingresa el nombre del archivo: ")
            entrada_archivo(archivo)
        else:
            print("Error")
            continuar = False
        continuar = int(input("Reintentar 1=si 0=no"))


def entrada_consola(texto):
    for x in texto:
        if (ord(x)<123 and ord(x) > 96):
            estado = estados_automata()
        else:
            print("no es ", x)

iniciar()
