# Recebe peso e altura
altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))

# Calcula o IMC
def calcula_imc (altura, peso):
  x = peso/(altura**2)
  return x

# Imprime o IMC
print(calcula_imc(altura, peso))