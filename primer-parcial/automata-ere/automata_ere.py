#automata_ere.py
# -*- coding: utf-8 -*-
from __future__ import print_function

def verificar_palabras(texto, palabras_ere, posiciones = []):
    palabra_aux = ''
    estado = 0
    num_palabra = 1
    for simbolo in texto:
        simbolo_aux = simbolo.lower()
        if simbolo ==  '\n':
            simbolo = '\\n'
        print('-> delta(q%s,%s)' % (estado, simbolo), end="\t")

        estado = automata(estado, simbolo_aux)

        if (ord(simbolo_aux) < 123 and ord(simbolo_aux) > 96):
            palabra_aux += simbolo
            if estado == 4:
                estado = 0
        else:
            if estado == 4:
                palabras_ere.append(palabra_aux)
                posiciones.append(num_palabra)
                estado = 0
            palabra_aux = ''
            if simbolo == ' ':
                num_palabra += 1

def automata(estado, simbolo):
    if estado == 0:
        estado = estado_cero(simbolo)
    elif estado == 1:
        estado = estado_uno(simbolo)
    elif estado == 2:
        estado = estado_dos(simbolo)
    elif estado == 3:
        estado = estado_tres(simbolo)
    else:
        print('Simbolo extraño: ', simbolo)

    return estado

def estado_cero(simbolo):
    if simbolo == 'e':
        return 1
    else:
        return 0

def estado_uno(simbolo):
    if simbolo == 'r':
        return 2
    elif simbolo == 'e':
        return 1
    else:
        return 0

def estado_dos(simbolo):
    if simbolo == 'e':
        return 3
    else:
        return 0

def estado_tres(simbolo):
    if simbolo == 'r':
        return 2
    elif simbolo == 'e':
        return 1
    else:
        return 4
