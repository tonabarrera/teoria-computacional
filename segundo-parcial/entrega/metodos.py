# -*- coding: utf-8 -*-
from __future__ import print_function

def maquina(cadena):
    continuar = True
    archivo = open('turing-historia.txt', 'w')
    i = 0
    estado = 0
    cadena_aux = list(cadena)
    cadena_final = ''
    archivo.write('La cadena es: %s \n' %cadena)
    while continuar:
        try:
            simbolo = cadena_aux[i]
        except Exception as e:
            cadena_aux.append('B')
            simbolo = cadena_aux[i]
        cadena_final = imprimir_secuencia(estado, cadena_aux, i)
        print(cadena_final, end = '')
        archivo.write(cadena_final)
        resultado = funcion_transicion(estado, simbolo)
        if len(resultado) == 0:
            break
        estado = resultado[0]
        cadena_aux[i] = resultado[1]
        if resultado[2] == 'R':
            i += 1
        elif resultado[2] == 'L':
            i -= 1
        print(' |- ', end='')
        archivo.write(' |- ')
    print('\n')
    if estado == 4:
        print('Cadena valida')
        archivo.write('\n\nCadena valida')
    else:
        print('Cadena invalida')
        archivo.write('\nCadena invalida')
    archivo.close()

def imprimir_secuencia(estado, cadena, indice):
    cadena_aux = ''
    i = 0
    while i<len(cadena):
        if i == indice:
            cadena_aux += '(q'+ str(estado) + ')'
        cadena_aux += cadena[i]
        i +=1
    return cadena_aux

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
    return []

def estado_uno(simbolo):
    if simbolo == '0':
        return [1, '0', 'R']
    elif simbolo == '1':
        return [2, 'Y', 'L']
    elif simbolo == 'Y':
        return [1, 'Y', 'R']
    return []

def estado_dos(simbolo):
    if simbolo == '0':
        return [2, '0', 'L']
    elif simbolo == 'X':
        return [0, 'X', 'R']
    elif simbolo == 'Y':
        return [2, 'Y', 'L']
    return []

def estado_tres(simbolo):
    if simbolo == 'Y':
        return [3, 'Y', 'R']
    elif simbolo == 'B':
        return [4, 'B', 'R']
    return []

def estado_cuatro(simbolo):
    return []
