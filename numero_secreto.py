from random import randint
nome = input("Digite seu nome: ")
print("*"*100)
print("Bem vindo " + nome + "!\n" +"Será se você consegue adivinhar o número secreto?")
print(("*"*100) + "\n")
num_sec = randint(0,9)
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