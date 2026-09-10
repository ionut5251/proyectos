def ceros_vecinos(*args):
    contador = 0
    for i in args:

        if contador + 1 == len(args):
            return False
        if args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False

print(ceros_vecinos(1, 2, 3, 0, 0, 5))