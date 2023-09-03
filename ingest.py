import os
from dotenv import load_dotenv

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

from langchain.vectorstores import Pinecone
import pinecone

import tiktoken

def embedding_cost_calculator(chunks):
    model_cost = 0.0004 / 1000
    total_tokens = 0

    encoding = tiktoken.encoding_for_model("text-embedding-ada-002")

    for chunk in chunks:
        total_tokens += len(encoding.encode(chunk.page_content))

    cost = total_tokens * model_cost
    return f'{cost:.7f}'




load_dotenv()
pinecone.init(
    api_key=os.environ.get("PINECONE_API_KEY"),
    environment=os.environ.get("PINECONE_REGION")
)

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir,"qfin.pdf")

loader = PyPDFLoader(file_path=file_path)
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 100, chunk_overlap=20)
chunks = text_splitter.split_documents(data)

embedding = OpenAIEmbeddings(model="text-embedding-ada-002")

# print(embedding_cost_calculator(chunks=chunks))

Pinecone.from_documents(index_name="chatpdf", embedding=embedding, documents=chunks)