from random import  randint
from fastapi import FastAPI
import json
import redis
import os
import requests

app = FastAPI()

# Conexión a Redis (host viene de docker-compose)
r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379, decode_responses=True)


@app.get("/ping/")
def ping():
    return {"pong": True}

usuarios = ["asd", "sld", "lñd", "sñlf", "ada", "ñaa", "ida"]

@app.get("/usuarios/{id}")
def get_idUsuario(id: int):
    if 0 <= id < len(usuarios):
        return {"id": id, "nombre": usuarios[id]}

@app.get("/usuarios")
def listar_usuarios():
    return usuarios


