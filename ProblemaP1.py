# Autor: Federico Melo Barrero, 202021525, f.melo

from sys import stdin

def max_ocur_subsecuencia() -> int:
    X, Y, m = tuple(stdin.readline().split())
    m = int(m)
    
    # return num_ocur


def main():
    num_casos = int(stdin.readline())
    for _ in range(0, num_casos):
        print(max_ocur_subsecuencia())

main()
