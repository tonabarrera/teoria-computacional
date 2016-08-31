# -*- coding: utf-8 -*-
from __future__ import print_function

def automata(texto):
    palabra_aux = ''
    estado = 0
    palabras_ere = []
    for caracter in texto:
        caracter_aux = caracter.lower()

        if estado == 0:
            estado = estado_cero(caracter)
        elif estado == 1:
            estado = estado_uno(caracter)
        elif estado == 2:
            estado = estado_dos(caracter)
        elif estado == 3:
            estado = estado_tres(caracter)
        else:
            print('Hay que ver que procede', caracter)

        if (ord(caracter_aux) < 123 and ord(caracter_aux) > 96):
            palabra_aux += caracter
            if estado == 4:
                estado = 0
        else:
            if estado == 4:
                palabras_ere.append(palabra_aux)
                estado = 0
            palabra_aux = ''


    return palabras_ere

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
