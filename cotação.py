import requests
import json

req = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='06-13-2019'&$top=100&$format=json")

cotacao = json.loads(req.text)
print(cotacao)
print(req)