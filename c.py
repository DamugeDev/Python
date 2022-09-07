import requests

def check_internet():
    ''' checar conexão de internet '''
    url = 'https://damuge.vercel.app'
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except exceptions.ConnectionError:
        return False

if not check_internet():
    print('Internet fora do ar!')
else:
    print('Internet OK!')