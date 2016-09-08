# -*- coding: utf-8 -*-
from __future__ import print_function
import time, random

def pausar_protocolo(segundos):
    time.sleep(segundos)

def generar_cadenas(archivo):
    try:
        archivo_abierto = open(archivo, 'a')
    except Exception as e:
        print('Error al abrir archivo ', e)
    i = 0
    LONGITUD = 32
    numero_binario = ''

    for x in range(5):
        while i < LONGITUD:
            numero_binario += random.choice(['0', '1'])
            i += 1
        archivo_abierto.write(numero_binario) # Tal vez los tenga que separar
        archivo_abierto.write(' ')
        i = 0
        numero_binario = ''

    archivo_abierto.close()

def verificar_cadenas(archivo, palabras):
    try:
        archivo_abierto = open(archivo, 'r')
    except Exception as e:
        print('Error al abrir archivo ', e)

    texto = archivo_abierto.read()
    estado = 0
    palabra_aux = ''
    for simbolo in texto:
        print('-> delta(%s,%s)' % (estado, simbolo), end="\t")

        if simbolo == ' ':
            if estado == 0:
                palabras.append(palabra_aux)
                palabra_aux = ''
        else:
            palabra_aux += simbolo
            estado = automata(estado, simbolo)

# 00 11
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
        print('Simbolo extraño ', simbolo)
        return -1
    return estado

def estado_cero(simbolo):
    if simbolo == '0':
        return 2
    elif simbolo == '1':
        return 1
    else:
        return -1

def estado_uno(simbolo):
    if simbolo == '0':
        return 3
    elif simbolo == '1':
        return 0
    else:
        return -1

def estado_dos(simbolo):
    if simbolo == '0':
        return 0
    elif simbolo == '1':
        return 3
    else:
        return -1

def estado_tres(simbolo):
    if simbolo == '0':
        return 1
    elif simbolo == '1':
        return 2
    else:
        return -1
