from docling.document_converter import DocumentConverter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS



source = "./task2_data.pdf"  
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

query = "What is langchain?"

top_k = 3
results = vector_store.similarity_search_with_score(query, k=top_k)

retrieved_chunks = [doc[0].page_content for doc in results]
scores = [float(doc[1]) for doc in results]

output = {"chunks": retrieved_chunks,"scores": scores}
print(output)