import urllib
import urllib.request

try:
    site = urllib.request.urlopen(
        'http://pudim.com.br')
except urllib.error.URLError:
    print('O site não está acessível no momento :(')
else:
    print('O site foi acessado com sucesso!')
