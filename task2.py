from docling.document_converter import DocumentConverter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_core.vectorstores import VectorStoreRetriever

source = "./t3.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
text=result.document.export_to_markdown()
sentences = []
if text:
  lines = [line.strip() for line in text.split('.') if line.strip()]
  sentences.extend(lines)

EMBEDDING_MODEL = "intfloat/e5-small-v2"
embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
vector_store = FAISS.from_texts(texts=sentences, embedding=embedding_model)

llm="deepseek-r1:8b"
retriever = VectorStoreRetriever(vector_store)
retrievalQA = RetrievalQA.from_llm(llm=llm, retriever=retriever)