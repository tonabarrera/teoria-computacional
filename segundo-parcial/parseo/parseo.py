# -*- coding: utf-8 -*-
from __future__ import print_function

def proceso(cadena):
    derivacion = 'B'
    cadena += ' '
    for simbolo in cadena:
        print('What: ', simbolo)
        for paso in derivacion:
            if paso == 'B':
                if simbolo == '(':
                    derivacion = derivacion.replace('B', '(RB', 1)
                    break
                elif simbolo == ' ':
                    derivacion = derivacion.replace('B', '', 1)
                    break
                else:
                    break
            elif paso == 'R':
                if simbolo == ')':
                    derivacion = derivacion.replace('R', ')', 1)
                    break
                elif simbolo == '(':
                    derivacion = derivacion.replace('R', '(RR', 1)
                    break
                else:
                    break
            print('Pre: %s simbolo %s' % (derivacion, simbolo))
        print('Derivacion: ', derivacion)
    print('Final: ', derivacion)
