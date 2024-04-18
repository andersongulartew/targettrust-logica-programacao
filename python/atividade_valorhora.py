# escreva um programa que retorne o valor hora
# de um funcionario com base no seu salario mensal
# e horas trabalhadas por mes.

# Informações
# salario_mensal = 7000,00
# horas_mensal = 160

salarioMensal = int(input("Digite o primeiro valor: "))
horasTrabalhadas = int(input("Digite o segundo valor: "))

valorhora = salarioMensal / horasTrabalhadas

valorhora = print("o valor da hora trabalhada é :", round(valorhora, 2))
