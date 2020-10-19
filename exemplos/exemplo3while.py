# Recebe um inteiro
num = int(input("Digite um número: "))

# Calcula o fatorial
fatorial = num
while num > 1:
  num -=1
  fatorial *= num

# Imprime o fatorial
print(fatorial)