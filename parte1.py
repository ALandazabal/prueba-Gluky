#Prueba técnica Parte 1

def calculo_puntos():
	print("******Bienvenid@ al calculo automático de puntos******")
	print("\n Por favor ingresa los siguientes datos:\n")

	flag = True

	while flag:
		cuota = int(input('Cuota: '))

		if cuota > 0:
			break #flag = False
		else:
			print('Cuota debe ser mayor a 0\n')

	while flag:		
		venta = int(input('Venta: '))

		if venta > 0:
			break
		else:
			print('Venta debe ser mayor a 0\n')

	while flag:
		producto = int(input('Producto(1-Gomas, 2-Galletas): '))

		if producto == 1 or producto == 2:
			break
		else:
			print('Producto debe ser 1-Gomas ó 2-Galletas\n')

	while flag:
		segmento = int(input('Segmento(1-Oro, 2-Plata, 3-Bronce): '))

		if segmento == 1 or segmento == 2 or segmento == 3:
			break
		else:
			print('Segmento debe ser 1-Oro ó 2-Plata ó 3-Bronce\n')

	salida = 0

	if venta > cuota:
		if producto == 1:
			if segmento == 1:
				salida = 234000
				if venta > (cuota*150/100):
					salida = salida + 20000
		else:
			if segmento == 1:
				salida = 156000
				if venta > (cuota*150/100):
					salida = salida + 30000
			elif segmento == 3:
				salida = 120000
	elif venta < cuota:
		if segmento == 2:
			salida = 1000


	return salida


if __name__ == '__main__':
    puntos = calculo_puntos()

    if puntos > 0:
    	print(f'La cantidad de puntos es {puntos}')
    else:
    	print('Debes realizar más ventas para que puedas obtener puntos.')
