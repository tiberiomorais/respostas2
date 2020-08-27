# 7. Faça um algoritmo que leia três números e mostre o maior e o menor deles.

num1 = int(input('\n Informe o 1º número: '))
num2 = int(input('\n Informe o 2º número: '))
num3 = int(input('\n Informe o 3º número: '))


def maior(num_maior):
    print (f'O maior número informado é: {num_maior}')


if num3 < num1 > num2:
    maior(num1)
elif num2 > num3:
    maior(num2)
else:
    maior(num3)


