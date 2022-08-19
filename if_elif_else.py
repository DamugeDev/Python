media=20
if(media>=0 and media<=20):
    if(media<=20 and media>=14):
        print('Dispensado')

    elif(media<14 and media>=10):
        print('Admitido')
    else:
        print('Excluido')
else:
    print("Media fora do intervalo permitido")