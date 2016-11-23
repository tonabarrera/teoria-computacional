# -*- coding: utf-8 -*-
from __future__ import print_function
from pila import Automata
def ver_diagrama():
    print('Mostrando animación. Cierre la ventana para continuar')
    try:
        animado = Automata()
        animado.master.title('Autómata de pila')
        animado.animar('0011')
        animado.mainloop()
    except Exception as e:
        print("Error", e)

ver_diagrama()
