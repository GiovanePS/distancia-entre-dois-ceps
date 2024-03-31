from fastapi import FastAPI
from fastapi.responses import JSONResponse

import geolocalizacao
import request

app = FastAPI()

@app.get("/")
def hello_world_root():
  return {"Hello": "World"}

@app.get("/ceps")
async def get_ceps(cep1: str = '', cep2: str = ''):
  if cep1 == '':
    return JSONResponse(content={"error": "cep1 não enviado."}, status_code=400)
  
  if cep2 == '':
    return JSONResponse(content={"error": "cep2 não enviado."}, status_code=400)
  
  try:
    bairro, cidade = request.cep_request(cep1)
  except:
    return JSONResponse(content={"error": "cep1 incorreto ou inexistente."}, status_code=400)
  bairro_cidade = bairro + "-" + cidade
  coordenadaA = geolocalizacao.get_location(bairro_cidade)

  try:
    bairro, cidade = request.cep_request(cep2)
  except:
    return JSONResponse(content={"error": "cep2 incorreto ou inexistente."}, status_code=400)
  bairro_cidade = bairro + "-" + cidade
  coordenadaB = geolocalizacao.get_location(bairro_cidade)

  distancia = geolocalizacao.get_distance(coordenadaA, coordenadaB)
  return JSONResponse(content={"distancia": distancia})