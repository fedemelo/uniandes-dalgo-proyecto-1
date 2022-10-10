# Autor: Federico Melo Barrero, 202021525, f.melo

from sys import stdin

def max_ocur_subsecuencia() -> int:
    X, Y, m = tuple(stdin.readline().split())
    m = int(m)
    
    # Mejor caso: X no contiene ningún caracter de los 2 de Y
    # o X contiene solo 1 de los caracteres de los 2 de Y.
    # Ambos O(n) 

    # X no contiene ningún caracter de Y
    if Y[0] not in X and Y[1] not in X: #2O(n) = O(n)
        return 1
    # X contiene solo 1 de los caracteres de Y
    elif Y[0] not in X or Y[1] not in X: #2O(n)
        if Y[0] in X: 
            if X.count(Y[0]) == 1: #O(n)
                return 2
            else:
                return 3
        elif Y[1] in X:
            if X.count(Y[1]) == 1: #O(n)
                return 2
            else:
                return 3

    # X contiene ambos caracteres de Y. 
    else:
        pass
        # verdadero algoritmo
        # return num_ocur


def main():
    num_casos = int(stdin.readline())
    for _ in range(0, num_casos):
        print(max_ocur_subsecuencia())

main()
