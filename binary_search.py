import random


def binary_search(datos, target, bajo, alto):
	if bajo > alto:
		return False

	medio = (bajo + alto) // 2

	if target == datos[medio]:
		return True
	elif target <  datos[medio]:
		return binary_search(datos, target, bajo, medio - 1)
	else:
		return binary_search(datos, target, medio + 1, alto)



if __name__ == '__main__':
	datos = [random.randint(0, 100) for i in range(10)]

	datos.sort()

	print(datos)

	target = int(input('Que numero quieres encontrar? '))
	found = binary_search(datos, target, 0, len(datos) -1)

	print(found)