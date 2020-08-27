# 5 Faça um algoritmo para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# ✓A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# ✓A mensagem "Reprovado", se a média for menor do que sete;
# ✓A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Informa a nota 1 '))
nota2 = float(input('Informa a nota 2 '))

media = (nota1 + nota2)/2
aprovado = media >=7.0
reprovado = media <7.0
ap_distinção = media ==10.0

if ap_distinção:
    print('AP COM DISTINÇÃO')
elif aprovado:
    print('APROVADO')
else:
    print('REPROVADO')
