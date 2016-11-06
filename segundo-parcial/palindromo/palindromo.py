# -*- coding: utf-8 -*-
from __future__ import print_function
import random
def palindromo(repeticiones):
    cadena = 'P'
    base_random = ''
    if repeticiones%2 == 1:
        cadena = generar_cadena(cadena, (repeticiones-1)/2)
        base_random = random.choice(['0', '1'])
    else:
        cadena = generar_cadena(cadena, repeticiones/2)
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
