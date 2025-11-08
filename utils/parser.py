from PyPDF2 import PdfReader
from docx import Document
from ai_agent.yandex_gpt import generate_theme_blocks
path = "../files/new_document.pdf"


def read_pdf(path_pdf: str):
    text = str()
    reader = PdfReader(path_pdf)

    for page in reader.pages:
        text += page.extract_text()
    return text

def read_docx(path_docs: str):
    doc = Document(path_docs)
    text = str()
    for para in doc.paragraphs:
        text += para.text

print(read_pdf(path))
