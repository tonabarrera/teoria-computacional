def automa(entrada):
    estado = 0
    for digito in entrada:
        if estado == 0:
            estado = estado_cero(digito)
        elif estado == 1:
            estado = estado_uno(digito)
        elif estado == 2:
            estado = estado_dos(digito)
        elif estado == 3
            estado = estado_tres(digito)
        else:
            print('Hay que ver que procede')


def estado_cero(digito):
    if digito == 0:
        return 2
    elif digito == 1:
        return 1
    else:
        return -1

def estado_uno(digito):
    if digito == 0:
        return 3
    elif digito == 1:
        return 0
    else:
        return -1

def estado_dos(digito):
    if digito == 0:
        return 0
    elif digito == 1:
        return 3
    else:
        return -1

def estado_tres(digito):
    if digito == 0:
        return 1
    elif digito == 1:
        return 2
    else:
        return -1
