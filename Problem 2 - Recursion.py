# Ejercicico N.2 para usar Recursion en Python por Michael Pachón

def recursiveReverseString(texto):
    if len(texto) == 0:
        return ""
    else:
        return texto[-1] + recursiveReverseString(texto[:-1])

entrada_texto = input("Ingrese un texto el cual quiere invertir: ")
texto_reves = recursiveReverseString(entrada_texto)
print("El texto invertido es: ",texto_reves) 