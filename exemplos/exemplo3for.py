# Recebe um inteiro qualquer
num = int(input("Digite um número: "))

# Calcula o fatorial
fatorial = num
for i in range(num - 1, 1, -1):
  fatorial *= i

# Imprime na tela o fatorial do número recebido
print(fatorial)