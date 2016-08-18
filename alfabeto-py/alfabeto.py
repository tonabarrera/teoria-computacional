import random

def iniciar():
    maximo = random.randint(1, 1000)
    maximo = 20
    continuar = True
    while continuar:
        generar_palabras(maximo)
        continuar = False

def generar_palabras(maximo):
    continuar = True
    m = 0
    archivo = open('palabras.txt', 'w')
    archivo.write('S = {e')

    for longitud_palabra in range(1, maximo+1):
        palabra_temporal = [0] * longitud_palabra
        while continuar:
            archivo.write(',')
            for j in range(longitud_palabra):
                archivo.write(palabra_temporal[j])
            m = 0
            while (m < longitud_palabra):
                palabra_temporal[m] = palabra_temporal[m] + 1
                if (palabra_temporal[m] > 1):
                    palabra_temporal[m] = 0
                else:
                    break
                m = m + 1
            if(m >= longitud_palabra):
                palabra_temporal = []
                break
        print('Va en: ', longitud_palabra)

    archivo.write('}')
    archivo.close()

iniciar()
