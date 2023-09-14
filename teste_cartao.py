from datetime import date
from model import Cartao

visa = Cartao("1234567890123456", "01/2031", 123, 1000.0, "João")
mastercard = Cartao("4567890123456789", "02/2031", 321, 1000.0, "Maria")

print(visa.numero)
print(visa.validade)
print(visa.cvv)
print(visa.limite)
print(visa.cliente)
print(visa.status)


print(mastercard.numero)
print(mastercard.validade)
print(mastercard.cvv)
print(mastercard.limite)
print(mastercard.cliente)
print(mastercard.status)

visa.cancela()
mastercard.cancela()

print(visa.status)
print(mastercard.status)

print()

visa.limite = 5000.0
mastercard.limite = 7500.0

print(visa.limite)
print(mastercard.limite)
print()

cartao_invalido = Cartao("1111 2222 3333 4444", "5/29", 321, 1000, "Carlos")

visa = Cartao("2222 3333 4444 5555", date(2031, 1, 31), 333, 1000, "Eduardo")
