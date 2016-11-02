# -*- coding: utf-8 -*-
from __future__ import print_function
from diagrama import Diagrama

def main():
    ver_diagrama()

def ver_diagrama():
    print('Mostrando diagrama del autómata. Cierre la ventana para continuar')
    try:
        diagrama = Diagrama()
        diagrama.master.title('Diagrama del autómata webay')
        diagrama.mainloop()
    except Exception as e:
        print("Error", e)

main()
