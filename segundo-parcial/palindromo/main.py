# -*- coding: utf-8 -*-
from __future__ import print_function
from palindromo import palindromo
import random

separador = '='*50

def main():
    continuar = True
    while continuar:
        opcion = imprimir_menu()
        if opcion == 1:
            entrada_consola()
        elif opcion == 2:
            entrada_automatico()
        else:
            break
        print('=' * 100)
        opcion = input("Reintentar [s/n]: ")
        if opcion.lower() != 's':
            continuar = False

    print('Saliendo del programa...')

def imprimir_menu():
    print("""\n\nGramatica libre de contexto Gpal = ({P},{0,1},A,P)
    Donde A es:
    1. P -> e
    2. P -> 0
    3. P -> 1
    4. P -> 0P0
    5. P -> 1P1
    """)
    print('\n%sMenu%s' % (separador, separador))
    print("""
        1.- Modo manual
        2.- Modo automatico
        4.- Salir
    """)
    try:
        opcion = int(input("Selecciona una opcion valida: "))
        return opcion
    except Exception as e:
        print('Error ', e)
        return 0
def entrada_automatico():
    longitud = random.randint(0, 1000)
    print("Generando palindromo con longitud = %s" % longitud)
    palindromo(longitud)

def entrada_consola():
    longitud = int(input('Introduce un numero entre 0 y 1000: '))
    if longitud>1000 or longitud<0:
        print('Algo salio mal =(')
        return 0
    print("Generando palindromo con longitud = %s" % longitud)
    palindromo(longitud)

main()
