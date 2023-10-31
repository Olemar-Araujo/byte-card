import use_cases

todos_os_cartoes = use_cases.lista_cartoes()
print(f"Cartões pré-cadastrados: {len(todos_os_cartoes)}")

try:
    use_cases.cadastra_compra(1, 200, "Joalheria", "Jóias do Infinito")
except Exception as e:
    print(e)

for compra in use_cases.lista_compras():
    print(compra)

try:
    use_cases.cadastra_compra(1, 0, "Alimentação", "Bom Prato")
except Exception as e:
    print(e)

try:
    use_cases.cadastra_compra(None, 100, "Alimentação", "Boa Pizza")
except Exception as e:
    print(e)

try:
    use_cases.cadastro_cartao("Lucas Silva", 9)
except Exception as e:
    print(e)

try:
    use_cases.cadastro_cartao("Lucas", 11)
except Exception as e:
    print(e)

try:
    use_cases.cadastro_cartao(None, 10)
except Exception as e:
    print(e)

try:
    use_cases.cadastro_cartao("l", 10)
except Exception as e:
    print(e)

try:
    use_cases.cadastra_compra(1, 100, "Alimentação", "Bom Bife")
except Exception as e:
    print(e)