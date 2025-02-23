class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def emitir_som(self):
        print("Vrummm")
        
    def exibir_detalhes(self):
        print(f"Carro: marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}")
        self.emitir_som()

carro01 = Carro(marca="Toyota", modelo="Corolla", ano=2020)
carro02 = Carro(marca="Renault", modelo="Duster", ano=2014)

carro01.exibir_detalhes()
carro02.exibir_detalhes()