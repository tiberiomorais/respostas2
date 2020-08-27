# 8. Faça um algoritmo que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais
# barato.

prod1 = int(input('\n Informe o preço do 1º produto: '))
prod2 = int(input('\n Informe o preço do 2º produto: '))
prod3 = int(input('\n Informe o preço do 3º produto: '))




def calcula_menor(prod1,prod2,prod3):
    if prod3 > prod1 < prod2:
        return prod1
    elif prod2 < prod3:
        return prod2
    else:
        return prod3




print(f'\n O menor é:{calcula_menor(prod1,prod2,prod3)}')