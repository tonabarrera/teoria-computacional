def ejecutar_automata(cadena):
    estado = 0
    #0011
    for simbolo in cadena:
        print('-> delta(q%s, %s)' % (estado, simbolo), end="\t")
        estado = automata(estado, simbolo)
        if estado == -1:
            break
    if estado == 0:
        return True
    return False

def automata(estado, simbolo):
    if estado == 0:
        estado = estado_cero(simbolo)
    elif estado == 1:
        estado = estado_uno(simbolo)
    elif estado == 2:
        estado = estado_dos(simbolo)
    elif estado == 3:
        estado = estado_tres(simbolo)
    else:
        print('Simbolo extraño ', simbolo)
        return -1
    return estado

def estado_cero(simbolo):
    if simbolo == '0':
        return 2
    elif simbolo == '1':
        return 1
    else:
        return -1

def estado_uno(simbolo):
    if simbolo == '0':
        return 3
    elif simbolo == '1':
        return 0
    else:
        return -1

def estado_dos(simbolo):
    if simbolo == '0':
        return 0
    elif simbolo == '1':
        return 3
    else:
        return -1

def estado_tres(simbolo):
    if simbolo == '0':
        return 1
    elif simbolo == '1':
        return 2
    else:
        return -1
