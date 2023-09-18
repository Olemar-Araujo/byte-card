import use_cases


todos_os_cartoes = use_cases.lista_cartoes()
print(f"Cartões pré-cadastrados: {len(todos_os_cartoes)}")

cartao_existente = use_cases.pesquisa_cartao_por_id(1)
cartao_inexistente = use_cases.pesquisa_cartao_por_id(1000)

print(f"Cartão existente {cartao_existente}")
print(f"Cartão existente {cartao_inexistente}")

use_cases.cadastro_cartao("José Barreto", 5500.0)
for cartao in use_cases.lista_cartoes():
    print(cartao)

use_cases.cadastra_compra(1, 100.0, "vestuário", "Adidas")
use_cases.cadastra_compra(1, 200.0, "deslocamento", "gasolina")
use_cases.cadastra_compra(1, 150.0, "alimentação", "retaurante")

use_cases.cadastra_compra(3, 150, "vestuário", "Nike")
use_cases.cadastra_compra(3, 230.0, "medicamento", "Farmais")