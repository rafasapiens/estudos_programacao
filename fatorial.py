#TPW250 - Python para zumbis - https://www.youtube.com/watch?v=1i9w5Sbuylc&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=20
print('\nCalcule o fatorial de \n')
contador=1
fat=1
x=int(input('Insira o número para saber seu fatorial: '))
while contador<=x:
    fat=fat*contador
    contador=contador+1
print('O fatorial de %d é %d' %(x,fat))

