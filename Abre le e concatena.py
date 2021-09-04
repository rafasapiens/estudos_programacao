import sys
 
# Abre o arquivo que criamos no modo de leitura (r)
arquivo = open('meuarquivo.txt')
 
# Lê todas as linhas do arquivo e faz a concatenação com join().
print('\n'.join(arquivo.readlines()))
    
# Sempre feche o arquivo
arquivo.close()