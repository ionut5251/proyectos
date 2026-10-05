"""Contiene los generadores de turnos de cada área y el decorador que añade el texto antes y después del número."""


def generador_turnos(prefijo):
    """Genera turnos infinitos con el prefijo indicado: P-1, P-2, P-3..."""
    numero = 1
    while True:
        yield f"{prefijo}-{numero}"
        numero += 1


gen_perfumeria = generador_turnos("P")
gen_farmacia = generador_turnos("F")
gen_cosmetica = generador_turnos("C")


def mensaje_turno(funcion):
    """Envuelve la función que da el turno con el texto para el cliente."""
    def envoltura():
        print("\n" + "*" * 30)
        print("Su turno es:")
        print(f"     {funcion()}")
        print("Aguarde y será atendido")
        print("*" * 30 + "\n")
    return envoltura


# ---------- FUNCIONES DE CADA ÁREA ----------
@mensaje_turno
def turno_perfumeria():
    return next(gen_perfumeria)


@mensaje_turno
def turno_farmacia():
    return next(gen_farmacia)


@mensaje_turno
def turno_cosmetica():
    return next(gen_cosmetica)