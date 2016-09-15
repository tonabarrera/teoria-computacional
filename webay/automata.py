# -*- coding: utf-8 -*-
from __future__ import print_function

def automata(cadenas):
    estado = 'B'
    for simbolo in cadenas:
        if simbolo ==  '\n':
            simbolo = '\\n'
        print('-> delta(%s,%s)' % (estado, simbolo), end="\t")
        simbolo_aux = simbolo.lower()
        estado = estados(estado, simbolo_aux)
        if estado == 'E' or estado == 'I':
            print('Contine web o ebay')

def estados(estado, simbolo):
    if estado == 'B':
        estado = estado_B(simbolo)
    elif estado == 'C':
        estado = estado_C(simbolo)
    elif estado == 'D':
        estado = estado_D(simbolo)
    elif estado == 'E':
        estado = estado_E(simbolo)
    elif estado == 'F':
        estado = estado_F(simbolo)
    elif estado == 'G':
        estado = estado_G(simbolo)
    elif estado == 'H':
        estado = estado_H(simbolo)
    elif estado == 'I':
        estado = estado_I(simbolo)
    else:
        estado = 'A'

    return estado

def estado_B(simbolo):
    if simbolo == 'w':
        return 'C'
    elif simbolo == 'e':
        return 'F'
    return 'B'

def estado_C(simbolo):
    if simbolo == 'w':
        return 'C'
    elif simbolo == 'e':
        return 'D'
    return 'B'

def estado_D(simbolo):
    if simbolo == 'b':
        return 'E'
    elif simbolo == 'e':
        return 'F'
    return 'B'

def estado_E(simbolo):
    if simbolo == 'a':
        return 'H'
    elif simbolo == 'e':
        return 'F'
    elif simbolo == 'w':
        return 'C'
    return 'B'

def estado_F(simbolo):
    if simbolo == 'b':
        return 'G'
    elif simbolo == 'e':
        return 'F'
    elif simbolo == 'w':
        return 'C'
    return 'B'

def estado_G(simbolo):
    if simbolo == 'a':
        return 'H'
    elif simbolo == 'e':
        return 'F'
    elif simbolo == 'w':
        return 'C'
    return 'B'

def estado_H(simbolo):
    if simbolo == 'y':
        return 'I'
    elif simbolo == 'e':
        return 'F'
    elif simbolo == 'w':
        return 'C'
    return 'B'

def estado_I(simbolo):
    if simbolo == 'e':
        return 'F'
    elif simbolo == 'w':
        return 'C'
    return 'B'
