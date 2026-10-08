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

#codigo = input("Ingrese su codigo de usuario: ")
#valor = input("Ingrese el valor ganado: ")
#porciento = float(valor) * 0.13
#print("Usuario con el codigo " + codigo + "" + ", que ha ganado un valor de "
#      + valor + "€ le corresponde un 13% del valor como comision, que esto seria " + str(round(porciento, 2)))

#texto = "Este es el texto de Constan"
#resultado = texto.upper()
#resultado = texto.lower()
#resultado = texto.split("t")
#resultado = texto.find("e")
#resultado = texto.replace("e", "Eli")
#print(resultado)

#a = "aprender"
#b = "python"
#c = "es"
#d = "genial"
#e = " ".join([a, b, c, d])
#print(e)

#lista = ["a", "b", "c"]
#lista.append("d")
#eliminado = lista.pop(1)
#print(lista)
#print(eliminado)

#otra_lista = [5, 2, 4, 3, 1, 0]
#otra_lista.sort()
#otra_lista.reverse()
#print(otra_lista)

#diccionario = {"nombre":"Ionut",
#               "apellido":"Majoru",
#               "peso":"90",
#               "altura":"1.90"}
#diccionario = {"c1":55,
#               "c2":[10, 20, 30],
#               "c3":["a", "e", "i", "o"]}
#resultado = diccionario["nombre"]
#print(diccionario["c3"][1].upper())
#print(diccionario["c3"][1])
#diccionario["5"] = "c4"
#print(diccionario)

'''mascota = "perro"
if mascota == "gato":
    print("tienes un gato")
elif mascota == "perro":
    print("tienes un perro")
else:
    print("no se que masscota tienes")

edad = 16
calificacion = 9
if edad > 18:
    print("eres un adulto")
else:
    print("eres menor de edad")
    if calificacion >= 6:
        print("aprobaste")
    else:
        print("has suspendido")'''

'''cliente = {"nombre": "Constan",
           "edad": 35,
           "sexo": "Masculino",}
pelicula = {"titulo": "Matrix",
            "ficha_tecnica": {"protagonista": "Neo",
                              "director": "hermanos Wachowski"}}
libro = {"titulo": "1984",
         "autor": "George Orwell"}
elementos = [cliente, pelicula, libro]
for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "sexo": sexo,}:
            print("este es un cliente")
            print(nombre, edad, sexo)
        case {"titulo": titulo,
              "ficha_tecnica": {"protagonista":protagonista,
                                "director":director}}:
            print("esta es un pelicula")
            print(titulo, director, protagonista)
        case _:
            print("No se que es esto")'''

'''Adivina el numero'''

class pajaro:
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"Mi color es {self.color}")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")


    def pintar_negro(self):
        self.color="negro"
        print(f"El pajaro ahora es {self.color}")

mi_pajaro = pajaro("blanco", "paloma")
print(mi_pajaro.color)
mi_pajaro.volar(50)
mi_pajaro.pintar_negro()
print(mi_pajaro.color)

