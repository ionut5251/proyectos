from random import choice
palabras = ["python", "programacion", "ahorcado", "variable", "funcion", "diccionario"]
def elegir_palabra(lista_palabras):
    """Elige una palabra al azar de la lista"""
    return choice(lista_palabras)
def mostrar_progreso(palabra, letras_adivinadas):
    """Muestra la palabra oculta con guiones, revelando las letras acertadas"""
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra
        else:
            progreso += "_"
    print(progreso)
def pedir_letra(letras_usadas):
    """Pide una letra al usuario y valida que sea correcta"""
    while True:
        letra = input("Elige una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Debes introducir una única letra válida.")
        elif letra in letras_usadas:
            print("Ya has probado esa letra. Elige otra.")
        else:
            return letra
def letra_en_palabra(letra, palabra):
    """Comprueba si la letra está en la palabra"""
    return letra in palabra
def ha_ganado(palabra, letras_adivinadas):
    """Comprueba si todas las letras de la palabra ya han sido adivinadas"""
    for letra in palabra:
        if letra not in letras_adivinadas:
            return False
    return True
def mostrar_letras_incorrectas(letras_incorrectas, vidas):
    """Muestra las letras incorrectas usadas hasta el momento y las vidas restantes"""
    letras = ", ".join(letras_incorrectas)
    print(f"Letra incorrecta: {letras}. Te quedan {vidas} vidas.")
palabra_secreta = elegir_palabra(palabras)
letras_adivinadas = []
letras_incorrectas = []
letras_usadas = []
vidas = 6
print("¡Bienvenido a El Ahorcado!")
while vidas > 0:
    mostrar_progreso(palabra_secreta, letras_adivinadas)
    if letras_incorrectas:
        mostrar_letras_incorrectas(letras_incorrectas, vidas)

    letra = pedir_letra(letras_usadas)
    letras_usadas.append(letra)

    if letra_en_palabra(letra, palabra_secreta):
        letras_adivinadas.append(letra)
        if ha_ganado(palabra_secreta, letras_adivinadas):
            mostrar_progreso(palabra_secreta, letras_adivinadas)
            print(f"¡Felicidades, has ganado! La palabra era: {palabra_secreta}")
            break
    else:
        vidas -= 1
        letras_incorrectas.append(letra)
if vidas == 0:
    print(f"Has perdido. La palabra era: {palabra_secreta}")