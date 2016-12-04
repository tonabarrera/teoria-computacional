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

    def mostrar(self):
        i = self.altura
        cadena = ''
        while(i>-1):
            cadena += self.elementos[i]
            i -= 1
        return cadena

def automata(cadena, ver_animacion):
    pila = Pila()
    archivo = open('historia-pila.txt', 'w')
    pila.meter('Zo')
    estado = 'q'
    cadena_aux = cadena
    cadena = cadena + ' '
    archivo.write('La cadena es: ' + cadena_aux + '\n')
    for simbolo in cadena:
        if cadena_aux == '':
            cadena_aux = 'e'
        if ver_animacion:
            time.sleep(1)
            pintar(estado, cadena_aux, pila)
        else:
            print('(%s, %s, %s)' %(estado, cadena_aux, pila.mostrar()), end='')
        archivo.write('(%s, %s, %s)' %(estado, cadena_aux, pila.mostrar()))
        if estado == 'q':
            if simbolo == '0':
                pila.meter('X')
            elif simbolo == '1':
                if pila.sacar() == 'Zo':
                    pila.meter('Zo')
                    break
                estado = 'p'
            else:
                estado='q'
                break
        elif estado == 'p':
            if simbolo == '1':
                if pila.sacar() == 'Zo':
                    estado = 'f'
                    pila.meter('Zo')
                    break
            elif simbolo == '0':
                pila.meter('X')
                cadena_aux = cadena_aux[1:]
                break
            elif simbolo == ' ':
                estado = 'f'
            else:
                break
        cadena_aux = cadena_aux[1:]
        print('|-', end='')
        archivo.write('|-')

    if cadena_aux == '':
        cadena_aux = 'e'
    if (pila.mostrar() == 'Zo') and cadena_aux == 'e' and estado=='f':
        if ver_animacion:
            time.sleep(1)
            pintar(estado, cadena_aux, pila)
        else:
            print('(%s, %s, %s)' %(estado, cadena_aux, pila.mostrar()))
            print('\n')
        archivo.write('(%s, %s, %s)' %(estado, cadena_aux, pila.mostrar()))
        print('\nCadena valida')
        archivo.write('\nCadena valida')
    else:
        print('\nCadena invalida')
        archivo.write('\nCadena invalida')
    archivo.close()

def pintar(estado, cadena_aux, stack):
    pila = 'Zo'
    if stack.mostrar() != '':
        pila = stack.mostrar()

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
