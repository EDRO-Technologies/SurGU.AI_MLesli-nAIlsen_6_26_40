from PyPDF2 import PdfReader
from docx import Document
from ai_agent.yandex_gpt import generate_theme_blocks
# path = "../files/new_document.pdf"


def read_pdf(bytes_):
    text = str()
    reader = PdfReader(bytes_)

    for page in reader.pages:
        text += page.extract_text()
    return text

def read_docx(path_docs: str):
    doc = Document(path_docs)
    text = str()
    for para in doc.paragraphs:
        text += para.text

