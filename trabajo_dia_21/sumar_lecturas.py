"""
Caso. Una actividad recibe números uno a uno hasta que aparezca -50. Muestre la suma de todas las
lecturas anteriores; -50 no forma parte de los datos y nunca se suma. Los demás valores, incluidos
negativos distintos de -50 y el cero, sí participan. Si el primer dato es -50, la suma es cero. El flujo siempre
contiene el centinela.

"""

total = 0
lectura = int(input())

while lectura != -50:
	total += lectura
	lectura = int(input())

print(total)