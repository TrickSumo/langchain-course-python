import tiktoken

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = PyPDFLoader(file_path="./q.pdf")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=30)
chunks = text_splitter.split_documents(data)

# print(chunks,len(chunks))

encoding = tiktoken.encoding_for_model("text-embedding-ada-002")
model_cost = 0.0004 / 1000

total_token = 0

for chunk in chunks:
    total_token = total_token + len(encoding.encode(chunk.page_content))


print(f"{total_token * model_cost:.7f}")

