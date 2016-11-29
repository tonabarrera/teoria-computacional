# -*- coding: utf-8 -*-
from __future__ import print_function

def maquina(cadena):
pass

def funcion_transicion(estado, simbolo):
    if estado == 0:
        return estado_cero(simbolo)
    elif estado == 1:
        return estado_uno(simbolo)
    elif estado == 2:
        return estado_dos(simbolo)
    elif estado == 3:
        return estado_tres(simbolo)
    elif estado == 4:
        return estado_cuatro(simbolo)

def estado_cero(simbolo):
    if simbolo == '0':
        return [1, 'X', 'R']
    elif simbolo == 'Y':
        return [3, 'Y', 'R']

def estado_uno(simbolo):
    if simbolo == '0':
        return [1, '0', 'R']
    elif simbolo == '1':
        return [2, 'Y', 'L']
    elif simbolo == 'Y':
        return [1, 'Y', 'R']

def estado_dos(simbolo):
    if simbolo == '0':
        return [2, '0', 'L']
    elif simbolo == 'X':
        return [0, 'X', 'R']
    elif simbolo == 'Y':
        return [2, 'Y', 'L']

def estado_tres(simbolo):
    if simbolo == 'Y':
        return [3, 'Y', 'R']
    elif simbolo == 'B':
        return [4, 'B', 'R']

def estado_cuatro(simbolo):
    pass
