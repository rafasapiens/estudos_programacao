# encoding: utf-8
#https://www.codenation.dev/acceleration/aceleradev-python-2/challenge/dev-ps
import requests
import json
import sys
import hashlib
r= requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=3cb2a0fb324f644ff94d185efa2cc3fb0d4a3e47')
r_text=r.text

cod = json.loads(r.text)
answer=open('answer2.json', 'w')
answer.write(r_text)
answer.close()

url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=3cb2a0fb324f644ff94d185efa2cc3fb0d4a3e47'
answer = {'answer': open('answer.json', 'rb')}

rp = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=3cb2a0fb324f644ff94d185efa2cc3fb0d4a3e47', files=answer)
print(rp.status_code)
print(rp.content)


'''
print('Data',cod)
r.json()
print(r.json())
for i in r:
    print(type(r))
    
print(type(cod))
'''
print(cod['cifrado'])

cifrado = cod['cifrado']
'''
print('Aqui o código criptografado: \n',cifrado)

chave = len(cifrado) 

print(type(cifrado))
'''

def decript(msg):
    s=''
    for c in msg:
        s+=chr(ord(c)-2)
        #if ' ' ==\x1d:
            #return s
    return s

print(decript("d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr ------- ctvkhkekcn kpvgnnkigpeg wuwcnna dgcvu pcvwtcn uvwrkfkva. wpmpqyp"))

def cript(msg):
    s=''
    for c in msg:
        s+=chr(ord(c)+2)
    return s

print(decript(cifrado))
hash=hashlib.sha1(b"artificial intelligence usually beats natural stupidity. unknown")
hex_dig = hash.hexdigest()
print(hex_dig)
