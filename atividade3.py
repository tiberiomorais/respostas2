# 3 Faça um algoritmo que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F -Feminino, M -Masculino, Sexo Inválido.

letra = input('Informe a letra ')

masculino = 'M'
feminino = 'F'

if letra == masculino:
    print('Masculino')
elif letra == feminino:
    print('Feminino')
else:
    print('Sexo Inválido')

