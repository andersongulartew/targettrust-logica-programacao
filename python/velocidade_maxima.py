validadeCNH = "sim"

Validade = input("Já renovou sua CNH: ")

if Validade == validadeCNH:
  print("Você pode dirigir")

else:
  print("Você não pode dirigir, Multa Gravissima")

velocidade_maxima = 80

velocidade = float(input("Digite a velocidade : "))

velocidade_acima = velocidade - velocidade_maxima

if velocidade > 80 and velocidade <= 90:
  print("Multa Leve :", velocidade_acima, "Km/h acima da velocidade permitida")

elif velocidade > 90 and velocidade <= 100:
  print("Multa Grave :", velocidade_acima,
        "Km/h acima da velocidade permitida")

elif velocidade > 100:
  print("Multa Gravissima :", velocidade_acima,
        "Km/h acima da velocidade permitida")

else:
  print("Não houve multa, velocidade permitida !")
