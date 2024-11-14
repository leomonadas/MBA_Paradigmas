from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

#map, filter, reduce

#filtrar os numeros pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
numeros_pares_dobrado = list(map(lambda x: x * 2, numeros_pares))
soma_numeros_pares_dobrado = reduce(lambda x, y: x + y, numeros_pares_dobrado)
print(numeros_pares)
print(numeros_pares_dobrado)
print(soma_numeros_pares_dobrado)