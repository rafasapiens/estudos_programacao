n1=int(input('Insira de 1 a 10 a Nota 1: '))
n2=int(input('Insira de 1 a 10 a Nota 2: '))

soma=n1+n2
media=soma/2
print('Sua média é:', media)
if media>=6:
    print('Aprovado')
else:
    print('Reprovado')