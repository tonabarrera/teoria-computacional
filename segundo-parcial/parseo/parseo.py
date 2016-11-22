# -*- coding: utf-8 -*-
from __future__ import print_function

def proceso(cadena):
    derivacion = 'B'
    for simbolo in cadena:
        for paso in derivacion:
            if paso == 'B':
                if simbolo == '(':
                    paso.replace('B', '(RB', 1)
                    break
            if paso == 'R':
                if simbolo == ')':
                    paso.replace('R', ')', 1)
