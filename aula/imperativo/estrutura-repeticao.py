# SOMAR NÚMEROS ATÉ ATINGIR UM LIMITE
limite = 100
soma = 0
numero = 1

# ENQUANTO A SOMA FOR MENOR QUE O LIMITE, CONTINUE SOMAND
while soma < limite:
    soma += numero
    numero += 1
    print(soma)
    print(numero)

#ENCONTRAR O PRIMEIRO NUMERO DIVISIVÉL POR 8 EM UM INTERVALO
# 1 -> 99
for numero in range(1,100):
    if numero % 8 == 00:
        print(numero)
        break


#VERIFICAR SE TODOS OS ITENS DE UMA LISTA SÃO POSITIVOS
numeros = [1,2,3,4,-13]
todos_positivos = True

for numero in numeros:
    if numero < 0:
        todos_positivos = False
        print("TEM ALGUM NUMERO NEGATIVO")
        break

if todos_positivos == True:
    print("TODOS OS NÚMERO SÃO POSITIVOS")

