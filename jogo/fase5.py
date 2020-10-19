from random import randint

# Recebe nome do jogador
nome = input("Digite seu nome: ")

# Boas vindas ao jogador
def boas_vindas(nome):
  print("*"*100)
  print("Bem vindo " + nome + "!\n" +"Será se você consegue adivinhar o número secreto?")
  print(("*"*100) + "\n")

# Analisa de o jogador acertou ou errou o número
def analise(num):
  achou = False
  tentativas = []
  while (not achou):
    num = (int)(input("Digite um numero de 0 a 9: \n"))
    if num < 0 or num > 9:
      print("Entrada inválida! Tente novamente.\n")
    elif num < num_sec:
      print("Número muito baixo, tente um maior!")
      tentativas.append(num)
      print("Números que você já testou: " + str(tentativas) + "\n")
    elif num > num_sec:
      print("Número muito alto, tente um menor!")
      tentativas.append(num)
      print("Números que você já testou: " + str(tentativas) + "\n")
    else:
      achou = True
      print("Você acertou!")

# Gera um número aleatório
num_sec = randint(0,9)

# Chama as funções definidas acima
boas_vindas(nome)
analise(num_sec)