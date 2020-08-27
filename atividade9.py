# 9. Faça um algoritmo que leia três números e mostre-os em ordem
# decrescente.

num1 = int(input('\n Informe o 1º número: '))
num2 = int(input('\n Informe o 2º número: '))
num3 = int(input('\n Informe o 3º número: '))

if num3 > num1 < num2:
    pri_menor = num1
    if num2 < num3:
        seg_menor = num2
        ter_menor = num3
    else:
        seg_menor = num3
        ter_menor = num2
elif num2 < num3:
    pri_menor = num2
    if num1 < num3:
        seg_menor = num1
        ter_menor = num3
else:
    pri_menor = num3
    if num2 < num3:
        seg_menor = num2
        ter_menor = num3
    else:
        seg_menor = num3
        ter_menor = num2

print(f'\n Os números em ordem crescente é: {pri_menor, seg_menor, ter_menor}')
