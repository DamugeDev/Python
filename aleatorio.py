
#Construa um programa que gere aleatoriamente N valores inteiros no intervalo de [–100, 100[ sendo o valor de N dado pelo utilizador.O programa deverá contar quantos valores gerados são positivos e quantos são negativos.

import random
b=int(input('Digite a quantidade de numeros a serem gerados: '))
print('=============')
neg=0
pos=0
while(b>0):
    a= random.randint(-100,100)    
    print(a)
    b-=1
    if(a>0):
        pos+=1
    else:
        neg+=1

print('==============')
print(f'Negativos: {neg} \nPositivos: {pos}')
