# -*- coding: utf-8 -*-
from __future__ import print_function
# >>> import pdb
# >>> a="a string"
# >>> pdb.set_trace()
# --Return--
# > <stdin>(1)<module>()->None
# (Pdb) p a
# 'a string'
# (Pdb) To continue execution use c (or cont or continue).
def iniciar():
    continuar = True
    while continuar:
        opcion = imprimir_menu()
        if opcion == 1:
            texto = input("Escribe un numero binario: ")
            entrada_consola(texto)
        elif opcion == 2:
            ejecutar_random()
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
        2.- Random
        3.- Ver diagrama de estados
    """)
    opcion = int(input("Selecciona una opcion: "))

    return opcion
