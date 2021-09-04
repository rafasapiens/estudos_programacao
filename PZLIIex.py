#Exercícios Lista II Python para zumbis
#Exercicio 1
import math

print ('Calcule os dados do triangulo.')
t=input('A figura que você quer calcular é um triangulo? s/n: ')
if t== 'n':
    print('Lamento, posso apenas calcular triangulos')
    exit()
else:
    print('Ok vamos começar')
try:
    a=int(input('Informe o lado do triangulo: '))
    b=int(input('Informe o lado 2 do triangulo: '))
    c=int(input('Informe o lado 3 do triangulo: '))
          
    p=((a+b+c)/2)
    area=math.sqrt((p*(p-a)*(p-b)*(p-c)))
    
    print('O perímetro do triangulo é ',2*p)
    print('A area do triangulo é %f metros quadrados' %area)
          
    if a==b==c:
          print('O triangulo é equilátero')
    elif a!=b!=c!=a:
          print('O triangulo é escaleno')
    else:
          print('O triangulo é isóceles')
          
except ValueError:
          print ('Os dados informados não são de um triangulo')

#Exercicio 2
import datetime
print('Data de hoje: ',datetime.datetime.today())
ano=int(input('Insira o ano: '))
try:
    d=bool(datetime.date(ano,2,29))

    if d ==True:
        print('É bissexto')
        
except ValueError:
    print('Não é bissexto')
#d=bool(datetime.date(2016,2,29))

#print(d)
    

#Exercício 3

peso=float(input('Informe quantos quilos de peixe: '))
excesso= int(peso-50)
multa= float(excesso*4)
if peso<=50:
    multa=0
    excesso=0
print('Você excedeu',excesso, 'quilos e o valor da multa é R$ %.2f' %multa)


#Exercício 4
n1=int(input('Insira um número: '))
n2=int(input('Insira um número: '))
n3=int(input('Insira um número: '))
             
if n1 >n2 and n1 >n3:
    print(n1, 'é o maior número inserido')
elif n2>n1 and n2>n3:
    print(n2, 'é o maior número inserido')
else:
    print(n3, 'é o maior número inserido')
             

#Exercício 5
n1=int(input('Informe um número: '))
n2=int(input('Informe um número: '))
n3=int(input('Informe um número: '))

if n1>n2 and n1>n3:
    print(n1, 'é o maior número inserido')
elif n2>n1 and n2>n3:
    print(n2, 'é o maior número inserido')
else:
    print(n3, 'é o maior número inserido')
    
if n1<n2 and n1<n3:
    print(n1, 'é o menor número inserido')
elif n2<n1 and n2<n3:
    print(n2, 'é o menor número inserido')
else:
    print(n3, 'é o menor número inserido')
    

#Exercício 6
sh=int(input('Quanto você ganha por hora: '))
ht=int(input('Quantas horas foram trabalhadas no mês: '))

sb= float(sh*ht)
ir= float(sb*0.11)
inss=float(sb*0.08)
sind=float(sb*0.05)
desc=float(ir+inss+sind)
sl=float(sb-desc)

print('Salário Bruto R$ %.2f' %sb)
print('Descontos: \n IR R$ %.2f \n INSS R$ %.2f \n SINDICATO R$ %.2f' %(ir,inss,sind))
print('TOTAL DE DESCONTOS: R$ %.2f' %desc)
print('SALÁRIO LÍQUIDO: R$ %.2f' %sl )




#Exercício 7
ap= int(input('Qual o tamanho da área a ser pintada em m²: '))
ln=(ap/3)
if ap % 54 !=0:
    latas= int(ap/54)+1
else:
    latas=int(ap/54)
prec_un= 80
prec_tot=(latas*prec_un)
print('Serão necessários %d litros e %d latas de tinta de 18 litros' %(ln,latas))
print('Valor unitário da lata R$ %.2f' %prec_un)
print('TOTAL: R$ %.2f' %prec_tot)
