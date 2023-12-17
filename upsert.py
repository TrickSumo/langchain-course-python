import os
from dotenv import load_dotenv

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

from langchain.vectorstores import Pinecone
import pinecone

import tiktoken

load_dotenv()
pinecone.init(
    api_key=os.environ.get("PINECONE_API_KEY"),
    environment=os.environ.get("PINECONE_ENV"),
)

current_dir = os.path.dirname(__file__)
docs_dir = os.path.join(current_dir, "data")

embedding = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key="")


def embedding_cost_calculator(chunks):
    model_cost = 0.0004 / 1000
    total_tokens = 0
    encoding = tiktoken.encoding_for_model("text-embedding-ada-002")
    for chunk in chunks:
        total_tokens += len(encoding.encode(chunk.page_content))
    cost = total_tokens * model_cost
    return f"{cost:.7f}"


def estimate_total_cost():
    total_estimated_cost = 0

    for root, dirs, files in os.walk(docs_dir):
        for filename in files:
            print(root, filename)
            if filename.endswith(".pdf"):  # Check if the file is a PDF
                file_path = os.path.join(root, filename)
                # Load and process the file
                loader = PyPDFLoader(file_path=file_path)
                data = loader.load()
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=100, chunk_overlap=20
                )
                chunks = text_splitter.split_documents(data)

                cost_of_embedding_file = embedding_cost_calculator(chunks=chunks)
                total_estimated_cost += float(cost_of_embedding_file)

                print(cost_of_embedding_file)

    return total_estimated_cost


def ingest_to_pinecone():
    for root, dirs, files in os.walk(docs_dir):
        for filename in files:
            print("ingesting file:- " + filename)
            if filename.endswith(".pdf"):  # Check if the file is a PDF
                file_path = os.path.join(root, filename)
                # Load and process the file
                loader = PyPDFLoader(file_path=file_path)
                data = loader.load()
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=100, chunk_overlap=20
                )
                chunks = text_splitter.split_documents(data)

                # Store in Pinecone
                Pinecone.from_documents(
                    index_name="rag369", embedding=embedding, documents=chunks
                )

    return True


print("Total estimated cost is:- " + str(estimate_total_cost()))
if input("Would you like to continue? Press y for yes:- ") == "y":
    print("Starting ingest_to_pinecone")
    ingest_to_pinecone()
else:
    print("Operation Aborted!")
