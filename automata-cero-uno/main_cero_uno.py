#main_cero_uno.py
# -*- coding: utf-8 -*-
from __future__ import print_function
from automata_cero_uno import automata
from diagrama_cero_uno import Diagrama
import random

separador = '*'*50

def iniciar():
    continuar = True
    while continuar:
        opcion = imprimir_menu()
        if opcion == 1:
            entrada_consola()
        elif opcion == 2:
            ejecutar_random()
        elif opcion == 3:
            ver_diagrama()
        else:
            break # Sal del programa
        print('*' * 100)
        opcion = input("Reintentar s/n: ")
        if opcion.lower() != 's':
            continuar = False

    print('Saliendo del programa...')

def imprimir_menu():
    print('\n\n%sMenu%s' % (separador, separador))
    print("""
        1.- Entrada en consola (Manual)
        2.- Aleatorio (Automatico)
        3.- Ver diagrama
        4.- Salir
    """)
    try:
        opcion = int(input("Selecciona una opcion valida: "))
        return opcion
    except Exception as e:
        print('Error ', e)
        return 0

def entrada_consola():
    texto = input("Escribe el numero binario: ")
    automata(texto)


def ejecutar_random():
    i = 0
    longitud_random = random.randint(1, 1000)
    numero_binario = ''
    while i < longitud_random:
        numero_binario += random.choice(['0', '1'])
        i += 1

    print("El numero aleatorio es: ", numero_binario)
    automata(numero_binario)

def ver_diagrama():
    print('Mostrando diagrama del automata. Cierre la ventana para continuar')
    try:
        diagrama_ere = Diagrama()
        diagrama_ere.master.title('Diagrama del automata cero-uno')
        diagrama_ere.mainloop()
    except Exception as e:
        print("Error", e)


iniciar()
