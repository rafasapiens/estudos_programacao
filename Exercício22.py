nome = str(input('Insira seu nome: ')).strip() # o .strip() remove os espaços antes e depois da string
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu nome tem {} letras a'.format(nome.count('a')))
print('Seu nome tem {} vezes o numero 42'.format(nome.count('42')))

separa = nome.split()

print (separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

         