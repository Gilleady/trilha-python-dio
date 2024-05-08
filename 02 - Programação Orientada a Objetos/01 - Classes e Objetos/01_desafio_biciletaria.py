class Bicicleta:
    def __init__(self, cor, modelo, ano, valor) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    

    def buzinar(self):
        print("Bip bip")
    

    def parar(self):
        print("Freando ...")
        print("Parado")
    

    def correr(self):
        print("Vruumm ...")


    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


bicicleta_1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
bicicleta_1.buzinar()
bicicleta_1.parar()
bicicleta_1.correr()
print(bicicleta_1.cor, bicicleta_1.modelo, bicicleta_1.ano, bicicleta_1.valor)


bicicleta_2 = Bicicleta("Verde", "Monark", 2000, 189)
print(bicicleta_2)
Bicicleta.correr(bicicleta_2) # bicicleta_2.correr()
