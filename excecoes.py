from decimal import DivisionByZero


a=(input('Insira o divisor: '))

try:
    b=13/a
    print('RESULTADO: ',b)
except IndexError as erro:
    print('Erro de indice')
except ZeroDivisionError as e:
    print('Nao pode ser dividido por zero')


except:
    print('Ocorreu um erro')

