import sys


clientes = ['pablo', 'ricardo']


def crear_cliente(nombre_cliente):
	global clientes
	
	if nombre_cliente not in clientes:
		clientes.append(nombre_cliente)
	else:
		print('El cliente ya se encuentra en la  BD ')


def lista_clientes():
	for idx, cliente in enumerate(clientes):
		print('{}: {}'.format(idx, cliente))


def actualizar_cliente(nombre_cliente, actualizar_nombre):
	global clientes

	if nombre_cliente in clientes:
		index = clientes.index(nombre_cliente)
		clientes[index] = actualizar_nombre
	else:
		print('El cliente no se encuentra en BD...')


def borrar_cliente(nombre_cliente):
	global clientes

	if nombre_cliente in clientes:
		clientes.remove(nombre_cliente)
	else:
		print('El cliente no se encunetra en BD')


def buscar_cliente(nombre_cliente):
	for cliente in clientes:
		if cliente != nombre_cliente:
			continue
		else:
			return True


def _get_nombre_cliente():
	nombre_cliente = None

	while not nombre_cliente:
		nombre_cliente = input('Cual es el nombre del cliente? ')

		if nombre_cliente == 'exit':
			nombre_cliente = None
			break

	if not nombre_cliente:
		sys.exit()

	return nombre_cliente



def _print_welcome():
	print('BIENVENIDO A MI PROYECTO')
	print('#' * 55)
	print('Que es lo que quieres hacer hoy? ')
	print('[C]rear cliente')
	print('[L]ista de clientes')
	print('[A]ctualizar ciente')
	print('[E]liminar cliente')
	print('[B]uscar cliente')




if __name__ == '__main__':
	_print_welcome()

	comando = input()
	comando = comando.upper()

	if comando == 'C':
		nombre_cliente = _get_nombre_cliente()
		crear_cliente(nombre_cliente)
		lista_clientes()
	
	elif comando == 'L':
		lista_clientes()
	
	elif comando == 'A':
		nombre_cliente = _get_nombre_cliente()
		actualizar_nombre = input('Cual es el nuevo nombre del cliente? ')

		actualizar_cliente(nombre_cliente, actualizar_nombre)
		lista_clientes()

	elif comando == 'E':
		nombre_cliente = _get_nombre_cliente()
		borrar_cliente(nombre_cliente)
		lista_clientes()

	elif comando == 'B':
		nombre_cliente = _get_nombre_cliente()
		found = buscar_cliente(nombre_cliente)

		if found:
			print('El cliente: {} se encunetra en BD'.format(nombre_cliente))
		else:
			print('El cliente: {} no se encunetra en BD'.format(nombre_cliente))
	
	else:
		print('Comando invalido')
	