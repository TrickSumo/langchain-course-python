import os
from dotenv import load_dotenv
from fastapi import FastAPI
from openai import OpenAI
from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

import pinecone

load_dotenv()

# uvicorn app:app --host 0.0.0.0 --port 10000
app = FastAPI()

# Setup environment variables
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pinecone_api_key = os.getenv("PINECONE_API_KEY")
environment = os.getenv("PINECONE_ENV")
index_name = os.getenv("PINECONE_INDEX")

# Initialize pinecone client
pinecone.init(api_key=pinecone_api_key, environment=environment)
index = pinecone.Index(index_name)

# Middleware to secure HTTP endpoint
security = HTTPBearer()


def validate_token(
    http_auth_credentials: HTTPAuthorizationCredentials = Security(security),
):
    if http_auth_credentials.scheme.lower() == "bearer":
        token = http_auth_credentials.credentials
        if token != os.getenv("RENDER_API_TOKEN"):
            raise HTTPException(status_code=403, detail="Invalid token")
    else:
        raise HTTPException(status_code=403, detail="Invalid authentication scheme")


class QueryModel(BaseModel):
    query: str


@app.post("/")
async def get_context(
    query_data: QueryModel,
    credentials: HTTPAuthorizationCredentials = Depends(validate_token),
):
    # convert query to embeddings
    res = openai_client.embeddings.create(
        input=[query_data.query], model="text-embedding-ada-002"
    )
    embedding = res.data[0].embedding
    # Search for matching Vectors
    results = index.query(embedding, top_k=6, include_metadata=True).to_dict()
    # Filter out metadata fron search result
    context = [match["metadata"]["text"] for match in results["matches"]]
    # Retrun context
    return context


# @app.get("/")
# async def get_context(query: str = None, credentials: HTTPAuthorizationCredentials = Depends(validate_token)):

#     # convert query to embeddings
#     res = openai_client.embeddings.create(
#         input=[query],
#         model="text-embedding-ada-002"
#     )
#     embedding = res.data[0].embedding
#     # Search for matching Vectors
#     results = index.query(embedding, top_k=6, include_metadata=True).to_dict()
#     # Filter out metadata fron search result
#     context = [match['metadata']['text'] for match in results['matches']]
#     # Retrun context
#     return context
