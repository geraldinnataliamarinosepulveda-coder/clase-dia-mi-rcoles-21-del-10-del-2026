"""
Caso. Un curso recibe notas entre 0 y 100, una a una, hasta recibir -99. Muestre la cantidad de notas y
su promedio. El centinela no es una nota y no participa en el cálculo. Si aparece primero, muestre
cantidad cero y «Sin notas» en lugar de un promedio. El flujo siempre contiene -99. El promedio es la
suma de las notas aceptadas dividida entre su cantidad.

"""
cantidad = 0
suma = 0

while True:
	nota = float(input("Ingrese una nota (-99 para terminar): "))
	if nota == -99:
		break
	suma += nota
	cantidad += 1

print("Cantidad de notas:", cantidad)
if cantidad == 0:
	print("Sin notas")
else:
	print("Promedio:", suma / cantidad)