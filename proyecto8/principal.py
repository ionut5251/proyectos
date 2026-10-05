import numeros


def elegir_area():
    """Pregunta al cliente a qué área desea dirigirse y le da el turno correspondiente."""
    while True:
        print("Bienvenido a la Farmacia")
        print("¿A qué área desea dirigirse?")
        print("  [P] Perfumería")
        print("  [F] Farmacia")
        print("  [C] Cosmética")
        area = input("Elija una opción: ").strip().upper()

        if area == "P":
            numeros.turno_perfumeria()
            break
        elif area == "F":
            numeros.turno_farmacia()
            break
        elif area == "C":
            numeros.turno_cosmetica()
            break
        else:
            print("\nOpción no válida. Inténtelo de nuevo.\n")


def otro_turno():
    """Pregunta si se quiere sacar otro turno."""
    while True:
        respuesta = input("¿Desea sacar otro turno? [S/N]: ").strip().upper()
        if respuesta == "S":
            print()
            return True
        elif respuesta == "N":
            return False
        else:
            print("Responda S o N.")


def inicio():
    while True:
        elegir_area()
        if not otro_turno():
            print("\nGracias por su visita. ¡Hasta pronto!")
            break


if __name__ == "__main__":
    inicio()