import numpy as np
import random
import math


def getFactoresPrimos(num):
    primos = []
    x = 2
    while(num != 1):
        if(num % x == 0):
            #print("{} ".format(x))
            num = num / x
            primos.append(x)
        else:
            x = x + 1
    return primos


def obtener_primos(modulo):
    getfactoresprimos = getFactoresPrimos(modulo)
    bases = list(set(getfactoresprimos))
    exponente = []
    cadena_primos = ""
    for x in bases:
        exponente.append(getfactoresprimos.count(x))
        cadena_primos += "{}^{} ".format(x, getfactoresprimos.count(x))
    # print(cadena_primos)
    return (bases, exponente, cadena_primos)


# Minimo comun multiplo(MCM)
def mcm(longitud, bases):
    num = []
    mayor = 0
    casilla = 0

    for i in range(longitud):
        num.append(bases[i])
        if num[i] > mayor:
            mayor = num[i]

    interruptor = 0
    multiplicador = 0
    multiplo = 0

    while interruptor == 0:
        contador = 0
        multiplicador = multiplicador + 1
        multiplo = mayor * multiplicador
        for i in range(longitud):
            if multiplo % num[i] == 0:
                contador = contador + 1

        if contador == longitud:
            interruptor = 1
    #print("El M.C.M es: %d" % (multiplo))
    return multiplo


def GenValuesMultiply(modulo, bases):
    basesForFunction = []
    basesForFunction = bases
    if(modulo%4 == 0):
        basesForFunction.append(4)
        mcmForFunction = mcm(len(basesForFunction), basesForFunction)
    else:
        basesForFunction = bases
        mcmForFunction = mcm(len(basesForFunction), basesForFunction)
        
    ##print("el mcmForFunction: {}".format(mcmForFunction))
    #Aplicando formula
    PosValoresMult = []
    cantidad = int(input("Ingrese la cantidad de valores posibles del multiplicador:"))
    for t in range(0, cantidad):
        PosValoresMult.append(1 + mcmForFunction * t)
    return PosValoresMult

def PosiblesVAloresC(bases, exponentes):
    posValoresC = 1
    for x in range(0, len(bases)-1):
        posValoresC = posValoresC * (pow(bases[x], exponentes[x]-1)*(bases[x]-1))
    return posValoresC


#Es maximo comun divisor
def mcd(num1, modulo):
    a = max(num1, modulo)
    b = min(num1, modulo)
    while(b != 0):
        res = b
        b = a % b
        a = res
        if(res == 1):
            return True
    return False
    


def ValoresC(posValoresC, modulo):
    cant = posValoresC
    primos = []
    for x in range(0, 999999999):
        if(mcd(x, modulo)):
            primos.append(x)
        else:
            posValoresC += 1
        if(len(primos) == (cant)):
            return(primos)

def ExeGenMulti():
    modulo = int(input("Ingrese el MODULO:"))
    bases, exponentes, cadena = obtener_primos(modulo)
    print("Los posibles valores de a son: {}".format(GenValuesMultiply(modulo, bases)))
    semilla = random.randint(0, modulo-1)
    print("El valor de la semilla es: {}".format(semilla))
    posValoresC = PosiblesVAloresC(bases, exponentes)
    print("Los posibles valores de C son: {}".format(posValoresC))
    if(posValoresC > 1000):
        posValoresC = 1000
    print("{}".format(ValoresC(posValoresC, modulo)))


def Init():
    ExeGenMulti()


if __name__ == "__main__":
    Init()

