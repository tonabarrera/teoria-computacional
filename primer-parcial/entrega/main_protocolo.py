#main_protocolo.py
# -*- coding: utf-8 -*-
from __future__ import print_function
from diagrama_protocolo import Diagrama
from protocolo import generar_cadenas, pausar_protocolo, verificar_cadenas
import random

separador = '*'*50

def iniciar():
    continuar = True
    while continuar:
        opcion = imprimir_menu()
        if opcion == 1:
            correr_protocolo()
        elif opcion == 2:
            ver_diagrama()
        else:
            break # Sal del programa
        print('*' * 100)
        opcion = input("Reintentar s/n: ")
        if opcion.lower() != 's':
            continuar = False

    print('\nSaliendo del programa...')

def imprimir_menu():
    print('\n\n%sMenu%s' % (separador, separador))
    print("""
        1.- Correr protocolo
        2.- Ver diagrama
        3.- Salir
    """)
    try:
        opcion = int(input("Selecciona una opcion valida: "))
        return opcion
    except Exception as e:
        print('Error ', e)
        return 0

def correr_protocolo():
    condicion = True
    ARCHIVO_PALABRAS = 'palabras.txt'
    ARCHIVO_PALABRAS_VALIDAS = 'validas.txt'
    TIEMPO_PAUSA = 2
    palabras = []
    while condicion:
        archivo = open('validas.txt', 'w')
        print('\nGenerando cadenas...')
        generar_cadenas(ARCHIVO_PALABRAS)
        print('\nEnviando las candenas...')
        pausar_protocolo(TIEMPO_PAUSA)
        print('\nVerificando las cadenas las candenas...')
        verificar_cadenas(ARCHIVO_PALABRAS, palabras)
        print('\nRegresando las candenas...')
        print('\nPalabras validas: ', palabras)
        for palabra in palabras:
            archivo.write(palabra)
            archivo.write(' ')
        palabras = []
        condicion = random.choice([True, False])
        archivo.close()

def ver_diagrama():
    print('Mostrando diagrama del automata. Cierre la ventana para continuar')
    try:
        diagrama_ere = Diagrama()
        diagrama_ere.master.title('Diagrama del protocolo')
        diagrama_ere.mainloop()
    except Exception as e:
        print("Error", e)

iniciar()
