# 10. Faça um algoritmo que pergunte em que turno você estuda. Peça para
# digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem
# "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o
# caso.

turno = input('Informe o turno em que você estuda (M,V ou N): ')
turno = turno.upper()
if turno == 'M':
    print('Matutino')
elif turno =='V':
    print('Vespertino')
elif turno =='N':
    print('Noturno')
else:
    print('Valor Inválido')