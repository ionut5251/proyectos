import os
import re
import time
import math
import datetime

RUTA_RAIZ = r"F:\Py9\Mi_Gran_Directorio"

PATRON = r"N[a-zA-Z]{3}-\d{5}"

def buscar_numero(archivo):
    with open(archivo, "r", encoding="utf-8", errors="ignore") as f:
        texto = f.read()
    resultado = re.search(PATRON, texto)
    return resultado.group() if resultado else None

def recorrer_directorio(ruta):
    hallazgos = []
    for carpeta, subcarpetas, archivos in os.walk(ruta):
        for nombre in archivos:
            numero = buscar_numero(os.path.join(carpeta, nombre))
            if numero:
                hallazgos.append((nombre, numero))
    return hallazgos

def mostrar_resultados(hallazgos, duracion):
    fecha = datetime.date.today().strftime("%d/%m/%y")
    print("-" * 52)
    print(f"Fecha de búsqueda: {fecha}\n")
    print("ARCHIVO\t\tNRO. SERIE")
    print("-------\t\t----------")
    for nombre, numero in hallazgos:
        print(f"{nombre}\t{numero}")
    print(f"\nNúmeros encontrados: {len(hallazgos)}")
    print(f"Duración de la búsqueda: {duracion} segundos")
    print("-" * 52)

def main():
    inicio = time.time()
    hallazgos = recorrer_directorio(RUTA_RAIZ)
    duracion = math.ceil(time.time() - inicio)
    mostrar_resultados(hallazgos, duracion)

if __name__ == "__main__":
    main()