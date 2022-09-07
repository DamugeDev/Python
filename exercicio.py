#Vamos tentar resolver alguns desafios. Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa que:
#a) imprima o maior elemento
#b) imprima o menor elemento
#c) imprima os números pares
#d) imprima o número de ocorrências do primeiro elemento da lista
#e) imprima a média dos elementos
#f) imprima a soma dos elementos de valor negativo

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print("a)")
print(max(lista))

print("b)")
print(min(lista))

print("c")
for i in range(len(lista)):
    if(lista[i]%2==0):
        print(lista[i])

print("d)")
print(lista.count(12))

print("e)")
g=0
for ik in range(len(lista)):
    g+=lista[ik]
print(g/len(lista)-1)

print("f)")
neg=0

for tt in range(len(lista)):
    if(lista[tt]<0):
        neg+=lista[tt]
print(neg)

