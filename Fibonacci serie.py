# Fibonacci series:
# the sum of two elements defines the next

a, b = 0, 1
while a < 100000:
    print(a)
    a, b = b, a+b
#sem pular nova linha
a, b = 0, 1
while a < 100000:
    print(a, end='')
    a, b = b, a+b
    
#Definindo uma função para chamar mais rapidamente e não ter que re-escrever o script da série Fibonacci

def fib(n):     # escreve a série de Fibonacci até n informado
    a,b=0,1
    while a<n:
        print(a)#, end='-\n')
        a,b=b,a+b
    print()
    
#Agora pode chamar a função fib que foi definida
fib(20010)

fib(10)
# Renomear a função fib como uma variável f
f=fib

    
    
    