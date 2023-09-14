from datetime import datetime, date

from model import CompraCredito
from teste_cartao import visa



compra_farmacia = CompraCredito(500.0, datetime(2023, 1, 1, 10, 0,
0), "Farpopular", "Medicamento", visa, 10)
compra_restaurante = CompraCredito(200.0, datetime(2023, 1, 2,
12, 15, 0), "BomPrato", "Alimentação", visa, 10)
compra_supermercado = CompraCredito(700.0, datetime(2023, 2, 3,
7, 5, 5), "CompreBem", "Alimentação", visa, 10)

print(compra_farmacia)
print(compra_restaurante)
print(compra_supermercado)
print()

compra_amazon = CompraCredito(200.0, datetime(2023, 2, 15, 19, 46,
17), "Amazon", "Casa", visa, 10)

print(f"Compra a crédito: {compra_farmacia.valor} em {compra_farmacia.quantidade_parcelas} x de {compra_farmacia.valor_parcelas}")

print()

fatura = [compra_farmacia, compra_restaurante, compra_supermercado, compra_amazon]
total = 0
for compra in fatura:
    total += compra.valor
print(f'O total da fatura é: {total}')
