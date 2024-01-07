"""
Simula la entrada a una farmacia. Pregunta que trámites desea hacer y asigna nº de turno segun trámite
(perfumeria, farmacia, cosmetica). Ej: para cosmetica: C-54

El programa debe mantener el orden del turno que se ha solicitado recordando cuál fue el último nº y
asignando el siguiente (utilizar generadores).

Mostrar texto con turno --> 'Su turno es ..." Utilizar decoradores para añadir ese texto adicional una sola vez.

Separar código por módulos:
    - numeros.py para añadir los generadores y decoradores
    - principal.py escribir las funciones para correr el programa.

Recordar importar los módulos.
"""
from numeros import *


def inicio():
    print('Bienvenido a tu farmacia de confianza, elige que servicio deseas realizar para ponerse en la cola')

    while True:
        seleccion = input('1- Farmacia, 2- Perfumeria, 3- Cosmetica, 4- Finalizar\n')
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if seleccion == 4:
                print("Gracías por su visita")
                break
            elif seleccion in range(1, 4):
                numero_asignado = asignar_numero(seleccion)
                print(next(numero_asignado))
            else:
                print('Porfavor, ingresa un número válido')


inicio()
