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
            print('simbolo %s, estado %s' % (simbolo, estado_evaluacion))
            if simbolo == '0' and estado_evaluacion == '0':
                temporal_cero = evaluar_estados(estado_evaluacion, simbolo)
                print('temporal_cero', temporal_cero)
            else:
                temporal_otro.append(evaluar_estados(estado_evaluacion, simbolo))
                print('temporal_otro', temporal_otro)


        temporal += temporal_cero[:]
        temporal += temporal_otro[:]
        print('otro ', temporal_otro)
        print('cero', temporal_cero)
        array_tabla.append(temporal[:])
        print('tabla: ', array_tabla)
        temporal_cero = []
        temporal_otro = []
        temporal = []
        i += 1

    print(array_tabla)

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
