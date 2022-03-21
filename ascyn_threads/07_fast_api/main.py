from fastapi import FastAPI
from pydantic import BaseModel


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False

app = FastAPI()

produtos = [
    Produto(id=1, nome='Playstation 5', preco=5756.55, em_oferta=True),
    Produto(id=2, nome='Playstation 4', preco=2500.45, em_oferta=False),
    Produto(id=1, nome='Playstation 3', preco=1215.56, em_oferta=True),
]


@app.get('/')
async def index():
    return {"Geek": "University"}


@app.get('/produtos/{id}')
async def buscar_produto(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
    return None


@app.put('/produtos/{id}')
async def atualizar_produto(id: int, produto: Produto):
    for prod in produtos:
        if prod.id == id:
            prod = produto

            return prod
    return None


