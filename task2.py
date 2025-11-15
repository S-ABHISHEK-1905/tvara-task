from docling.document_converter import DocumentConverter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS



source = "./task2_data.pdf"  
converter = DocumentConverter()
result = converter.convert(source)
text=result.document.export_to_markdown()

chunks = []

# Used a chunk size of 200 because the pdf contains statements of short facts about Langchain and Rag
chunk_size = 200
overlap = 50

start = 0
while start < len(text):
    end = start + chunk_size
    chunk = text[start:end].strip()
    if chunk:
        chunks.append(chunk)
    start = end - overlap 


EMBEDDING_MODEL = "intfloat/e5-small-v2"
embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
vector_store = FAISS.from_texts(texts=chunks, embedding=embedding_model)

query = "What is langchain?"

top_k = 3
results = vector_store.similarity_search_with_score(query, k=top_k)

retrieved_chunks = [doc[0].page_content for doc in results]
scores = [float(doc[1]) for doc in results]

output = {"chunks": retrieved_chunks,"scores": scores}
print(output)