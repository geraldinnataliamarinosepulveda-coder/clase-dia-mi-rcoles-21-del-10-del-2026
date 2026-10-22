"""
Caso. Una actividad recibe dos enteros A y B con A < B. Muestre, en orden ascendente, todos los enteros
estrictamente mayores que A y menores que B. Los extremos no se muestran. Si no hay enteros entre
ellos, informe «No hay enteros interiores».

"""
A = int(input("Ingrese A: "))
B = int(input("Ingrese B: "))

if A + 1 >= B:
	print("No hay enteros interiores")
else:
	for numero in range(A + 1, B):
		print(numero)