from fastapi import FastAPI
import redis
import os
from random import  randint

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
# guardar la info 