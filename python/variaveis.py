## Tipos de variaveis

# String ========================================================
nome = "Andeson"
sobrenome = "Wodnoff"

print(nome + " " + sobrenome)
print("O nome completo é :", nome, sobrenome)

nome = "João"
print("O nome agora é :", nome, sobrenome)

# Integer ou número inteiro =======================================
idade1 = 25
idade2 = 15

totalIdade = idade1 + idade2

print("A idade total é :", totalIdade)
#
totalIdade = idade1 / idade2

print("A divisão  é :", totalIdade)
# #
# print(type(xxxx)) # identifica o tipo da variavel

# Float ou número decimal =========================================
valorFloat01 = 20.55
valorFloat02 = 3.5

totalFloat = valorFloat01 / valorFloat02
print(type(totalFloat))

print("A soma é :", totalFloat)

print("A soma é :", round(totalFloat, 2))
#o round  reduz o valor  dos números após a vírgula

# Boolean ou lógico =================================================

#True ou False
existe = None

print("A variavel que existe é do tipo :", type(existe))

if (existe):
  print("É igual a verdadeiro : ", existe)

elif not existe:
  print("É igual a falso : ", existe)

else:
  print("Não é  Verdadeiro  e nem  Falso :", existe)
