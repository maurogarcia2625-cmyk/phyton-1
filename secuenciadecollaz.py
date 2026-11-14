max_terminos = 0
numero_ganador = 0

for inicio in range(1, 1000000):
    n = inicio
    terminos = 1

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
        terminos += 1

    if terminos > max_terminos:
        max_terminos = terminos
        numero_ganador = inicio

print("Número inicial:", numero_ganador)
print("Cantidad de términos:", max_terminos)