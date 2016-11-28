# -*- coding: utf-8 -*-
from __future__ import print_function
import time

class Pila(object):
    def __init__(self):
        self.altura = -1
        self.elementos = []

    def vacio(self):
        if self.altura == -1:
            return True
        else:
            return False

    def sacar(self):
        if self.vacio():
            return 'e'
        else:
            valor = self.elementos[self.altura]
            self.altura -= 1
            return valor

    def meter(self, elemento):
        self.altura += 1
        self.elementos[self.altura:] = [elemento]

    def mostar(self):
        i = self.altura
        cadena = ''
        while(i>-1):
            cadena += self.elementos[i]
            i -= 1
        return cadena

def automata(cadena):
    pila = Pila()
    pila.meter('Zo')
    estado = 'q'
    cadena_aux = cadena
    cadena = cadena + ' '
    for simbolo in cadena:
        time.sleep(1)
        if cadena_aux == '':
            cadena_aux = 'e'
        #print('(%s, %s, %s)' %(estado, cadena_aux, pila.mostar()), end='+')
        pintar(estado, cadena_aux, pila)
        if estado == 'q':
            if simbolo == '0':
                pila.meter('X')
            elif simbolo == '1':
                if pila.sacar() == 'Zo':
                    break
                estado = 'p'
            else:
                estado = 'f'
                break
        elif estado == 'p':
            if simbolo == '1':
                if pila.sacar() == 'Zo':
                    estado = 'f'
                    break
            elif simbolo == '0':
                pila.meter('X')
                break
            elif simbolo == ' ':
                estado = 'f'
                if pila.mostar() == 'Zo':
                    break
        cadena_aux = cadena_aux[1:]

    time.sleep(1)
    if cadena_aux == '':
        cadena_aux = 'e'
    pintar(estado, cadena_aux, pila)

def pintar(estado, cadena_aux, stack):
    pila = 'Zo'
    if stack.mostar() != '':
        pila = stack.mostar()

    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('     %s' %cadena_aux)
    print('     ^')
    print('     |')
    print('     |')
    print('     |')
    print('-----------')
    print('|         |')
    print('|    %s    |' %estado)
    print('|         |')
    print('-----------')
    print('     |')
    print('     |')
    print('     |')
    print('     v')
    print('     %s' %pila)
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
