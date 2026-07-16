# main.py – API de álbum de figurinhas com arquivos estáticos

"""Servidor FastAPI que expõe uma lista de figurinhas e disponibiliza as imagens das figurinhas como arquivos estáticos.
"""

# -------------------------------------------------
# Imports necessários
# -------------------------------------------------
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

# -------------------------------------------------
# Configuração de caminhos absolutos
# -------------------------------------------------
# Diretório onde este arquivo está localizado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
# Diretório que contém as imagens das figurinhas (criar a pasta 'figurinhas')
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# -------------------------------------------------
# Criação da aplicação FastAPI
# -------------------------------------------------
app = FastAPI()

# -------------------------------------------------
# Montagem da pasta de arquivos estáticos
# Rotas como '/imgs/...jpg' servirão arquivos da pasta PASTA_IMAGENS
# -------------------------------------------------
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# -------------------------------------------------
# Dados estáticos das figurinhas (id, nome, categoria, caminho da imagem)
# -------------------------------------------------
figurinhas = [
    {"id": 1, "nome": "Hamurábi", "categoria": "Mesopotâmia", "imagem_url": "/imgs/01-hamurabi.jpg"},
    {"id": 2, "nome": "Gilgamesh", "categoria": "Mesopotâmia", "imagem_url": "/imgs/02-gilgamesh.jpg"},
    {"id": 3, "nome": "Nabucodonosor", "categoria": "Mesopotâmia", "imagem_url": "/imgs/03-nabucodonosor.jpg"},
    {"id": 4, "nome": "Sargão", "categoria": "Mesopotâmia", "imagem_url": "/imgs/04-sargao.jpg"},
    {"id": 5, "nome": "Assurbanipal", "categoria": "Mesopotâmia", "imagem_url": "/imgs/05-assurbanipal.jpg"},
    {"id": 6, "nome": "Ramsés II", "categoria": "Egito Antigo", "imagem_url": "/imgs/06-ramses-II.jpg"},
    {"id": 7, "nome": "Cleópatra", "categoria": "Egito Antigo", "imagem_url": "/imgs/07-cleopatra.jpg"},
    {"id": 8, "nome": "Tutancâmon", "categoria": "Egito Antigo", "imagem_url": "/imgs/08-tutancamon.jpg"},
    {"id": 9, "nome": "Hatshepsut", "categoria": "Egito Antigo", "imagem_url": "/imgs/09-hatshepsut.jpg"},
    {"id": 10, "nome": "Imhotep", "categoria": "Egito Antigo", "imagem_url": "/imgs/10-imhotep.jpg"},
    {"id": 11, "nome": "Sócrates", "categoria": "Grécia Antiga", "imagem_url": "/imgs/11-socrates.jpg"},
    {"id": 12, "nome": "Alexandre", "categoria": "Grécia Antiga", "imagem_url": "/imgs/12-alexander.jpg"},
    {"id": 13, "nome": "Péricles", "categoria": "Grécia Antiga", "imagem_url": "/imgs/13-pericles.jpg"},
    {"id": 14, "nome": "Pitágoras", "categoria": "Grécia Antiga", "imagem_url": "/imgs/14-pitagoras.jpg"},
    {"id": 15, "nome": "Homero", "categoria": "Grécia Antiga", "imagem_url": "/imgs/15-homero.jpg"},
    {"id": 16, "nome": "Júlio César", "categoria": "Império Romano", "imagem_url": "/imgs/16-julio-cesar.jpg"},
    {"id": 17, "nome": "Otávio Augusto", "categoria": "Império Romano", "imagem_url": "/imgs/17-otavio-augusto.jpg"},
    {"id": 18, "nome": "Marco Aurélio", "categoria": "Império Romano", "imagem_url": "/imgs/18-marco-aurelio.jpg"},
    {"id": 19, "nome": "Constantino", "categoria": "Império Romano", "imagem_url": "/imgs/19-constantino.jpg"},
    {"id": 20, "nome": "Espártaco", "categoria": "Império Romano", "imagem_url": "/imgs/20-espartaco.jpg"},
    {"id": 21, "nome": "Pirâmides", "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/imgs/21-piramides.jpg"},
    {"id": 22, "nome": "Jardins da Babilônia", "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/imgs/22-jardins-babilonia.jpg"},
    {"id": 23, "nome": "Estátua de Zeus", "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/imgs/23-estatua-zeus.jpg"},
    {"id": 24, "nome": "Templo de Ártemis", "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/imgs/24-templo-artemis.jpg"},
    {"id": 25, "nome": "Mausoléu", "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/imgs/25-mausoleu.jpg"},
    {"id": 26, "nome": "Colosso de Rodes", "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/imgs/26-colosso-rodes.jpg"},
    {"id": 27, "nome": "Farol de Alexandria", "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/imgs/27-farol-alexandria.jpg"},
]

# -------------------------------------------------
# Endpoint que retorna a lista de figurinhas
# -------------------------------------------------
@app.get("/figurinhas")
def listar_figurinhas():
    """Retorna a lista completa de figurinhas com seus metadados.

    Returns:
        list[dict]: Lista contendo dicionários de figurinhas.
    """
    return figurinhas
