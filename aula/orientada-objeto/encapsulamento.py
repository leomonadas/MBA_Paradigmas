class ContaBancaria:

    def __init__(self, titular, saldo_inicial = 0):
        self.titular = titular #atributo publico
        self.__saldo = saldo_inicial #atributo privado encapsulado apenas nessa classe

    def get_saldo(self): #método que retorna o atributo privado dentro da própria instância
        return self.__saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor de depósito deve ser positivo.")

conta_a = ContaBancaria(titular="Maria", saldo=200)
conta_b = ContaBancaria(titular="José", saldo=40000)

# print(conta_a.titular, conta_a.__saldo_inicial)
#O atributo saldo inicial dará erro porque é um atributo privado, não são revelados informações sensíveis

print(conta_a.get_saldo())