# main.py – Versão final da API de álbum de figurinhas

"""
Servidor FastAPI que:
  - Libera acesso para o frontend via CORS
  - Lista as figurinhas cadastradas
  - Entrega a imagem de cada figurinha por um endpoint próprio
"""

# -------------------------------------------------
# Imports necessários
# -------------------------------------------------
import os
import glob

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# -------------------------------------------------
# Configuração de caminhos absolutos
# -------------------------------------------------
# Diretório onde este arquivo (main.py) está localizado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
# Diretório que contém as imagens das figurinhas
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# -------------------------------------------------
# Criação da aplicação FastAPI
# -------------------------------------------------
app = FastAPI()

# -------------------------------------------------
# Middleware CORS – aceita requisições de qualquer origem
# Isso permite que o frontend (rodando em outra porta/domínio)
# consiga consumir esta API sem bloqueio do navegador.
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Permite qualquer origem
    allow_credentials=True,    # Permite envio de cookies/credenciais
    allow_methods=["*"],       # Permite todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],       # Permite todos os cabeçalhos
)

# -------------------------------------------------
# Lista de figurinhas
# Cada figurinha possui: id, nome, categoria e imagem_url
# O imagem_url aponta para o endpoint /figurinhas/{id}/imagem
# Figurinhas comentadas ainda não possuem imagem na pasta figurinhas/
# -------------------------------------------------
figurinhas = [
    # ====== Mesopotâmia ======
    {"id": 1,  "nome": "Hamurábi",       "categoria": "Mesopotâmia",          "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2,  "nome": "Gilgamesh",      "categoria": "Mesopotâmia",          "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3,  "nome": "Nabucodonosor",  "categoria": "Mesopotâmia",          "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4,  "nome": "Sargão",         "categoria": "Mesopotâmia",          "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5,  "nome": "Assurbanípal",   "categoria": "Mesopotâmia",          "imagem_url": "/figurinhas/5/imagem"},

    # ====== Egito Antigo ======
    {"id": 6,  "nome": "Ramsés II",      "categoria": "Egito Antigo",         "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7,  "nome": "Cleópatra",      "categoria": "Egito Antigo",         "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8,  "nome": "Tutancâmon",     "categoria": "Egito Antigo",         "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9,  "nome": "Hatshepsut",     "categoria": "Egito Antigo",         "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Imhotep",        "categoria": "Egito Antigo",         "imagem_url": "/figurinhas/10/imagem"},

    # ====== Grécia Antiga ======
    {"id": 11, "nome": "Sócrates",       "categoria": "Grécia Antiga",        "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Alexandre",      "categoria": "Grécia Antiga",        "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Péricles",       "categoria": "Grécia Antiga",        "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Pitágoras",      "categoria": "Grécia Antiga",        "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Homero",         "categoria": "Grécia Antiga",        "imagem_url": "/figurinhas/15/imagem"},

    # ====== Roma Antiga ======
    {"id": 16, "nome": "Júlio César",    "categoria": "Roma Antiga",          "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Otávio Augusto", "categoria": "Roma Antiga",          "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Marco Aurélio",  "categoria": "Roma Antiga",          "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Constantino",    "categoria": "Roma Antiga",          "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Espártaco",      "categoria": "Roma Antiga",          "imagem_url": "/figurinhas/20/imagem"},

    # ====== Maravilhas do Mundo Antigo ======
    {"id": 21, "nome": "Pirâmides de Gizé",         "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Jardins da Babilônia",       "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Estátua de Zeus",            "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Templo de Ártemis",          "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Mausoléu de Halicarnasso",   "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Colosso de Rodes",           "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Farol de Alexandria",        "categoria": "Maravilhas do Mundo Antigo", "imagem_url": "/figurinhas/27/imagem"},
]


# -------------------------------------------------
# Endpoint GET "/figurinhas"
# Retorna a lista completa de figurinhas cadastradas
# -------------------------------------------------
@app.get("/figurinhas")
def listar_figurinhas():
    """Retorna a lista completa de figurinhas com seus metadados."""
    return figurinhas


# -------------------------------------------------
# Endpoint GET "/figurinhas/{id}/imagem"
# Busca o arquivo de imagem correspondente ao id na pasta figurinhas/
# Usa glob com o padrão "{id:02d}[!0-9]*" para localizar o arquivo
# Retorna 404 se nenhuma imagem for encontrada
# -------------------------------------------------
@app.get("/figurinhas/{id}/imagem")
def obter_imagem(id: int):
    """Retorna a imagem da figurinha correspondente ao id informado.

    O padrão de busca usa o id com dois dígitos seguido de qualquer
    caractere que NÃO seja dígito, garantindo que '01-*' não capture '010-*'.

    Args:
        id: Identificador numérico da figurinha.

    Returns:
        FileResponse: Arquivo de imagem encontrado.

    Raises:
        HTTPException 404: Se nenhuma imagem correspondente for encontrada.
    """
    # Monta o padrão de busca: ex. "01[!0-9]*" para id=1
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")

    # Procura arquivos que correspondam ao padrão
    arquivos = glob.glob(padrao)

    # Se não encontrou nenhum arquivo, retorna 404
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")

    # Retorna o primeiro arquivo encontrado como resposta de arquivo
    return FileResponse(arquivos[0])
