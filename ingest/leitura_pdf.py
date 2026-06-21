from pypdf import PdfReader

def ler_pdf(caminho_pdf):
    pdf = PdfReader(caminho_pdf)
    texto =""
    
    for pagina in pdf.pages:
        
        texto += pagina.extract_text() +"\n"

    return texto