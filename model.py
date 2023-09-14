import re
class Cartao:
    def __init__(self, numero, validade, cvv, limite, cliente):
        self.__numero = numero
        self.__validade = validade
        self.__cvv = cvv
        self.__limite = limite
        self.__cliente = cliente
        self.__status = 'ATIVO'

        print(f"Cartão com validade inválida: {self.__validade}")
    def cancela(self):
        self.__status = 'CANCELADO'
    def ativa(self):
        self.__status = 'ATIVO'

    @property
    def numero(self):
        return self.__numero
    @property
    def validade(self):
        return self.__validade
    @property
    def cvv(self):
        return self.__cvv
    @property
    def limite(self):
        return self.__limite
    @property
    def cliente(self):
        return self.__cliente

    @property
    def status(self):
        return self.__status

    @limite.setter
    def limite(self, limite):
        self.__limite

class Compra:

    def __init__(self, valor, data, estabelecimento, categoria, cartao):
        self._valor = valor
        self.__data = data
        self.__estabelecimento = estabelecimento.split()
        self.__categoria = categoria.split()
        self.__cartao = cartao
    


        if len(self.__estabelecimento) > 10:
            print(f"Nome do estabelecimento grande: {self.__estabelecimento}")

        dia_da_compra = self.__data.strftime('%d/%m/%Y')
        hora_da_compra = self.__data.strftime('%H:%M:%S')
        print(f"Compra realizada dia {dia_da_compra} na hora {hora_da_compra}")
    def __str__(self):
        return f"Compra: {self._valor} no dia {self.__data} em {self.__estabelecimento} no cartao {self.__cartao.numero}"

    @property
    def valor(self):
        return self._valor()


class CompraCredito(Compra):

    def __init__(self, valor, data, estabelecimento, categoria, cartao, quantidade_parcelas):
        super().__init__(valor, data, estabelecimento, categoria, cartao)
        self.__quantidade_parcelas = quantidade_parcelas

    @property
    def valor(self):
        return self._valor *1.1

    @property
    def quantidade_parcelas(self):
        return self.__quantidade_parcelas

    @property
    def valor_parcelas(self):
        return self.valor / self.quantidade_parcelas