texto = input("Ingrese un texto: ")
letras = []
text = texto.lower

letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("Ingrese la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")

cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado {cantidad_letras1} veces la letra '{letras[0]}' en el texto.")
print(f"Hemos encontrado {cantidad_letras2} veces la letra '{letras[1]}' en el texto.")
print(f"Hemos encontrado {cantidad_letras3} veces la letra '{letras[2]}' en el texto.")

print("\n")
print("CANTIDAD DE PALABRAS")

palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en el texto.")

print("\n")
print("Letra INICIAL y letra FINAL")

letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial del texto es: '{letra_inicio}'")
print(f"La letra final del texto es: '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")

palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"El texto invertido es: '{texto_invertido}'")

print("\n")
print("BUSCAR PALABRA PYTHON")

buscar_python = "python" in texto
dic = {True: "Sí", False: "No"}
print(f"¿Se encuentra la palabra 'python' en el texto? {dic[buscar_python]}")