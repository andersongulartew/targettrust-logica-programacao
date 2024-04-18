# o fatorial de um numero

valor = int(input("Digite un numero para calculo d fatiorial: "))

fatorial = 1
for i in range(1, valor + 1):
  fatorial = fatorial * i

print("O fatorial de", valor, "é", fatorial)
