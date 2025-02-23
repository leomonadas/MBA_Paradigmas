# from abc import ABC, abstractmethod

# class FormaGeometrica(ABC):
#     @abstractmethod
#     def calcular_area(self):
#         raise NotImplementedError("Este método deve ser implementado.")

#     # @abstractmethod
#     # def calcular_perimetro(self):
#     #     raise NotImplementedError("Este método deve ser implementado.")

# class Circulo(FormaGeometrica):
#     def __init__(self, raio):
#         self.raio = raio

#     def calcular_area(self):
#         area = 3.14*self.raio ** 2
#         return area

# class Retangulo(FormaGeometrica):

#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura

#     def calcular_area(self):
#         return  self.largura * self.altura

# circulo1 = Circulo(raio = 10)
# circulo2 = Circulo(raio=2)

# print(circulo1.calcular_area())
# print(circulo2.calcular_area())

# retangulo1 = Retangulo(largura=10, altura=5)
# print(retangulo1.calcular_area())


class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        self.ligado = False
    
    def ligar_motor(self):
        self.ligado = True
        print("Moto ligado!")

class Carro:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def exibir_detalhes(self):
        print(f"Carro {self.marca} {self.modelo}")

    def potencia_motor(self):
        print(f"Motor de potência: {self.motor.potencia} cavalos")


motor1 = Motor(potencia=200)

carro1 = Carro(marca = "Honda", modelo = "Civic", motor = motor1)

carro1.exibir_detalhes()
carro1.potencia_motor()