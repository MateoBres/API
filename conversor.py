import requests

r = requests.get("https://api.recursospython.com/dollar")
if r.status_code == 200:
	resultado = r.json()
	compra = resultado['buy_price']
	venta = resultado['sale_price']
	conversor = ((compra) + (venta))/2
	conv = int(input('Eliga 1 para convertir dolar pesos\nEliga 2 para convertir de pesos a dolar\n'))
	if conv == 1:
		dolar = input('Escriba la cantidad de dolares: ')
		moneda = int(dolar) * conversor
		print(round(moneda,2))
	elif conv == 2:
		pesos = input('Escriba la cantidad de pesos: ')
		moneda = int(pesos) / conversor
		print(round(moneda,2))
	else:
		print('No es valida la seleccion')
	




# ~ r = requests.get("http://localhost:7001/student")
# ~ if r.status_code == 200:
	# ~ print("Ejecutando correctamente.")
	# ~ resultado = r.json()
	# ~ alumnos = resultado["students"]
	# ~ print(alumnos)
	# ~ print(alumnos[0]["name"])
# ~ else:
	# ~ print("Ha ocurrido un error.")
