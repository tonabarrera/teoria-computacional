# -*- coding: utf-8 -*-
from __future__ import print_function
import random
def palindromo(repeticiones):
    base = ['', '0', '1']
    cadena = 'P'
    cadena = generar_cadena(cadena, repeticiones)
    base_random = random.choice(base)
    cadena = cadena.replace('P', base_random)

    print('Cadena final con base P="%s" -> %s' %(base_random, cadena))

def generar_cadena(cadena, repeticiones):
    if repeticiones > 0:
        regla = random.choice(['0', '1'])
        cadena = regla + cadena + regla
        print(cadena)
        repeticiones = repeticiones - 1
        cadena = generar_cadena(cadena, repeticiones)
    return cadena
