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


def PeriodoMax(bases, exponentes):

    resultado = []
    for x in range(0, len(bases)):
        if(bases[x] == 2):
            if(exponentes[x] >= 3):
                resultado.append(pow(bases[x], (exponentes[x]-2)))
            if(exponentes[x] == 1 or exponentes[x] == 2):
                resultado.append(pow(bases[x], (exponentes[x]-1)))
        else:
            if(bases[x]%2 != 0):
                resultado.append(pow(bases[x], exponentes[x]-1)*(bases[x]-1))
    
    return resultado

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

# Cantidad Posibles valores semilla
def PosValSemilla(bases, exponentes):
    PosValSemilla = 1
    for x in range(0, len(bases)):
        PosValSemilla = PosValSemilla * (pow(bases[x], exponentes[x]-1)*(bases[x]-1))
    return PosValSemilla

        
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

# Valores de la semilla
def ValoresSemilla(CantidadSemilla, modulo):
    cant = CantidadSemilla
    primos = []
    for x in range(0, 999999999):
        if(mcd(x, modulo)):
            primos.append(x)
        else:
            CantidadSemilla += 1
        if(len(primos) == (cant)):
            return(primos)


def MostrarValoresSemilla(cantidad, CantidadSemilla):
    val = []
    for x in range(0, cantidad):
        val.append(CantidadSemilla[x])
    return val


def ValoresMultiplicador(modulo, cantidad):
    valores = []
    p = [3, 11, 13, 19, 21, 27, 29, 37, 53, 59, 61, 67, 69, 77, 83, 91]
    for y in range(0, len(p)):
        for x in range(1, 99999):
            operacion = 200*x+p[y]
            if(operacion < modulo):
                valores.append(operacion)
                if(cantidad == len(valores)):
                    return valores
            else:
                break

def ExeGenMulti():
    modulo = int(input("Ingrese el MODULO:"))
    bases, exponentes, cadena = obtener_primos(modulo)
    #print("La cadena es: " + cadena)

    # Calcular periodo
    ResPeriodoMax = PeriodoMax(bases, exponentes)
    ResPeriodoMax = mcm(len(bases), ResPeriodoMax)
    print("El periodo MAX es: {}".format(ResPeriodoMax))

    # Calculando la cantidad de valores posibles semilla
    CantidadSemilla = PosValSemilla(bases, exponentes)
    print("La cantidad de valores que puede terner la SEMILLA es: {}".format(CantidadSemilla))
    cantidad = int(input("Ingresar la cantidad de valores de la SEMILLA a mostrar: "))
    valSemilla = ValoresSemilla(CantidadSemilla, modulo)
    print(MostrarValoresSemilla(cantidad, valSemilla))

    # Valores Multiplicador
    cantidad2 = int(input("Ingresar la cantidad de valores del MULTILPICADOR a mostrar: "))
    valoresA = ValoresMultiplicador(modulo, cantidad2)
    print("Los valores del multiplicador son: ")
    print(ValoresMultiplicador(modulo, cantidad2))

    print("Mi GLC MULTIPLICATIVO generado es:")
    print("GLC({},{},{})".format(valSemilla[random.randint(0, len(valSemilla))], valoresA[random.randint(0, len(valoresA))], modulo))


def Init():
    ExeGenMulti()


if __name__ == "__main__":
    Init()
