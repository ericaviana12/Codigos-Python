import random

num_min = int(input("Digite o valor mínimo: "))
num_max = int(input("Digite o valor máximo: "))

numero_aleatorio = random.randint(num_min, num_max)

print("Número aleatório:", numero_aleatorio)
