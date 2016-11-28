# -*- coding: utf-8 -*-
from __future__ import print_function

def proceso(cadena):
    derivacion = 'B'
    cadena += ' '
    print('Cadena: ', cadena)
    continuar = True
    for simbolo in cadena:
        if not continuar:
            break
        print(derivacion)
        for paso in derivacion:
            #print('Pre %s paso: %s simbolo %s' %(derivacion, paso, simbolo))
            if paso == 'B':
                if simbolo == '(':
                    derivacion = derivacion.replace('B', '(RB', 1)
                    break
                elif simbolo == ' ':
                    derivacion = derivacion.replace('B', '', 1)
                    break
                else:
                    continuar = False
                    break
            elif paso == 'R':
                if simbolo == ')':
                    derivacion = derivacion.replace('R', ')', 1)
                    break
                elif simbolo == '(':
                    derivacion = derivacion.replace('R', '(RR', 1)
                    break
                else:
                    continuar = False
                    break
    print('Final: ', derivacion)
