from __future__ import print_function
import math
# calcular primos de n para abajo
# guardar como binarios
# contar ceros y unos
def iniciar():
    maximo = 10
    lista_primos = []
    primos_binario = []
    lista_primos = calcular_primos(maximo)
    primos_binario = conversion_binaria(lista_primos)
    print(lista_primos)
    print(primos_binario)
    contar_repeticiones(primos_binario)

def calcular_primos(maximo):
    lista_primos = []
    es_primo = False
    if maximo < 2:
        es_primo = False
    else:
        lista_primos.append(2)
        for numero_actual in range(2, maximo + 1):
            raiz = math.sqrt(numero_actual)
            if raiz == round(raiz):
                es_primo = False
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
    return lista_primos

def conversion_binaria(lista_primos):
    primos_binario = []
    for numero in lista_primos:
        primos_binario.append(bin(numero)[2:])

    return primos_binario

def contar_repeticiones(primos_binario):
    total = []
    for valor in primos_binario:
        ceros, unos = 0, 0
        for digito in valor:
            if digito == '0':
                ceros += 1
            else:
                unos += 1
        total.append({'ceros': ceros, 'unos': unos})

    print(total)

iniciar()
