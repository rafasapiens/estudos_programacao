# encoding: utf-8
#https://www.codenation.dev/acceleration/frontend-vuejs-2/challenge/dev-ps
import requests

req = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=3cb2a0fb324f644ff94d185efa2cc3fb0d4a3e47')
print(req)
print(req.content)
dic = req.content
print(type(dic))
def decript(msg):
    s=''
    for c in msg:
        s+=chr(ord(c)-2)
        #if ' ' ==\x1d:
            #return s
    return s

print(decript("ctvkhkekcn kpvgnnkigpeg wuwcnna dgcvu pcvwtcn uvwrkfkva. wpmpqyp"))

