from shutil import register_unpack_format
import sys
import matplotlib.pyplot as plt
from random import sample, choice, shuffle
import numpy as np

def tableGenerator(number_reserves):
    wing_types = map(lambda x: x + '-Reserva', ['JUAN', 'PEPE', 'MARIA', 'LAIA', 'MONTSE', 'PAULA'])
    L = list(wing_types)
    free_pos = sample(range(number_reserves), number_reserves >> 1)
    position = 0

    global solution
    solution = min(free_pos)

    while position <= number_reserves:
        if position not in free_pos:
            yield choice(L), str(position)
        position += 1

def reserveList (number_reserves):

    reserve_list = [i for i in tableGenerator(number_reserves * 2)]

    reserve_list = reserve_list[:number_reserves]

    shuffle(reserve_list)

    return reserve_list, solution



def bookerineManagement_iterativo(reserves):

    #función iterativa que devuelve la posición de la reserva más cercana a la que se puede reservar

    k = 1

    reserves.sort(key=lambda x: int(x[1]))

    #Ordenamiento de la lista de menor a mayor número de mesa mediante la función
    #sort y una función lambda. Realizar casteo de String a Entero del segundo valor de cada tupla
    #de la lista (el número de mesa)

    if int(reserves[0][1]) != 0:
        return 0 

    #Si la primera reserva es distinta de 0, devolver 0

    for j in range(len(reserves)): 
        if k == len(reserves) or int(reserves[k][1]) - int(reserves[j][1]) > 1:
            return int(reserves[j][1]) + 1
        k += 1

    # Bucle que se ejecuta |reserves| veces, y devuelve la posición de la reserva más cercana a la que se puede reservar
    # Si la resta  entre la primera posción y la seguna es mayor que 1

    return int(reserves[-1][1]) + 1

    #Devuelve la última posición de la lista de reservas + 1 en caso de que no se cumpla la condición dentro del bucle



def bookerineManagement_recursivo(reserves): 
    
    #función recursiva que devuelve la posición de la reserva más cercana a la que se puede reservar
    
    reserves.sort(key=lambda x: int(x[1]))
    
    #Ordenamiento de la lista de menor a mayor número de mesa mediante la función
    #sort y una función lambda. Realizar casteo de String a Entero del segundo valor de cada tupla
    #de la lista (el número de mesa)
    
    return bookerineManagement_recursivo_cola(reserves, 0) 


def bookerineManagement_recursivo_cola(reserves, res):

    #función recursiva

    if not reserves:
        return res

    #Si la lista de reservas está vacía, devolver la posición de la reserva más cercana a la que se puede reservar
        
    if int(reserves[0][1]) > res:
        return res

    #Si la primera reserva es mayor que la posición de la reserva más cercana a la que se puede reservar,

    return bookerineManagement_recursivo_cola(reserves[1:], int(reserves[0][1]) + 1)

    #devolver la lista exepto el primer elemento y la posición de la reserva más cercana a la que se puede reservar

def calcular_temps_iterativo():
    import timeit
    temps = []
    for x in range(1,200,10):
        out_reserves = reserveList(x)
        reserves = out_reserves[0]
        temps.append( (x, timeit.timeit("bookerineManagement_iterativo("+str(reserves)+")",
            setup="from __main__ import bookerineManagement_iterativo")) )
    return temps

def calcular_temps_recursivo():
    import timeit
    temps = []
    for x in range(1,200,10):
        out_reserves = reserveList(x)
        reserves = out_reserves[0]
        temps.append( (x, timeit.timeit("bookerineManagement_recursivo("+str(reserves)+")",
            setup="from __main__ import bookerineManagement_recursivo")) )
    return temps


def crear_grafica( x_list, y_list ):
    plt.scatter(x_list, y_list)
    plt.show()


def costEmpiricalComputation ():

    temps_iterativo = calcular_temps_iterativo()
    crear_grafica(*map(list, zip(*temps_iterativo)))

    temps_recursivo = calcular_temps_recursivo()
    crear_grafica(*map(list, zip(*temps_recursivo)))

    return 0


# Programa Principal para la generación de mesas y reservas dentro de un restaurante. Para ello, al programa deberemos
# de pasarle como argumentos el tamaño del restaurante en número de mesas.
if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Usage: ' + sys.argv[0] + ' <list_size>')

    out_reserves = reserveList(int (sys.argv[1]))
    reserves = out_reserves [0]
    idTable = bookerineManagement_iterativo(reserves)
    #idTable = bookerineManagement_recursivo(reserves)
    costEmpiricalComputation()

    if idTable == solution:
        print ('Solucion Correcta')
    else:
        print ('Solucion Incorrecta')
