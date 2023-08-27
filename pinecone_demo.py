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

# res = index.describe_index_stats()
# print(res)

model = SentenceTransformer('all-MiniLM-L6-v2')

#Our sentences we like to encode
sentences = ['This framework generates embeddings for each input sentence',
    'Sentences are passed as a list of string.',
    'The quick brown fox jumps over the lazy dog.']

#Sentences are encoded by calling model.encode()
embeddings = model.encode(sentences).tolist()


index.upsert(vectors=zip(['1','2','3'],embeddings))


res = index.describe_index_stats()
print(res)
