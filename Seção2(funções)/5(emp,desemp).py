"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10

outra_soma = soma(*numeros)

print(outra_soma)

print(sum(numeros))
# print(*numeros)