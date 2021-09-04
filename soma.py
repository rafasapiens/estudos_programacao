#TPW230 - Python para zumbis -https://www.youtube.com/watch?v=bnUiJhfgzHk&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=19

print('\nCalcule a soma de 10 números\n')
n=1
soma=0
while n<=10:
    x=int(input('Insira o %d número: '%n))
    soma=soma+x
    n=n+1
print('A soma é %d'%soma)
print('A média é ',soma/10) 
