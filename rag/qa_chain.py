from config.llm import modelo
from rag.prompt import PROMPT_RAG


def responder_pergunta(pergunta, retriever):

    documentos = retriever.invoke(pergunta)

    contexto = "\n\n".join([doc.page_content for doc in documentos])

    chain = PROMPT_RAG | modelo

    resposta = chain.invoke({"contexto": contexto, "pergunta": pergunta})

    return resposta.content, documentos