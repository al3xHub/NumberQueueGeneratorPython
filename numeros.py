numero_farmacia = 0
numero_perfumeria = 0
numero_cosmetica = 0


def asignar_numero(seleccion):
    global numero_farmacia, numero_perfumeria, numero_cosmetica
    if seleccion == 1:
        numero_farmacia += 1
        yield f'Su turno es: F-{numero_farmacia}'
    elif seleccion == 2:
        numero_perfumeria += 1
        yield f'Su turno es: P-{numero_perfumeria}'
    elif seleccion == 3:
        numero_cosmetica += 1
        yield f'Su turno es: C-{numero_cosmetica}'



