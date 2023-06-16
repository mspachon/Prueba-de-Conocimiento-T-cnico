# Ejercicico N.4 para encontrar la suma de un numero objetivo en Python por Michael Pachón

def encontrar_suma_objetivo(lista, objetivo):
    contenidos = set()

    for num in lista:
        contenido = objetivo - num
        if contenido in contenidos:
            return [num, contenido]
        contenidos.add(num)

    return []

lista = [3, 6, 9, 12, 4, 1]
objetivo = 10
resultado = encontrar_suma_objetivo(lista, objetivo)
if resultado:
    suma = resultado[0] + resultado[1]
    print(f"{resultado} ({resultado[0]} + {resultado[1]} = {suma})")
else:
    print("[]")

