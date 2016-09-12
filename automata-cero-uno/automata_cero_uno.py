#automata_cero_uno.py
# -*- coding: utf-8 -*-
from __future__ import print_function

def automata(text):
    array_tabla = []
    array = ['0']
    i = 0
    array_tabla.append(['0'])
    temporal_cero = []
    temporal_otro = []
    temporal = []
    for simbolo in text:
        array = array_tabla[i]
        for estado_evaluacion in array:
            if simbolo == '0' and estado_evaluacion == '0':
                temporal_cero = evaluar_estados(estado_evaluacion, simbolo)
            else:
                temporal_otro.append(evaluar_estados(estado_evaluacion, simbolo))

        if(len(temporal_cero) != 0):
            temporal.append(temporal_cero[0])
            temporal += temporal_otro[:]
            temporal.append(temporal_cero[1])
        else:
            temporal += temporal_cero[:]
            temporal += temporal_otro[:]
        array_tabla.append(temporal[:])
        temporal_cero = []
        temporal_otro = []
        temporal = []
        i += 1

    rellenar_tabla(array_tabla, text)
    letra = 0
    text +=' '
    print('')
    for linea in array_tabla:
        print(text[letra], end=' | ')
        for valor in linea:
            if(valor == '-1'):
                print("x", end=' ')
            else:
                print("q%s" %valor, end=' ')
        print()
        letra +=1

    if array_tabla[len(text)-1][len(array_tabla[len(text)-1])-1] == '2':
        print('El numero: %s es una cadena valida' % text)
    else:
        print('El numero: %s NO es una cadena valida' % text)

def rellenar_tabla(array_tabla, text):
    longitud = len(text)
    ultima_fila = len(array_tabla[longitud])
    ceros = False
    if array_tabla[longitud][ultima_fila-1] == '2':
        ceros = True
    for fila in array_tabla:
        while True:
            if len(fila) >= ultima_fila:
                break
            if (len(fila)+1 >= ultima_fila) and ceros:
                fila.append('0')
            else:
                fila.append('-1')

def evaluar_estados(estado, simbolo):
    if estado == '0':
        estado = estado_cero(simbolo)
    elif estado == '1':
        estado = estado_uno(simbolo)
    elif estado == '2':
        estado = estado_dos(simbolo)

    return estado

def estado_cero(simbolo):
    if simbolo == '1':
        return '0'
    elif simbolo == '0':
        return ['0', '1']

def estado_uno(simbolo):
    if simbolo == '1':
        return '2'
    else:
        return '-1'

def estado_dos(simbolo):
    return '-1'
