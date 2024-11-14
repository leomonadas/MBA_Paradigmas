def soma(a,b):
    return a + b

print (soma(3,4))
print (soma(3,4))

def aplicar_duas_vezes(func, valor):
    #output = func(valor)
    #output = func(outuput)
    return func(func(valor))

def incrementar(x):
    return x + 1

def elevar_ao_quadrado(x):
    return x**2

def divisao_dois(x):
    return x/2

#print(incrementar(6))

print(aplicar_duas_vezes(incrementar, 6))


numeros = [1, 2, 3, 4, 5 ,6]

def aplicar_transformacao(funcao, lista):
    return [funcao(x) for x in lista]


numero_ao_quadrado = aplicar_transformacao(elevar_ao_quadrado, numeros)
numeros_quadrado_dividido_dois = aplicar_transformacao(divisao_dois, numero_ao_quadrado)
print(numero_ao_quadrado)
print(numeros_quadrado_dividido_dois)