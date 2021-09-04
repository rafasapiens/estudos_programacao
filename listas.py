# -*- coding: utf-8 -*-
lista1 = [1,2,5,7,12,3]
lista2 = ["laranja","limão","maçã","pera","melancia","mamão"]
lista3 = []

print (lista1)

tamanho1 =len(lista1)

lista2.append("abacate")
print (lista2)

print ("Lista 1 possui", tamanho1, "elementos")
print (lista3)
lista3.append(55)
print(lista3)

if "pera" in lista2:
    print("Comprar",lista2[3])
    
del lista2[0:2]
print(lista2)

for item in lista2:
    print(item)
