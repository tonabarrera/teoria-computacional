# -*- coding: utf-8 -*-
from __future__ import print_function

def automata(texto):
    estado = 'B'
    palabra_aux = ''
    num_palabra = 1
    cumple = False
    ebay = 0
    palabra_posicion = 0
    ebay_pos = []
    web_pos = []
    web = 0
    palabras = []
    diccionario = {}
    for simbolo in texto:
        palabra_posicion += 1
        simbolo_aux = simbolo.lower()
        if simbolo ==  '\n':
            simbolo = '\\n'
        print('-> delta(%s,%s)' % (estado, simbolo), end="\t")
        estado = estados(estado, simbolo_aux)
        if estado == 'G' or estado == 'I':
            cumple = True
        if estado == 'G':
            web += 1
            web_pos.append([palabra_posicion-2, palabra_posicion])
        elif estado == 'I':
            ebay += 1
            ebay_pos.append([palabra_posicion-3, palabra_posicion])

        if (ord(simbolo_aux) < 123 and ord(simbolo_aux) > 96):
            palabra_aux += simbolo
        else:
            if cumple:
                palabras.append(palabra_aux)
                cumple = False
            palabra_aux = ''
    diccionario = {'num_web': web, 'num_ebay':ebay, 'web_pos':web_pos, 'ebay_pos':ebay_pos, 'palabras':palabras}
    return diccionario

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
        return 'D'
    return 'B'

def estado_C(simbolo):
    if simbolo == 'w':
        return 'C'
    elif simbolo == 'e':
        return 'E'
    return 'B'

def estado_D(simbolo):
    if simbolo == 'b':
        return 'F'
    elif simbolo == 'e':
        return 'D'
    elif simbolo == 'w':
        return 'C'
    return 'B'

def estado_E(simbolo):
    if simbolo == 'b':
        return 'G'
    elif simbolo == 'e':
        return 'D'
    elif simbolo == 'w':
        return 'C'
    return 'B'

def estado_F(simbolo):
    if simbolo == 'a':
        return 'H'
    elif simbolo == 'e':
        return 'D'
    elif simbolo == 'w':
        return 'C'
    return 'B'

def estado_G(simbolo):
    if simbolo == 'a':
        return 'H'
    elif simbolo == 'e':
        return 'D'
    elif simbolo == 'w':
        return 'C'
    return 'B'

def estado_H(simbolo):
    if simbolo == 'y':
        return 'I'
    elif simbolo == 'e':
        return 'D'
    elif simbolo == 'w':
        return 'C'
    return 'B'

def estado_I(simbolo):
    if simbolo == 'e':
        return 'D'
    elif simbolo == 'w':
        return 'C'
    return 'B'
