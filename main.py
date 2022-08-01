a = float(input('Insira o valor de a:\n'))
b = float(input('Insira o valor de b:\n'))
c = float(input('Insira o valor de c:\n'))

delta = (b ** 2) - 4 * a * c


if a == 0:
    print('O valor de a nao pode ser zero')
elif delta < 0:
    print('Não existe raiz negativa')
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print(f'x1 = {x1}\n'
          f'x2 = {x2}')
