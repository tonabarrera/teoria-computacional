#main_paridad.py
# -*- coding: utf-8 -*-
from __future__ import print_function
from automata_paridad import ejecutar_automata
from diagrama_paridad import Diagrama
import random

separador = '*' * 50
def iniciar():
    continuar = True
    while continuar:
        opcion = imprimir_menu()
        if opcion == 1:
            ejecutar_manual()
        elif opcion == 2:
            ejecutar_random()
        elif opcion == 3:
            ver_diagrama()
        else:
            break
        print('\n', separador)
        opcion = input("Reintentar s/n: ")
        if opcion.lower() != 's':
            continuar = False

    print('Saliendo del programa...')

def imprimir_menu():
    print('\n\n%sMenu%s' % (separador, separador))
    print("""
        1.- Entrada en consola (Manual)
        2.- Numero aleatorio (automatico)
        3.- Ver diagrama de transiciones
        4.- Salir
    """)
    try:
        opcion = int(input("Selecciona una opcion valida: "))
        return opcion
    except Exception as e:
        print('Error ', e)
        return 0

def ejecutar_random():
    i = 0
    longitud_random = random.randint(1, 1000)
    numero_binario = ''
    while i < longitud_random:
        numero_binario += random.choice(['0', '1'])
        i += 1

    print("El numero aleatorio es: ", numero_binario)
    provar_paridad(numero_binario)

def ejecutar_manual():
    numero_binario = input("Escribe un numero binario: ")
    provar_paridad(numero_binario)

def provar_paridad(numero_binario):
    resultado = ejecutar_automata(numero_binario)
    print('\n')
    if resultado:
        print('El numero %s, es valido' % numero_binario)
    else:
        print('El numero: %s, no es valido' % numero_binario)

def ver_diagrama():
    print('Mostrando diagrama del automata. Cierre la ventana para continuar')
    try:
        diagrama_paridad = Diagrama()
        diagrama_paridad.master.title('Diagrama del automata paridad')
        diagrama_paridad.mainloop()
    except Exception as e:
        print("Error", e)

iniciar()
