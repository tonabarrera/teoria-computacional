# -*- coding: utf-8 -*-
from __future__ import print_function
from palindromo import palindromo
import random
def main():
    repeticiones = random.randint(1, 10)
    print("""Gramatica libre de contexto Gpal = ({P},{0,1},A,P)
    Donde A es:
    1. P -> e
    2. P -> 0
    3. P -> 1
    4. P -> 0P0
    5. P -> 1P1
    """)
    print("Generando palindromo con %s repeticiones" % repeticiones)
    palindromo(repeticiones)

main()
