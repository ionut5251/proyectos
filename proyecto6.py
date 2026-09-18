import os
from pathlib import Path

# Ruta
def obtener_ruta_recetas() -> Path:
    """Devuelve la ruta a la carpeta Recetas dentro del Escritorio del usuario."""
    return Path.home() / "Desktop" / "Recetas"

# Utilidades generales

def limpiar_pantalla() -> None:
    """Limpia la consola, tanto en Windows como en Linux/Mac."""
    os.system("cls" if os.name == "nt" else "clear")
def pausar() -> None:
    """Espera a que el usuario presione una tecla para continuar."""
    input("\nPresiona ENTER para volver al menú principal...")
def contar_recetas(ruta_recetas: Path) -> int:
    """Cuenta todos los archivos de receta dentro de todas las categorías."""
    return sum(1 for archivo in ruta_recetas.rglob("*") if archivo.is_file())
def mostrar_bienvenida(ruta_recetas: Path) -> None:
    """Muestra el mensaje de bienvenida, la ruta y la cantidad de recetas."""
    print("=" * 60)
    print("  BIENVENIDO AL GESTOR DE RECETAS")
    print("=" * 60)
    print(f"Ruta de la carpeta de recetas: {ruta_recetas.resolve()}")
    print(f"Cantidad total de recetas: {contar_recetas(ruta_recetas)}")
    print("=" * 60)

# Selección de categorías y recetas

def listar_categorias(ruta_recetas: Path) -> list[Path]:
    """Devuelve una lista con las subcarpetas (categorías) de Recetas."""
    return [carpeta for carpeta in ruta_recetas.iterdir() if carpeta.is_dir()]
def elegir_categoria(ruta_recetas: Path) -> Path | None:
    """Muestra las categorías disponibles y devuelve la elegida por el usuario."""
    categorias = listar_categorias(ruta_recetas)
    if not categorias:
        print("No hay categorías creadas todavía.")
        return None
    print("\nCategorías disponibles:")
    for i, categoria in enumerate(categorias, start=1):
        print(f"  {i}. {categoria.name}")
    try:
        opcion = int(input("Elige el número de categoría: "))
        if 1 <= opcion <= len(categorias):
            return categorias[opcion - 1]
        print("Opción inválida.")
        return None
    except ValueError:
        print("Debes ingresar un número.")
        return None
def listar_recetas(categoria: Path) -> list[Path]:
    """Devuelve la lista de archivos de receta dentro de una categoría."""
    return [archivo for archivo in categoria.iterdir() if archivo.is_file()]
def elegir_receta(categoria: Path) -> Path | None:
    """Muestra las recetas de una categoría y devuelve la elegida por el usuario."""
    recetas = listar_recetas(categoria)
    if not recetas:
        print(f"No hay recetas en la categoría '{categoria.name}'.")
        return None
    print(f"\nRecetas en '{categoria.name}':")
    for i, receta in enumerate(recetas, start=1):
        print(f"  {i}. {receta.stem}")
    try:
        opcion = int(input("Elige el número de receta: "))
        if 1 <= opcion <= len(recetas):
            return recetas[opcion - 1]
        print("Opción inválida.")
        return None
    except ValueError:
        print("Debes ingresar un número.")
        return None

# Opción 1: Leer receta

def leer_receta(ruta_recetas: Path) -> bool:
    """Permite elegir una categoría y una receta, y muestra su contenido."""
    categoria = elegir_categoria(ruta_recetas)
    if categoria is None:
        return False
    receta = elegir_receta(categoria)
    if receta is None:
        return False
    print(f"\n--- Contenido de '{receta.stem}' ---")
    print(receta.read_text(encoding="utf-8"))
    print("-" * 40)
    return True

# Opción 2: Crear receta

def crear_receta(ruta_recetas: Path) -> bool:
    """Permite elegir una categoría y crear un nuevo archivo de receta en ella."""
    categoria = elegir_categoria(ruta_recetas)
    if categoria is None:
        return False
    nombre = input("Nombre de la nueva receta: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return False
    print("Escribe el contenido de la receta (finaliza con una línea vacía):")
    lineas = []
    while True:
        linea = input()
        if linea == "":
            break
        lineas.append(linea)
    contenido = "\n".join(lineas)
    nuevo_archivo = categoria / f"{nombre}.txt"
    if nuevo_archivo.exists():
        print("Ya existe una receta con ese nombre en esta categoría.")
        return False
    nuevo_archivo.write_text(contenido, encoding="utf-8")
    print(f"Receta '{nombre}' creada correctamente en '{categoria.name}'.")
    return True

# Opción 3: Crear categoría

def crear_categoria(ruta_recetas: Path) -> bool:
    """Crea una nueva carpeta de categoría dentro de Recetas."""
    nombre = input("Nombre de la nueva categoría: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return False
    nueva_carpeta = ruta_recetas / nombre
    if nueva_carpeta.exists():
        print("Ya existe una categoría con ese nombre.")
        return False
    nueva_carpeta.mkdir(parents=True)
    print(f"Categoría '{nombre}' creada correctamente.")
    return True

# Opción 4: Eliminar receta

def eliminar_receta(ruta_recetas: Path) -> bool:
    """Permite elegir una categoría y una receta, y la elimina."""
    categoria = elegir_categoria(ruta_recetas)
    if categoria is None:
        return False
    receta = elegir_receta(categoria)
    if receta is None:
        return False
    confirmacion = input(f"¿Seguro que quieres eliminar '{receta.stem}'? (s/n): ").strip().lower()
    if confirmacion != "s":
        print("Operación cancelada.")
        return False
    receta.unlink()
    print(f"Receta '{receta.stem}' eliminada correctamente.")
    return True

# Opción 5: Eliminar categoría

def eliminar_categoria(ruta_recetas: Path) -> bool:
    """Permite elegir una categoría y eliminarla junto con su contenido."""
    categoria = elegir_categoria(ruta_recetas)
    if categoria is None:
        return False
    confirmacion = input(
        f"¿Seguro que quieres eliminar la categoría '{categoria.name}' y TODAS sus recetas? (s/n): "
    ).strip().lower()
    if confirmacion != "s":
        print("Operación cancelada.")
        return False
    for archivo in categoria.iterdir():
        if archivo.is_file():
            archivo.unlink()
    categoria.rmdir()
    print(f"Categoría '{categoria.name}' eliminada correctamente.")
    return True

# Menú principal

def mostrar_menu() -> str:
    """Muestra las opciones del menú y devuelve la elección del usuario."""
    print("\nMENÚ PRINCIPAL")
    print("1. Leer una receta")
    print("2. Crear una receta")
    print("3. Crear una categoría")
    print("4. Eliminar una receta")
    print("5. Eliminar una categoría")
    print("6. Salir")
    return input("Elige una opción (1-6): ").strip()
def main() -> None:
    ruta_recetas = obtener_ruta_recetas()
    if not ruta_recetas.exists():
        print(f"No se encontró la carpeta de recetas en: {ruta_recetas.resolve()}")
        return
    opcion = ""
    while opcion != "6":
        limpiar_pantalla()
        mostrar_bienvenida(ruta_recetas)
        opcion = mostrar_menu()
        exito = False
        if opcion == "1":
            exito = leer_receta(ruta_recetas)
        elif opcion == "2":
            exito = crear_receta(ruta_recetas)
        elif opcion == "3":
            exito = crear_categoria(ruta_recetas)
        elif opcion == "4":
            exito = eliminar_receta(ruta_recetas)
        elif opcion == "5":
            exito = eliminar_categoria(ruta_recetas)
        elif opcion == "6":
            print("\n¡Hasta la próxima!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
        if exito:
            pausar()
        elif opcion != "6":
            pausar()
if __name__ == "__main__":
    main()