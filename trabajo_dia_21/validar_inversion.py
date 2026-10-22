"""
Caso. Una actividad recibe ternas de capital C, tasa anual I y cantidad entera de años M. Una terna solo
se acepta si C es no negativo, 0 < I < 100 y M es positivo. Las ternas inválidas se descartan y se recibe
otra completa; el flujo garantiza una terna válida. Para la primera terna válida, muestre el saldo al
terminar cada año y el saldo final. Los intereses se incorporan al saldo una vez por año. La tasa I se
ingresa como porcentaje. Cada interés anual es el saldo anterior multiplicado por I y dividido entre 100;
el nuevo saldo es el saldo anterior más ese interés. Capital y saldos se expresan en una misma unidad
monetaria.
"""
while True:
	capital = float(input("Ingrese el capital: "))
	tasa = float(input("Ingrese la tasa anual (porcentaje): "))
	anios = int(input("Ingrese la cantidad de años: "))

	if capital >= 0 and 0 < tasa < 100 and anios > 0:
		break

for anio in range(1, anios + 1):
	interes = capital * tasa / 100
	capital += interes
	print(f"Saldo al terminar el año {anio}: {capital}")

print(f"Saldo final: {capital}")