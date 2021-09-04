import sys

# Abre o arquivo que criamos no modo de leitura (r)
arquivo = open ('meuarquivo.txt')

# Le cada linha e mostra no terminal
for linha in arquivo:
    sys.stdout.write(linha)
    
#Sempre feche o arquivo
arquivo.close()