#FUNCOES
def somar(a,b):
    c=a+b
    return c

def subtrair(a,b):
    c=a-b
    return c
def multiplicar(a,b):
    c=a*b
    return c

def exponenciar(a,b):
    c=a**b
    return c

def dividir(a,b):
   try:
        c=a/b
        return c
   except ZeroDivisionError as zero:
        return 'NAO pode DIVIDIR por ZERO'

def divisaoInteira(a,b):
    try:
        c=a//b
        return c
    except ZeroDivisionError as zero:
        return 'NAO pode DIVIDIR por ZERO'

def resto(a,b):
    try:
        c=a%b
        return c
    except ZeroDivisionError as zero:
        return 'NAO pode DIVIDIR por ZERO'


#EXEMPLOS
print(divisaoInteira(20,0))
print(exponenciar(20,2))