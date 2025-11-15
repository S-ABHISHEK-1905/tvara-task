from PyPDF2 import PdfReader

def load_pdf(path: str) -> str:
    reader = PdfReader(path)
    text = []

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)

    return "\n".join(text).strip()
