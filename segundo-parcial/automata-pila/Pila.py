# -*- coding: utf-8 -*-
from __future__ import print_function
from animacion import Animacion
import time
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

    def mostar(self):
        i = self.altura
        while(i>-1):
            print(self.elementos[i], end = ' ')
            i -= 1
        print('')

class Automata(Animacion):
    def animar(self, cadena):
        super(Automata, self).animar()
        pila = Pila()
        pila.meter('Zo')
        estado = 'q'
        cadena_aux = cadena
        print(cadena)
        for simbolo in cadena:
            time.sleep(0.1)
            cadena_aux = cadena_aux[1:]
            pila.mostar()
            print(cadena_aux)
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
        pila.mostar()
        if estado == 'p':
            if pila.sacar() == 'Zo':
                estado = 'f'

        if estado == 'f':
            print("Valido")
        else:
            print("No valido")
