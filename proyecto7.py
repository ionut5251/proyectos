"""
Proyecto del Día 7 - Cuenta bancaria con Programación Orientada a Objetos.
"""


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0.0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return (f"Cliente: {self.nombre} {self.apellido}\n"
                f"Cuenta N.º: {self.numero_cuenta}\n"
                f"Balance: {self.balance:.2f} €")

    def depositar(self, monto):
        if monto <= 0:
            print("El monto a depositar debe ser mayor que cero.")
            return
        self.balance += monto
        print(f"Depósito de {monto:.2f} € realizado con éxito.")

    def retirar(self, monto):
        if monto <= 0:
            print("El monto a retirar debe ser mayor que cero.")
        elif monto > self.balance:
            print(f"Fondos insuficientes. Tu saldo es de {self.balance:.2f} €.")
        else:
            self.balance -= monto
            print(f"Retiro de {monto:.2f} € realizado con éxito.")


def pedir_monto(mensaje):
    """Pide un número positivo hasta que el usuario introduzca uno válido."""
    while True:
        try:
            monto = float(input(mensaje).replace(",", "."))
            if monto > 0:
                return monto
            print("Introduce una cantidad mayor que cero.")
        except ValueError:
            print("Eso no es un número válido.")


def crear_cliente():
    print("=== Alta de cliente ===")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    numero_cuenta = input("Número de cuenta: ").strip()
    return Cliente(nombre, apellido, numero_cuenta)


def inicio():
    cliente = crear_cliente()
    print("\n" + str(cliente))

    while True:
        print("\n¿Qué deseas hacer?")
        print("  [D] Depositar")
        print("  [R] Retirar")
        print("  [S] Salir")
        opcion = input("Opción: ").strip().upper()

        if opcion == "D":
            cliente.depositar(pedir_monto("Cantidad a depositar: "))
        elif opcion == "R":
            cliente.retirar(pedir_monto("Cantidad a retirar: "))
        elif opcion == "S":
            print(f"\nGracias por usar nuestro banco, {cliente.nombre}. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")
            continue

        print("\n" + str(cliente))


if __name__ == "__main__":
    inicio()