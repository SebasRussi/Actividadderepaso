from random import randint


numeros_aleatorios = [randint(1, 50) for i in range(0, 50)]
print(numeros_aleatorios)
print("el numero mas GRANDE es ", max(numeros_aleatorios))
print("el numero mas PEQUEÑO es ", min(numeros_aleatorios))