#RECURSÃO
#ENTRADA -> FUNÇÃO -> SAIDA (PRÓPRIA FUNÇÃO)

#CALCULA O FATORIAL DE 4
# def fatorial(numero):
#     if numero == 0:
#         return 1
#     else:
#         return numero * fatorial(numero-1)

# print(fatorial(4))

#FIBONACCI
def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero - 2) + fibonacci(numero - 1)

print(fibonacci(6))