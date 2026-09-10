'''Adivina el numero'''
from random import randint
intentos = 0
estimado = 8
numero_secreto = randint(1, 100)

nombre = input("Hola, ¿cual es tu nombre? ")
print(f"Bienvenido, {nombre}, estoy pensando en un numero entre 1 y 100")

while intentos<10:
    estimado = int(input(f"Intento {intentos + 1}: Adivina el numero: "))
    intentos += 1
    if estimado not in range(1, 101):
        print("Por favor, introduce un numero entre 1 y 100")
        continue
    elif estimado < numero_secreto:
        print("El numero es mayor. Intentalo de nuevo")
    elif estimado > numero_secreto:
        print("El numero es menor. Intentalo de nuevo")
    else:
        print(f"Felicidades, {nombre}! Adivinaste el numero en {intentos} intentos.")
        break
if estimado != numero_secreto:
    print(f"Lo siento, {nombre}. El numero secreto era {numero_secreto}. Mejor suerte la proxima vez!")