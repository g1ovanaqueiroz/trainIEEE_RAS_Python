from random import randint

# Recebe nome do jogador
nome = input("Digite seu nome: ")

# Imprime as boas vindas
print("*"*100)
print("Bem vindo(a), " + nome + "!\n" +"Será se você consegue adivinhar o número secreto?")
print(("*"*100) + "\n")

# Gera um número aleatório
num_sec = randint(0,9)

# Checa se o número recebido é maior, menor ou igual ao número secreto
achou = False
while not achou:
  num = (int)(input("Digite um numero de 0 a 9: \n"))
  if num < 0 or num > 9:
    print("Entrada inválida! Tente novamente.")
  elif num < num_sec:
    print("Número muito baixo, tente um maior!")
  elif num > num_sec:
    print("Número muito alto, tente um menor!")
  else:
    print("Você acertou!")
    achou = True