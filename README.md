# Chatbot para Documentos | RAG

Projeto desenvolvido para responder perguntas sobre arquivos PDF utilizando RAG (Retrieval-Augmented Generation), com recuperação semântica de contexto e geração de respostas por IA.

Os documentos enviados são processados, transformados em embeddings e armazenados no Pinecone, permitindo consultas em linguagem natural sobre um ou mais arquivos PDF.

## Funcionalidades

* Upload de um ou mais arquivos PDF
* Extração e divisão automática do texto em chunks
* Vetorização com embeddings da OpenAI
* Armazenamento vetorial no Pinecone
* Recuperação semântica de contexto por similaridade
* Respostas geradas pelo GPT-4o-mini com base nos documentos
* Indicação das fontes utilizadas em cada resposta
* Interface interativa desenvolvida com Streamlit

## Como Executar

1. Clone o repositório:

```txt
git clone https://github.com/seu-usuario/chatbot-documentos.git
```

2. Instale as dependências:

```txt
pip install -r requirements.txt
```

3. Crie um arquivo `.env` com suas chaves de API:

```txt
OPENAI_API_KEY=sua_chave
PINECONE_API_KEY=sua_chave
```

4. Execute a aplicação:

```txt
streamlit run app/ui.py
```

## Ferramentas Utilizadas

* Python
* LangChain
* OpenAI API (GPT-4o-mini + text-embedding-3-small)
* Pinecone
* Streamlit
* PyPDF

## Estrutura do Projeto

```txt
chatbot-documentos/
│
├── app/
│   └── ui.py
│
├── config/
│   └── llm.py
│
├── embeddings/
│   └── gerar_embeddings.py
│
├── ingest/
│   ├── leitura_pdf.py
│   └── dividir_texto.py
│
├── rag/
│   ├── prompt.py
│   ├── qa_chain.py
│   └── retriever.py
│
├── vectorstore/
│   └── criar_base.py
│
├── requirements.txt
└── README.md
```

## Aprendizados

Durante o desenvolvimento deste projeto, foram praticados conceitos relacionados a:

* Processamento e extração de texto de arquivos PDF
* Divisão de texto em chunks para preservação de contexto
* Geração e armazenamento de embeddings em banco vetorial
* Construção de pipelines RAG com LangChain
* Recuperação de contexto para perguntas e respostas
* Desenvolvimento de interfaces com Streamlit

## Próximos Passos

* Suporte a outros formatos de arquivo como .docx e .txt
* Histórico persistente das conversas
* Resumo automático dos documentos carregados

## Autor

Gustavo Locatelli Helena

LinkedIn:
https://www.linkedin.com/in/gustavo-locatelli-helena-9967b224b/
