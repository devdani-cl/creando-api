from Pokemon import Pokemon
from random import  randint
from fastapi import FastAPI
import json
import redis
import os
import requests

app = FastAPI()

# Conexión a Redis (host viene de docker-compose)
r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379, decode_responses=True)

@app.get("/cache/{key}") # endpoit
def set_cache(key: str):
    value = r.get(key)
    if value:
        return {"key": key, "value": value, "cached": True}

    r.set(key, f'nuevo valor{key}', ex=3600)  # expira en 1 hora 
    return {"key": key, "value": key, "cached": False}

@app.get("/usm/alumnos")
def get_alumnos():
    a = randint(0,100)
    b = randint(0,100)
    return [
        {
            "name": "Maximiliano",
            "edad": a
        },
        {
            "name": "Shaquira",
            "edad": b
        }
    ]

@app.get("usm/pokemones")
def get_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/?limit=151"
    response = requests.get(url) 
    poke_json = json.loads(response.text)
    lista_pokemones = [Pokemon(n["name"], n["url"]) for n in poke_json["results"]]
    for p in lista_pokemones:
        hp = p.vidaPokemon()
        print(f'{p.nombre}: {hp} HP')
    
