from langchain.text_splitter import RecursiveCharacterTextSplitter

def dividir_texto(texto):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=[
            "\n\n\n",
            "\n\n",
            "\n",
            ". ",
            "; ",
            " ",
            ""
        ]
    )

    chunks = text_splitter.split_text(texto)

    return chunks