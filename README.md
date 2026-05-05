# 🤖 Agente IA RAG: Consultoria Inteligente e Arquitetura do Zero
Este projeto não é apenas uma ferramenta de consulta; é um estudo prático sobre como construir um Agente de IA do zero, manipulando variáveis críticas para obter precisão técnica e utilidade real. O foco aqui é entender como transformar uma LLM genérica em um especialista capaz de analisar documentos PDF específicos com alta fidelidade.

## 🎯 O Objetivo do Projeto
A criação deste agente foi guiada pelo desejo de compreender a anatomia de um sistema RAG (Retrieval-Augmented Generation):

* **Manipulação de Precisão**: Ajustar como a informação é recuperada e filtrada (via scores de relevância).

* **Atribuição de Função**: Transformar a IA em um assistente técnico que se baseia estritamente em uma base de conhecimento.

* **Domínio do Hardware**: Entender como o software pode "conversar" com o processador para maximizar a eficiência.

## 🚀 Escolha da LLM: Local vs Cloud
Neste projeto, foi uma escolha técnica minha utilizar LLMs locais (via Ollama). O objetivo principal foi garantir a privacidade absoluta dos dados e permitir experimentos ilimitados sem custos de API.

* **Nota**: Embora o projeto esteja configurado para o ecossistema local por padrão, a arquitetura é modular. Isso significa que você pode facilmente adaptar o código para utilizar outras LLMs (como GPT-4, Claude ou Gemini) apenas alterando os provedores no LangChain.
* [Caso utilize o Ollama](https://ollama.com/)

## 🛠️ Tecnologias e Bibliotecas
* **LangChain**: O "esqueleto" do agente, responsável por orquestrar o fluxo de dados.

* **ChromaDB**: Nosso banco de dados vetorial, onde o conhecimento é armazenado.

* **Ollama**: O motor que permite rodar a inteligência (Llama 3.2) e os Embeddings (Nomic) localmente.

* **PyPDF** & TextSplitters: Ferramentas para fragmentar o conhecimento em pedaços digeríveis pela IA.

* **Python**: Versão 3.14.4

## 🧠 Customização de Embeddings

Uma peça fundamental na arquitetura deste agente é o modelo de **Embedding**. Ele é responsável por transformar o texto do seu PDF em vetores matemáticos para que a IA realize a busca semântica. 

### Modelo Padrão: **nomic-embed-text**
Por escolha técnica, utilizamos o **`nomic-embed-text`** devido ao seu excelente equilíbrio entre performance local e precisão. Contudo, o projeto é modular e permite a troca fácil de modelos.

### Como alterar o modelo:
Caso deseje testar outras representações, altere a string do modelo nos arquivos `cria_db.py` e `main.py`:
```python
embeddings = OllamaEmbeddings(model="nome-do-modelo-desejado")
```
### Onde encontrar novos modelos?
Para facilitar a escolha, você pode consultar a biblioteca oficial do Ollama para descobrir novos modelos de embedding:
* [Ollama Library - Embedding Models](https://ollama.com/search?c=embedding)
  
## ⚙️ Configuração do Ambiente de Desenvolvimento

Para garantir que o agente rode perfeitamente no seu hardware e evitar conflitos de versões, siga este passo a passo técnico:

### 1. Preparação do Terreno (Setup)
Primeiro, isole o projeto criando um ambiente virtual e instale as bibliotecas necessárias:

```bash
# Criação do ambiente virtual (Recomendado)
py -m venv .venv

# Ativação do ambiente
# No Windows: .venv\Scripts\activate | No Linux/Mac: source .venv/bin/activate

```
### 2. Preparação do Terreno
Instale as bibliotecas necessárias para o seu ambiente:
```
pip install langchain langchain-ollama langchain-community langchain-chroma pypdf chromadb python-dotenv
```

### 3. Criação da Memória (Embedding)
Insira seus PDFs na pasta /base e execute:

```
python cria_db.py
```
Aqui você verá a mágica da Vetorização: transformar texto humano em coordenadas matemáticas que a IA consegue buscar por significado.

### 4. Execução do Agente
Inicie o diálogo com:

```
python main.py
```
## 🧠 Engenharia e Performance: Otimização de Threads
Uma das partes mais profundas deste projeto é o gerenciamento de recursos. Para garantir que a resposta seja gerada com velocidade sem travar o seu computador:

* **Cálculo de Hardware**: O agente identifica automaticamente o total de núcleos do CPU (ex: as 14 threads do seu processador).

* **Reserva de Segurança**: O código reserva automaticamente 4 threads para o Sistema Operacional, utilizando o restante para a "frequência de pensamento" da LLM.

* **Streaming**: A resposta é entregue em tempo real, permitindo que o usuário comece a leitura enquanto a IA ainda está finalizando o raciocínio.

Autor
```Tiago Lucas - Junior Quality Assurance Analyst & Engineer```

"Construindo hoje as ferramentas que automatizam o amanhã."
