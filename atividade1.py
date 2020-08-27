# 1 Faça um algoritmo que peça dois números e imprima o maior deles.

num1 = float(input('Informe o primeiro numero'))
num2 = float(input('Informe o segundo numero'))

if num1 > num2:
    print('O maior é: ', num1)
elif num1<num2:
    print('O maior é: ', num2)
else:
    print('os valores são iguais')
