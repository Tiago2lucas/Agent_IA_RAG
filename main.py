from langchain_chroma.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import  ChatPromptTemplate
from langchain_ollama import ChatOllama
import time
import os

CAMINHO_DB = "db"

prompt_template= """
Responsta a pergunta do usuário:
{pergunta_usuario}

com base nessas informações:

{base_conhecimento}
"""

def perguntar():
    pergunta_usuario= input("Digite sua pergunta:  ")

    function_ollmaEmbbengings = OllamaEmbeddings(model="nomic-embed-text")

    db = Chroma(persist_directory=CAMINHO_DB,
                embedding_function=function_ollmaEmbbengings
                )

    resultados= db._similarity_search_with_relevance_scores(pergunta_usuario, k=4)

    if len(resultados) == 0 or resultados[0][1] < 0.5:
        print("Desculpe, não encontrei informações relevantes no PDF.")
        
    
    score_topo = resultados[0][1]
        
    base_conhecimento = resultados[0][0].page_content
    
    total_threads = os.cpu_count() 
    threads_para_uso = total_threads - 4 if total_threads > 4 else total_threads
    
    
    prompt = ChatPromptTemplate.from_template(prompt_template)
    prompt_formatado = prompt.format(pergunta_usuario=pergunta_usuario, base_conhecimento=base_conhecimento)
    
    modelo = ChatOllama(model="llama3.2", temperature=0.3, num_thread=threads_para_uso)
    print(f"Score do resultado mais relevante: {score_topo:.4f}")
    print(f"🚀 Usando {threads_para_uso} threads")
    
    
    print("\n✅ Resposta da IA: ", end="", flush=True)
    
    inicio_time = time.time()
    
    for chunk in modelo.stream(prompt_formatado):
        print(chunk.content, end="", flush=True)
    
    fim_time = time.time()

    tempo_total = fim_time - inicio_time
    print(f"\n\n⏱️ Tempo total de processamento: {tempo_total:.2f} segundos.")
    

if __name__ == "__main__":
    perguntar()