# -*- coding: utf-8 -*-
from __future__ import print_function

class Pila(object):
    def __init__(self):
        self.altura = -1
        self.elementos = []
        self.estado = 'q0'

    def vacio(self):
        if self.altura == -1:
            return True
        else:
            return False

    def sacar(self):
        if self.vacio():
            print("Vacio")
        else:
            valor = self.elementos[self.altura]
            self.altura -= 1
            return valor

    def meter(self, elemento):
        self.altura += 1
        self.elementos[self.altura:] = [elemento]

def automata(cadena):
    pila = Pila()
    pila.meter('Zo')
    estado = 'q'
    for simbolo in cadena:
        if estado == 'q':
            if simbolo == '0':
                pila.meter('X')
            elif simbolo == '1':
                pila.sacar()
                estado = 'p'
        elif estado == 'p':
            if simbolo == '1':
                pila.sacar()
            elif simbolo == '0':
                pila.meter('X')
                break

    if estado == 'p':
        if pila.sacar() == 'Zo':
            estado = 'f'

    if estado == 'f':
        print("Valido")
    else:
        print("No valido")
