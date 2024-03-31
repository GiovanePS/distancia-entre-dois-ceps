import urllib.request
import json

def cep_request(cep: str) -> str:
  url = f'https://viacep.com.br/ws/{cep}/json'
  headers = { 'User-Agent': 'Autociencia/1.0' }
  requisicao = urllib.request.Request(url=url, headers=headers, method='GET')
  cliente = urllib.request.urlopen(requisicao)
  conteudo = cliente.read().decode('utf-8')
  endereco = json.loads(conteudo)
  cliente.close()

  if "cep" in endereco:
    return endereco["bairro"], endereco["localidade"]
  else:
    return 'Não Localizado'