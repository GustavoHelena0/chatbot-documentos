from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
import tempfile
import os
from ingest.leitura_pdf import ler_pdf
from ingest.dividir_texto import dividir_texto
from embeddings.gerar_embeddings import carregar_embeddings

load_dotenv()

def criar_base_vetorial(documentos):

    todos_documentos = []

    for documento in documentos:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(documento.read())
            temp_path = tmp.name

        texto = ler_pdf(temp_path)

        os.unlink(temp_path)

        chunks = dividir_texto(texto)

        for chunk in chunks:
            todos_documentos.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "arquivo": documento.name
                    }
                )
            )

    modelo_embeddings = carregar_embeddings()

    vectorstore = None
    lote = 50

    for i in range(0, len(todos_documentos), lote):
        batch = todos_documentos[i:i + lote]

        if vectorstore is None:
            vectorstore = PineconeVectorStore.from_documents(documents=batch, embedding=modelo_embeddings, index_name="chatbot-documentos")
        else:
            vectorstore.add_documents(batch)

    return vectorstore