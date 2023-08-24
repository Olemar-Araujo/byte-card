
class Cartao:
    def __init__(self, numero, data_de_validade, cvv, limite, nome_cliente):
        print("Contruindo objeto ...{}".format(self))
        self.__numero = numero
        self.__data_de_validade = data_de_validade
        self.__cvv = cvv
        self.__limite = limite
        self.__nome_cliente = nome_cliente
        self.__status = "Ativo"

    def cancela(self):
        self.__status = "CANCELADO"

    def ativo(self):
        self.__status = "ATIVO"

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value

    @property
    def data_de_validade(self):
        return self.__data_de_validade

    @data_de_validade.setter
    def data_de_validade(self, data):
        if not self.data_de_validade_valida(data):
            raise ValueError("Validade inválida. Use o formato MM/YY")
        self.__data_de_validade = data

    @staticmethod
    def data_de_validade_valida(valida):
        try:
            mes, ano = valida.split("/")
            mes = int(mes)
            ano = int(ano)
            if 1 <= mes <= 12 and len(str(ano)) == 2:
                return True
        except (ValueError, IndexError):
            pass
        return False

    @property
    def CVV(self):
        return self.__cvv

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite