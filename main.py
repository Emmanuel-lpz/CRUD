import sys


clientes = [
{
	'nombre': 'Pablo',
	'company': 'Google',
	'email': 'pablo@google.com',
	'posicion': 'Sofware Engineer',
},

{
	'nombre': 'Ricardo',
	'company': 'Facebook',
	'email': 'rochard@google.com',
	'posicion': 'Sr. Sofware Engineer',
}
]


def crear_cliente(nombre_cliente):
	global clientes
	
	if nombre_cliente not in clientes:
		clientes.append(nombre_cliente)
	else:
		print('El cliente ya se encuentra en la  BD ')


def lista_clientes():
	print('uid | nombre | company | email | posicion')
	print('|' * 75)

	for idx, cliente in enumerate(clientes):
		print('{uid} | {nombre} | {company} | {email} | {posicion}'.format(
			uid=idx,
			nombre=cliente['nombre'],
			company=cliente['company'],
			email=cliente['email'],
			posicion=cliente['posicion']))


def actualizar_cliente(cliente_id, actualizar_cliente):
	global clientes

	if len(clientes) - 1 >= cliente_id:
		clientes[cliente_id] = actualizar_cliente
	else:
		print('El cliente no se encuentra en BD...')


def borrar_cliente(cliente_id):
	global clientes

	for idx, cliente in enumerate(clientes):
		if idx == cliente_id:
			del clientes[idx]
			break


def buscar_cliente(nombre_cliente):
	for cliente in clientes:
		if cliente['nombre'] != nombre_cliente:
			continue
		else:
			return True


def _get_nombre_cliente_field(field_nombre, mensaje='Cual es el cliente {} ? '):
	field= None

	while not field:
		field = input(mensaje.format(field_nombre))

	return field


def _get_cliente_from_user():
	cliente = {
	'nombre': _get_nombre_cliente_field('nombre'),
	'company': _get_nombre_cliente_field('company'),
	'email': _get_nombre_cliente_field('email'),
	'posicion': _get_nombre_cliente_field('posicion')
	}

	return cliente



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
		cliente =_get_cliente_from_user()

		crear_cliente(cliente)
		lista_clientes()
	
	elif comando == 'L':
		lista_clientes()
	
	elif comando == 'A':
		cliente_id = int(_get_nombre_cliente_field('id'))
		actualizar_cliente = _get_cliente_from_user()

		actualizar_cliente(cliente_id, actualizar_cliente)
		lista_clientes()

	elif comando == 'E':
		cliente_id = int(_get_nombre_cliente_field('id'))

		borrar_cliente(cliente_id)
		lista_clientes()

	elif comando == 'B':
		nombre_cliente = _get_nombre_cliente_field('nombre')
		found = buscar_cliente(nombre_cliente)

		if found:
			print('El cliente: {} SI encunetra en BD'.format(nombre_cliente))
		else:
			print('El cliente: {} NO se encunetra en BD'.format(nombre_cliente))
	
	else:
		print('Comando invalido')
	