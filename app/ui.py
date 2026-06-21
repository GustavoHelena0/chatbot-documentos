import streamlit as st

from vectorstore.criar_base import criar_base_vetorial
from rag.retriever import criar_retriever
from rag.qa_chain import responder_pergunta


st.set_page_config(page_title="Chatbot para Documentos", layout="wide")

st.title("Chatbot para Documentos")

st.caption("Faça perguntas sobre um ou mais arquivos PDF.")

documentos = st.file_uploader("Selecione um ou mais arquivos PDF", type="pdf", accept_multiple_files=True, label_visibility="collapsed")

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if documentos:

    if st.button("Processar Documentos"):

        with st.spinner("Processando documentos..."):

            vectorstore = criar_base_vetorial(documentos)

            st.session_state.retriever = criar_retriever(vectorstore)

        st.success("Documentos processados com sucesso!")

if st.session_state.retriever:

    pergunta = st.text_input("Digite sua pergunta:")

    if st.button("Enviar Pergunta"):

        with st.spinner("Gerando resposta..."):

            resposta, documentos_recuperados = responder_pergunta(pergunta, st.session_state.retriever)

        st.write(resposta)

        arquivos = set()

        for doc in documentos_recuperados:

            nome_arquivo = doc.metadata.get("arquivo")

            if nome_arquivo:

                arquivos.add(nome_arquivo)

        if arquivos:

            st.markdown("### Fontes utilizadas")

            for arquivo in sorted(arquivos):
                st.markdown(f"- {arquivo}")
