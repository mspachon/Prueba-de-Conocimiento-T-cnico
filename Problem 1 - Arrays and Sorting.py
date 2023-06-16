# Ejercicico N.1 para organizar datos en Python por Michael Pachón

datos=[]
cero=0

cantidad=int(input("Ingrese la cantidad de datos que desea ordenar: "))

for cero in range(cantidad):
    dato = input(f"Ingrese el dato #{cero+1}: ")    
    datos.append(dato)

orden = sorted(datos)

print("Datos ordenados: ",orden)

