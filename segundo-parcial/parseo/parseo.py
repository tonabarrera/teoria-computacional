# -*- coding: utf-8 -*-
from __future__ import print_function

def proceso(cadena):
    derivacion = 'B'
    archivo = open('historia-parentesis.txt', 'w')
    cadena += ' '
    print('Cadena: ', cadena)
    archivo.write('Cadena: %s'%cadena)
    continuar = True
    for simbolo in cadena:
        if not continuar:
            break
        print(derivacion, end = '\t')
        archivo.write('\n%s   ' %derivacion)
        for paso in derivacion:
            if paso == 'B':
                if simbolo == '(':
                    derivacion = derivacion.replace('B', '(RB', 1)
                    print('Regla usada: B->(RB')
                    archivo.write('Regla usada: B->(RB')
                    break
                elif simbolo == ' ':
                    derivacion = derivacion.replace('B', '', 1)
                    print('Regla usada: B->e')
                    archivo.write('Regla usada: B->e')
                    break
                elif simbolo == ')':
                    continuar = False
                    break
            elif paso == 'R':
                if simbolo == ')':
                    derivacion = derivacion.replace('R', ')', 1)
                    print('Regla usada: R->)')
                    archivo.write('Regla usada: R->)')
                    break
                elif simbolo == '(':
                    derivacion = derivacion.replace('R', '(RR', 1)
                    print('Regla usada: R->(RR')
                    archivo.write('Regla usada: R->(RR')
                    break
                elif simbolo == ' ':
                    continuar = False
                    break
    archivo.write('\nFinal: %s' %derivacion)
    print('\nFinal: ', derivacion)
    if paso == 'B' and simbolo == ' ':
        print('\nCadena balanceada')
        archivo.write('\nCadena balanceada')
    else:
        print('\nCandena no balanceada')
        archivo.write('\nCadena no balanceada')
    archivo.close()
