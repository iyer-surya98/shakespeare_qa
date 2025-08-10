import os
import faiss
from langchain import hub
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_core.documents import Document

# IMPORTANT: make sure your openai API key is set!
print("Initializing chat model: gpt-4o-mini...")
chat_model = init_chat_model(model="gpt-4o-mini", api_key = os.environ.get("OPENAI_API_KEY"), temperature = 0.6)
print("Model initialized successfully. Now preparing embeddings and setting up an in-memory vector store...")
embeddings = OpenAIEmbeddings()
embedding_dim = len(embeddings.embed_query("hello world"))

index = faiss.IndexFlatL2(embedding_dim)
vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)
print("Vector store initialized successfully.")
print("Loading document and splitting into chunks...")
documents = TextLoader("shaks12.txt").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)
print(f"Successfully split the file into {len(texts)} chunks. Now adding to vector store...")
_ = vector_store.add_documents(texts)

prompt = hub.pull("rlm/rag-prompt")

# For now, accept command line input:
print("Ready for user query! Please enter your query:")
user_query = str(input)
relevant_documents: list[Document] = vector_store.search(query=user_query)
if relevant_documents:
    contents = "\n\n".join(document.page_content for document in relevant_documents)
prompt = prompt.invoke({
    "question": user_query,
    "context": contents
})
print("Thinking....")
answer = chat_model.invoke(prompt)
print(f"Model output: {answer}")