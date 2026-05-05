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

def iniciar_agente():

    total_threads = os.cpu_count() or 4
    threads_para_uso = total_threads - 4 if total_threads > 4 else total_threads
    
   
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    db = Chroma(persist_directory=CAMINHO_DB, embedding_function=embeddings)
    modelo = ChatOllama(model="llama3.2", temperature=0.3, num_thread=threads_para_uso)
    
    print("\n" + "="*30 + "\n🤖 AGENTE RAG ONLINE\n" + "="*30)
    print(f"🚀 Hardware otimizado: {threads_para_uso} threads em uso.")

    while True:
        print("\n" + "-"*50)
        pergunta_usuario = input("➤ Pergunta (ou Enter/Sair para finalizar): ").strip()

        # TRAVA DE SEGURANÇA: Se o input for vazio ou 'sair', encerra na hora
        if not pergunta_usuario or pergunta_usuario.lower() == "sair":
            print("\n" + "="*30)
            print("🛑 AGENTE FINALIZADO: Encerrando conexões... Até logo!")
            print("="*30)
            break 
        
        resultados = db._similarity_search_with_relevance_scores(pergunta_usuario, k=4)

        if not resultados or resultados[0][1] < 0.5:
            print("\n⚠️  Aviso: Não encontrei informações seguras nos documentos.")
            continue 

        base_conhecimento = resultados[0][0].page_content
        prompt = ChatPromptTemplate.from_template(prompt_template)
        prompt_formatado = prompt.format(pergunta_usuario=pergunta_usuario, base_conhecimento=base_conhecimento)
        
        print(f"📊 Score de Relevância: {resultados[0][1]:.4f}")
        print("✅ Resposta: ", end="", flush=True)
        
        inicio = time.time()
        
        for chunk in modelo.stream(prompt_formatado):
            print(chunk.content, end="", flush=True)
        
        tempo_final = time.time() - inicio
        print(f"\n\n⏱️  Tempo de processamento: {tempo_final:.2f}s")

if __name__ == "__main__":
    iniciar_agente()