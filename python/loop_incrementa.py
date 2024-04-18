#crie um algoritimo que recebe um  numero e o incrementa por 1 por 10 vezes
#valor = 10;
#em cada repetição : valor + 1;
#valor final deve ser 20;

valor = int(input("Digite um numero: "))

for _i in range(10):
  #print(i)
  valor = valor + 1
  print(valor)
  
print("o valor final é : ", valor)
