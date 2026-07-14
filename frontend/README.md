# 🏆 Álbum Histórico - Civilizações da Antiguidade

O **Álbum Histórico** é um tributo interativo às grandes civilizações, monumentos e povos da Idade Antiga. Ele consiste em um álbum digital de figurinhas que celebra governantes lendários, filósofos influentes e as Sete Maravilhas do Mundo Antigo da Mesopotâmia, Egito Antigo, Grécia Antiga e Império Romano.

O projeto traz uma experiência imersiva e tátil através de uma interface baseada em um livro real que pode ser folheado, acompanhado por efeitos sonoros e integração a uma API de backend para carregamento dinâmico das figurinhas.

---

## 📂 Estrutura dos Arquivos do Frontend

O projeto do frontend é composto por três arquivos principais, organizados de forma modular e limpa:

### 1. 📄 [index.html](index.html)
* **Objetivo:** Define o esqueleto e a estrutura semântica da aplicação.
* **Funcionalidades:**
  * Define o layout físico do álbum com tags semânticas da HTML5.
  * Estrutura a capa (agora com arte temática clássica de civilizações antigas em `cover-art.png`), contracapa e as páginas internas de conteúdo divididas por categorias históricas (Mesopotâmia, Egito, Grécia, Roma, Maravilhas I e Maravilhas II).
  * Organiza os slots individuais (`.sticker-slot`) onde cada figurinha será colada.
  * Importa as dependências do projeto: a biblioteca `page-flip` (via CDN) para a simulação física do livro, a folha de estilos `style.css` e o arquivo de controle lógico `app.js`.

### 2. 🎨 [style.css](style.css)
* **Objetivo:** Estabelece o design visual, animações e a responsividade da aplicação.
* **Funcionalidades:**
  * Define uma paleta de cores clássica e imersiva em tons de **terracota, bronze, ouro antigo e pergaminho**, criando um clima de relíquia histórica.
  * Renderiza o design do livro, suas páginas (páginas esquerdas, direitas, capa e contracapa) e os efeitos realistas de sombreamento e dobras tridimensionais.
  * Adiciona efeitos interativos de hover nas páginas e botões, além de um efeito especial de animação *glitch* nos títulos principais.
  * Controla os slots das figurinhas, adicionando uma animação de "surgimento" e bordas especiais para as figurinhas raras (como os *slots especiais*).
  * Garante que o layout seja responsivo em telas menores e dispositivos móveis.

### 3. ⚙️ [app.js](app.js)
* **Objetivo:** Implementa o comportamento interativo, efeitos de áudio e a integração com dados dinâmicos.
* **Funcionalidades:**
  * **Carregamento Dinâmico:** Busca os dados das figurinhas a partir de uma API backend (`http://localhost:8000/figurinhas`) de forma assíncrona e cola as imagens nos slots correspondentes.
  * **Interatividade do Livro:** Inicializa e gerencia a biblioteca `St.PageFlip`, adaptando o arraste por toque e cliques para uma transição suave de 800ms.
  * **Efeitos de Áudio:** Sintetiza em tempo real um ruído de papel sendo folheado utilizando a *Web Audio API* (eliminando a necessidade de arquivos pesados de áudio `.mp3`).
  * **Controles do Usuário:** Gerencia o botão de ativação/mudo do áudio e implementa atalhos de teclado (setas direcionais esquerda/direita) para mudar de página.

---

## 🛠️ Tecnologias Utilizadas

* **HTML5:** Estruturação semântica da página.
* **CSS3 (Vanilla):** Estilização, animações e layout flexível.
* **JavaScript (Moderno/ES6+):** Integração com API (Fetch API), manipulação de DOM e lógica de áudio.
* **Web Audio API:** Geração procedural de som para otimizar a performance.
* **Page-Flip Library (St.PageFlip):** Biblioteca para simular a física de virar páginas de um livro físico.

---

## 🚀 Como Executar o Frontend

Para visualizar e interagir com o álbum em sua máquina:

1. Certifique-se de que os arquivos do frontend estejam em um servidor web local. Se você utiliza o VS Code, pode usar a extensão **Live Server** para rodar a aplicação.
2. Inicie o servidor da API de figurinhas (backend) para preencher o seu álbum. O comando sugerido para inicialização do servidor Python (FastAPI) é:
   ```bash
   cd backend/dia-3
   uvicorn main:app --reload
   ```
3. Abra o endereço gerado pelo seu servidor local (ex: `http://127.0.0.1:5500/index.html`) em qualquer navegador moderno.
