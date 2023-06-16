# Ejercicico N.3 para encontrar la maxima diferencia en Python por Michael Pachón

def diferencia(matriz):
    if len(matriz) < 2:
        return "Sin Diferencia"

    max_diferencia = matriz[1] - matriz[0]
    max_num1 = matriz[0]
    max_num2 = matriz[1]

    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            diferencia = matriz[j] - matriz[i]
            if diferencia > max_diferencia:
                max_diferencia = diferencia
                max_num1 = matriz[i]
                max_num2 = matriz[j]

    return f"{max_diferencia} (la maxima diferencia entre {max_num1} y {max_num2})"

matriz = [7, 2, 9, 5, 1, 6]
resultado = diferencia(matriz)
print(resultado)
