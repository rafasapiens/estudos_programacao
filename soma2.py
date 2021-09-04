#TPW260 - Python para zumbis - https://www.youtube.com/watch?v=HmS66jBu_po&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=22

print('\nCalcule a soma de diversos números\n')

n=1
soma=0.0
while True:
    x=float(input('Insira o %d número (insira "0" para o TOTAL): ' %n))
    if x==0:
        break
    n=n+1
    soma=soma+x
print('O TOTAL é %.2f' %soma)
