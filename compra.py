
from model import Compra, Cartao

visa = Cartao("1234567890123456", "01/2031", "321", 1000.0, "João")

compra_farmacia = Compra(100.0, "10/10/2022 10:00:00", "Farmacia Popular", "Saúde", visa)
compra_restaurante = Compra(89.9, '02/01/2023 12:15:00', 'Burguer King', 'Lazer', visa)
compra_supermercado = Compra(475.5, '03/02/2023 07:05:05', 'Carrefour', 'Alimentação', visa)

#compra_farmacia = Compra()
#compra_restaurante = Compra()
#compra_supermercado = Compra()

print(compra_farmacia)
print(compra_restaurante)
print(compra_supermercado)
def cria_cartao(numero, titular, limite, saldo):
    cartao ={"numero": numero, "titular": titular, "limite": limite, "saldo": saldo}
    return cartao

def compra(cartao, valor):
    cartao["limite"] -= valor

def paga(fatura, valor):
    fatura["limite"] += valor

def extrato(cartao):
    print("Seu limite é  {}".format(cartao["limite"]))

    #datetime
class CompraCredito(Compra):

    def __init__(self, valor, data, estabelecimento, categoria, cartao, quantidade_parcelas):
        super().__init__(valor, data, estabelecimento, categoria, cartao)
        self.__quantidade_parcelas = quantidade_parcelas

    @property
    def valor(self):
        return super().valor *1.1

    @property
    def quantidade_parcelas(self):
        return self.__quantidade_parcelas

    @property
    def valor_parcelas(self):
        return self.valor / self.quantidade_parcelas

