from model import CompraCredito
from teste_cartao import visa


compra_farmacia = CompraCredito(500.0, "10/10/2020 10:00:00", "Farpopular", "Medicamento", visa, 10)
compra_restaurante = CompraCredito(200.0, "10/10/2020 10:00:00", "BomPrato", "Alimentação", visa, 10)
compra_supermercado = CompraCredito(700.0, "10/10/2020 10:00:00", "CompreBem", "Alimentação", visa, 10)

print(f"Compra a crédito: {compra_farmacia.valor} em {compra_farmacia.quantidade_parcelas} x de {compra_farmacia.valor_parcela}")

fatura = [compra_farmacia, compra_restaurante, compra_supermercado]
total = 0
for compra in fatura:
    total += compra.valor
print(f'O total da fatura é: {total}')
