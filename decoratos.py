PASSWORD = '12345'

def password_requerido(func):
    def wrapper():
        password = input('Cual es tu contrasena? ')

        if password == PASSWORD:
            return func()
        else:
            print('La contrasena NO es correcta')

    return wrapper



@password_requerido
def needs_password():
    print('La contraseña es incorrecta')


def upper(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)

        return resultado.upper()

    return wrapper


@upper
def decir_my_nombre(nombre):
    return 'Hola, {}'.format(nombre)


if __name__ == '__main__':
    print(decir_my_nombre('David'))