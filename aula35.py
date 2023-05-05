#Números para a LOTOFÁCIL

import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
print(f'"Antes" {numeros}')
random.shuffle(numeros)
print(f'"Depois" {numeros}')
print('\033[33m-=\033[m' * 40)
print('\033[1;32mNúmeros da Sorte:', sorted(numeros[0:15]))
print('\033[33m-=\033[m' * 40)
