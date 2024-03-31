import request
import geolocalizacao

def exemplo_de_uso():
  bairro, cidade = request.cep_request("88058-100")
  bairro_cidade = bairro + "-" + cidade
  coordenadaA = geolocalizacao.get_location(bairro_cidade)
  bairro, cidade = request.cep_request("30110-001")
  bairro_cidade = bairro + "-" + cidade
  coordenadaB = geolocalizacao.get_location(bairro_cidade)
  distancia = geolocalizacao.get_distance(coordenadaA, coordenadaB)
  print(distancia)
  

if __name__ == "__main__":
  exemplo_de_uso()