from datetime import date, datetime
from model import Cartao, Compra, cria_cvv_do_cartao, cria_numero_do_cartao, define_validade_do_cartao, limite, cliente, valor


cartao1 = Cartao(cria_numero_do_cartao(), date(2031, 1, 31), '321', 1000.0, 'Steve Rogers', id=1)
cartao2 = Cartao(cria_numero_do_cartao(), date(2035, 5, 31), '789', 2000.0, 'Matt Murdock', id=2)
cartao3 = Cartao(cria_numero_do_cartao(), date(2029, 5, 31), '887', 10000.0, 'Bruce Wayne', id=3)
banco_cartoes = [cartao1, cartao2, cartao3]

sequecia_de_ids = (4)

def lista_cartoes():
    return banco_cartoes

def pesquisa_cartao_por_id(id):
    for cartao in banco_cartoes:
        if cartao.id == id:
            return cartao
    return None

def cadastro_cartao(cliente, limite):
    global sequecia_de_ids, banco_cartoes

numero = cria_numero_do_cartao()
cvv = cria_cvv_do_cartao()
validade = define_validade_do_cartao()

novo_cartao = Cartao(numero=numero, validade=validade, cvv=cvv, limite=limite, cliente=cliente, id=sequecia_de_ids)


banco_compras = []
banco_cartoes.append(novo_cartao)

sequecia_de_ids += 1
cartao_id = sequecia_de_ids

def cadastra_compra(cartao_id, valor, categoria, estabelecimento):
    global sequecia_de_ids, banco_campras

    cartao = pesquisa_cartao_por_id(cartao_id)

    agora = datetime.now()

    nova_compra = Compra(valor=valor, data=agora, estabelecimento=estabelecimento, categoria=categoria,  cartao=cartao, id=sequecia_de_ids)

    banco_compras.append(nova_compra)

