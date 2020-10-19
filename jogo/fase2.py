from random import randint

# Recebe nome do jogador
nome = input("Digite seu nome: ")

# Imprime as boas vindas
print("*"*100)
print("Bem vindo(a), " + nome + "!\n" +"Será se você consegue adivinhar o número secreto?")
print(("*"*100) + "\n")

# Gera um número aleatório
num_sec = randint(0,9)

#Recebe o número do jogador
num = (int)(input("Digite um numero de 0 a 9: \n"))

# Checa se o número recebido é maior, menor ou igual ao número secreto
if num < 0 or num > 9:
  print("Entrada inválida!")
elif num < num_sec:
  print("Número muito baixo!")
elif num > num_sec:
  print("Número muito alto!")
else:
  print("Você acertou!")