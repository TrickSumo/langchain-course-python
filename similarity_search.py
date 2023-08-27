import os
from dotenv import load_dotenv
import pinecone

from sentence_transformers import SentenceTransformer

load_dotenv()

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_REGION")
)

index = pinecone.Index("demo")

model = SentenceTransformer('all-MiniLM-L6-v2')

query_vector = model.encode(["dog"]).tolist()

res = index.query(queries=query_vector, top_k=1, include_values=True)
print(res)