def criar_retriever(vectorstore):

    retriever = vectorstore.as_retriever(search_kwargs={"k": 8})

    return retriever