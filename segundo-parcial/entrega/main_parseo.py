# -*- coding: utf-8 -*-
from __future__ import print_function
from parseo import proceso
import random

separador = '='*50
def iniciar():
    continuar = True
    while continuar:
        opcion = imprimir_menu()
        if opcion == 1:
            entrada_consola()
        elif opcion == 2:
            ejecutar_random()
        else:
            break
        print('=' * 100)
        opcion = input("Reintentar [s/n]: ")
        if opcion.lower() != 's':
            continuar = False

    print('Saliendo del programa...')

def imprimir_menu():
    print('\n\n%sMenu%s' % (separador, separador))
    print("""
        1.- Entrada en consola (Manual)
        2.- Aleatorio (Automatico)
        3.- Salir
    """)
    try:
        opcion = int(input("Selecciona una opcion valida: "))
        return opcion
    except Exception as e:
        print('Error ', e)
        return 0

def entrada_consola():
    texto = input("Escribe la cadena de parentesis: ")
    proceso(texto)

def ejecutar_random():
    i = 0
    longitud_random = random.randint(1, 1000)
    cadena = ''
    while i < longitud_random:
        cadena += random.choice(['(', ')'])
        i += 1

    print("La cadena es: ", cadena)
    proceso(cadena)

iniciar()
