#Cerveceria
#print('El nombre de tu cerveceria sera:\n'
#      + input('Que animal o elemento de la naturaleza representa el caracter de la marca?: ')
#      + " "
#      + input('Que adjetivo define su sabor o potencia?: ') + '\nFelicidades!!')

#Comisiones
#nombre = input('Ingrese su nombre: ')
#print (nombre)

#palabra1 = "hola "
#palabra2 = "python"
#print(palabra1 + palabra2)

#curso = "Python"
#print("Estas tomando un curso de " + curso)

#num2 = 10
#print(num2)
#print(type(num2))

#num2 = float(num2)
#print(num2)
#print(type(num2))

#num1 = "7.5"
#num2 = "10"
#num1 = float(num1)
#num2 = float(num2)
#print(num1 + num2)
#print(type(num1 + num2))

#resultado = round(90 / 7)
#print(resultado)

#valor = 98.32145
#print(round(valor, 3))

codigo = input("Ingrese su codigo de usuario: ")
valor = input("Ingrese el valor ganado: ")
porciento = float(valor) * 0.13
print("Usuario con el codigo " + codigo + "" + ", que ha ganado un valor de "
      + valor + "€ le corresponde un 13% del valor como comision, que esto seria " + str(round(porciento, 2)))