lista = [20, 9, 8, 7]
soma = 0
multiplicacao = 1
for numero in lista:
  if numero % 2 == 0:
    soma = soma + numero  
  else:
    multiplicacao = multiplicacao * numero
print("A soma dos números pares é : ", soma)
print("A multiplicacao dos números ímpares é : ", multiplicacao)