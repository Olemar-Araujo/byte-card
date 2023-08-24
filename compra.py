

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


