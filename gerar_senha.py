#Gerar senhas usando a biblioteca random
import random

minusculas = "abcdefghijklmnopqrstuvwxyz"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "/*!@#$%&"

ciclo = minusculas+maiusculas+numeros+simbolos
tamanho=8

senha= "".join(random.sample(ciclo,tamanho))

print(f'Senha gerada: {senha}')