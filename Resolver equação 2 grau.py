print('Solucionador de Equação de 2º grau')
print('A Equação de segundo grau é dada pela fórmula: ax²+bx+c=0')
print('Insira os coeficientes "a" "b" "c" quando solicitado para resolver a equação')
print('='*70)

a=int(input('Insira o valor de "a": '))
b=int(input('Insira o valor de "b": '))
c=int(input('Insira o valor de "c": '))

#Formula de Bhaskara:
# x = (-b+-raiz² de delta)/2a
# delta = b²-4ac

delta = (b)**2-(4*a*c)

print('Delta é =', delta)
try:
    raiz=float(delta**(1/2))
    print('Raiz é =', raiz)
except:
    print('A Equação não possui raízes de números Reais')
    
try:
    x1= float((-b+raiz)/(2*a))
    x2= float((-b-raiz)/(2*a))

    print("X' é =", x1)
    print("X'' é =", x2)
except:
    print('Não foi possível encontrar raízes válidas para os números reais')