# 4 Faça um algoritmo que verifique se uma letra digitada é vogal ou consoante.

letra = input('Informe a letra')
vogal = ['a','e','i','o','u']
consoante = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

if letra in vogal:
    print('Vogal')
elif letra in consoante:
    print('Consoante')
else:
    print('Não é vogal e nem consoante')


