from __future__ import print_function
import math
# calcular primos de n para abajo
# guardar como binarios
# contar ceros y unos
def iniciar():
    maximo = 1000
    calcular_primos(maximo)

def calcular_primos(maximo):
    lista_primos = []
    es_primo = False
    if maximo < 2:
        print('No es primo')
    else:
        lista_primos.append(2)
        for numero_actual in range(2, maximo + 1):
            raiz = math.sqrt(numero_actual)
            if raiz == round(raiz):
                es_primo = False
                #print('No es primo: ', numero_actual)
            else:
                for num in lista_primos:
                    if num > math.ceil(raiz):
                        break
                    if numero_actual % num == 0:
                        es_primo = False
                        break
                    else:
                        es_primo = True
                if es_primo:
                    lista_primos.append(numero_actual)
    print(lista_primos)

iniciar()
