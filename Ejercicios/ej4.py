def contar_primos(n):

    primos = [2]
    iteracion = 3

    if n < 2:
        return 0
    while iteracion <= n:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
            else:
                primos.append(iteracion)
                iteracion += 2

    print(primos)
    return len(primos)
print(contar_primos(250))