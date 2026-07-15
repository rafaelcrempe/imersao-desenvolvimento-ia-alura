# main.py – servidor FastAPI simples

# Importa a classe FastAPI necessária para criar a aplicação
from fastapi import FastAPI

# Cria a instância da aplicação FastAPI
app = FastAPI()


@app.get("/")
async def hello_world():
    """Endpoint raiz que devolve uma saudação em JSON.

    Retorna:
        dict: Mensagem de boas‑vindas.
    """
    return {"mensagem": "Olá, mundo! 🌍"}

# -------------------------------------------------
# Endpoint GET "/figurinhas" - lista de figurinhas de exemplo
# -------------------------------------------------
@app.get("/figurinhas")
def listar_figurinhas():
    """
    Retorna uma lista fixa com duas figurinhas de exemplo.
    Cada figurinha possui: id (int), nome (str) e categoria (str).
    """
    return [
        {"id": 1, "nome": "Hamurabi", "categoria": "Mesopotâmia"},
        {"id": 2, "nome": "Gilgamesh", "categoria": "Mesopotâmia"},
    ]
