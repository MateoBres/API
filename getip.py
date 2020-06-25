import requests

ip_usuario = input("Ingrese un dominio o un IP: ")


r = requests.get("http://api.ipstack.com/"+ ip_usuario+ "?access_key=4bc5a15c0961819279d1151e6cbe4456")
resultado = r.json()

try:
	if r.status_code == 200:
		print(ip_usuario + ' se encuentra alojado en ' + resultado['country_name'])
except KeyError:
	print('Ocurrió un problema.')

	
