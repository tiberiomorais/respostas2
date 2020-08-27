# 6 Faça um algoritmo que leia três números e mostre o maior deles.
num1 = float(input('Informa o num 1 '))
num2 = float(input('Informa o num 2 '))
num3 = float(input('Informa o num 3 '))

maior1 = num1>num2 and num1>num3
maior2 = num2>num1 and num2>num3
maior3 = num3>num1 and num3>num2

if maior1:
    print('O maior é ', num1)
elif maior2:
    print('O maior é ', num2)
else:
    print('O maior é', num3)