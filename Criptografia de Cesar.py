import requests
#from bs4 import BeatifulSoup

desafio=requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=3cb2a0fb324f644ff94d185efa2cc3fb0d4a3e47')



def decript(msg):
    s=''
    for c in msg: s+=chr(ord(c)-2)
        #if ' ' ==\x1d:
    return s

decript('d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr')

def cript(msg):
    s=''
    for c in msg:
        s+=chr(ord(c)+2)
    return s
print(desafio)

print('\033[1;33;44m')

